import redis
from faker import Faker
from threading import Thread
import os


class MeetupManager:
    def __init__(self):
        redis_host = os.getenv("REDIS_HOST", "localhost")
        redis_port = int(os.getenv("REDIS_PORT", 6379))
        
        self.redis = redis.Redis(
            host=redis_host, port=redis_port, decode_responses=True
        )
        self.faker = Faker()
        
    def seed_fake_events(self):
        tehran_center = (51.3890, 35.6892)
        
        for i in range(1, 6):
            event_id = f"event:{i}"
            
            # تولید مختصات تصادفی در شعاع ۱۰ کیلومتری مرکز تهران
            lon = tehran_center[0] + (self.faker.random.uniform(-0.05, 0.05))
            lat = tehran_center[1] + (self.faker.random.uniform(-0.05, 0.05))
            
            # 1. Hashes: ذخیره اطلاعات رویداد
            self.redis.hset(event_id, mapping={
                "title": self.faker.catch_phrase(),
                "owner": self.faker.first_name(),
                "capacity": 10
            })
            
            # 2. Geo: ثبت موقعیت مکانی
            self.redis.geoadd("events:geo", (lon, lat, event_id))
            
            # 3. Sorted Sets: مقداردهی اولیه امتیاز (تعداد لایک)
            self.redis.zadd("events:trending", {event_id: 0})
            
        print("✅ Database filled by fake data.")
        

    def find_nearby_events(self, user_lon, user_lat, radius_km=5):
        
        nearby_ids = self.redis.geosearch(
            "events:geo", 
            longitude=user_lon, 
            latitude=user_lat, 
            radius=radius_km, 
            unit='km',
            withdist=True,  # برگرداندن فاصله
            withcoord=True, # برگرداندن مختصات
            sort='ASC',     # مرتب‌سازی بر اساس نزدیک‌ترین
            count=10        # محدودیت تعداد نتایج
        )
        
        events = []
        for event in nearby_ids:
            event_id = event[0]
            details = self.redis.hgetall(event_id)
            details['id'] = event_id
            details['distance'] = f"{event[1]} km"
            events.append(details)
            
        return events

    def like_event(self, event_id):
        self.redis.zincrby("events:trending", 1, event_id)
    
    def get_trending_events(self, top_n=3):
        return self.redis.zrevrange("events:trending", 0, top_n-1, withscores=True)
    
    def register_for_event(self, event_id, user_id):
        attendees_key = f"{event_id}:attendees"

        with self.redis.pipeline() as pipe:
            while True:  # الگوی استاندارد retry برای WATCH
                try:
                    # هر دو کلیدی که تصمیم به اونها وابسته‌ست
                    pipe.watch(event_id, attendees_key)

                    # بعد از watch، خوندن باید از خود pipe باشه
                    capacity = pipe.hget(event_id, "capacity")
                    if capacity is None:
                        print("❌ Event not found.")
                        return False

                    if int(capacity) <= 0:
                        print("❌ Event is full.")
                        return False

                    if pipe.sismember(attendees_key, user_id):
                        print("⚠️ Duplicate registration.")
                        return False

                    pipe.multi()
                    pipe.hincrby(event_id, "capacity", -1)
                    pipe.sadd(attendees_key, user_id)
                    pipe.lpush(f"chat:{event_id}:history",
                            f"System: {user_id} joined the event!")
                    pipe.ltrim(f"chat:{event_id}:history", 0, 99) # محدود کردن تاریخچه
                    pipe.execute()

                    print("✅ Register successful")
                    return True

                except redis.WatchError:
                    continue  # داده عوض شده؛ از اول می‌خونیم

    
    def start_live_chat(self, event_id, user_id):
        channel = f"chat:{event_id}"
        pubsub = self.redis.pubsub()
        pubsub.subscribe(channel)
        
        # تابع شنونده در یک Thread جداگانه
        def listener():
            print(f"\n🎧 Connected to {event_id} chat (Ctrl+C to Exit)")
            for message in pubsub.listen():
                if message['type'] == 'message':
                    print(f"\n💬 {message['data']}")
                    print(">", end="", flush=True) # برگرداندن prompt به کاربر
            
        # اجرای Thread
        thread = Thread(target=listener, daemon=True)
        thread.start()
        
        try:
            while True:
                msg = input('> ')
                if msg.lower() == 'exit':
                    break
                
                # انتشار پیام (Pub/Sub)
                self.redis.publish(channel, f"{user_id}: {msg}")
                
                # ذخیره در تاریخچه Lists
                self.redis.lpush(f"{channel}:history", f"{user_id}: {msg}")
                
        except KeyboardInterrupt:
            pass
        finally:
            pubsub.unsubscribe(channel)
            print("Logged out.")

if __name__ == "__main__":
    app = MeetupManager()
    app.seed_fake_events()
    
    current_user = input("Enter Username: ")
        
    while True:
        print("\n--- MAIN MENU ---")
        print("1. Find vents near me")
        print("2. View trending events")
        print("3. Register for an event")
        print("4. Join a live event chat")
        print("5. Like an event")
        print("0. Logout")
        
        choice = input("Please select: ")
        
        if choice == '1':
            # مختصات فرضی کاربر (مثلاً میدان ونک تهران)
            events = app.find_nearby_events(51.4050, 35.7550, 7)
            for e in events: print(e)
            
        elif choice == '2':
            trending = app.get_trending_events()
            print("🔥 Threndings:", trending)
            
        elif choice == '3':
            event_id = input("Event ID (event:1): ")
            app.register_for_event(event_id, current_user)
            
        elif choice == '4':
            event_id = input("Event ID for chat: ")
            app.start_live_chat(event_id, current_user)
            
        elif choice == '5':
            event_id = input("Event ID for like: ")
            app.like_event(event_id)
            
        elif choice == '0':
            break
