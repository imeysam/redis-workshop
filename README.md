# 🚀 Local Meetups & Live Chat (Redis Workshop)

![Python](https://img.shields.io/badge/Python-3.8+-blue?logo=python)
![Redis](https://img.shields.io/badge/Redis-8.0-red?logo=redis)
![Docker](https://img.shields.io/badge/Docker-Ready-blue?logo=docker)
![License](https://img.shields.io/badge/License-MIT-green)
   
## 🎓 کارگاه آموزش عملی Redis با Python

یک پروژه‌ی آموزشی و عملی برای یادگیری Redis با استفاده از **Python** و کتابخانه‌ی رسمی/رایج `redis-py` که در قالب یک برنامه‌ی CLI سناریوی **رویدادهای محلی (Meetups)** را شبیه‌سازی می‌کند.

در این پروژه، Redis فقط به عنوان یک Cache ساده استفاده نشده؛ بلکه چند قابلیت مهم آن در یک سناریوی واقعی کنار هم قرار گرفته‌اند:

- جستجوی رویدادهای نزدیک با **Geo**
- نگهداری اطلاعات رویداد با **Hash**
- ساخت Leaderboard با **Sorted Set**
- نگهداری اعضای ثبت‌نام‌شده با **Set**
- ذخیره‌ی تاریخچه‌ی چت با **List**
- چت زنده با **Pub/Sub**
- ثبت‌نام اتمیک در رویداد با **WATCH + MULTI/EXEC**
- تولید داده‌ی تست با **Faker**

علاوه بر کد پروژه، این README یک مرجع آموزشی برای کار با **String, List, Hash, Set, Sorted Set, Geo, Pub/Sub, Blocking Queue, Transaction, MONITOR و INFO** نیز ارائه می‌دهد.

<br>

<div dir="rtl" align="center">

### ⚠️ **نکته مهم:** این پروژه صرفاً برای **آموزش، تمرین و آزمایش Redis** طراحی شده است.

</div>

<br>

## 🚫 این پروژه مناسب نیست برای:

- ✖️ محیط Production بدون بازبینی
- ✖️ ذخیره‌سازی داده‌های واقعی و حساس
- ✖️ سیستم‌های مالی یا تراکنش‌های حیاتی بدون طراحی مستقل
- ✖️ استفاده‌ی مستقیم در معماری سازمانی بدون اعمال Security, Observability و Error Handling مناسب
- ✖️ استفاده‌ی مستقیم از CLI به عنوان رابط کاربری محصول نهایی

<br>

## ✅ این پروژه مناسب است برای:

- ✔️ یادگیری Data Structureهای Redis
- ✔️ تمرین دستورات Redis با `redis-cli`
- ✔️ یادگیری اتصال Python به Redis
- ✔️ درک کاربرد Redis در Queue، Leaderboard و Real-time Communication
- ✔️ یادگیری Transaction و Optimistic Locking
- ✔️ نمونه‌سازی سریع قبل از پیاده‌سازی در پروژه‌های واقعی
- ✔️ آمادگی برای مصاحبه‌های Backend

<br>

> **📌 توجه:** داده‌های رویدادها در زمان اجرای برنامه به صورت Fake و با `Faker` تولید می‌شوند. مختصات نیز در اطراف مرکز تهران به صورت تصادفی تولید می‌شوند.

<br>

---

## 📚 فهرست

- [مفاهیم پایه](#basics)
- [سناریوی پروژه](#project-scenario)
- [معماری و ساختار برنامه](#architecture)
- [ساختار کلیدها در Redis](#key-design)
- [پیش‌نیازها](#prerequisites)
- [راه‌اندازی سریع](#quick-start)
- [آموزش دستورات Redis](#redis-commands)
  - [داده‌ساختار String](#string)
  - [داده‌ساختار List](#list)
  - [داده‌ساختار Hash](#hash)
  - [داده‌ساختار Set](#set)
  - [داده‌ساختار Sorted Set](#sorted-set)
  - [داده‌ساختار Geo](#geo)
  - [داده‌ساختار Pub/Sub](#pubsub)
  - [داده‌ساختار Blocking Queue](#blocking-queue)
  - [داده‌ساختار Transaction](#transaction)
  - [داده‌ساختار MONITOR و INFO](#monitor-info)
- [نکات مهم پیاده‌سازی](#implementation-notes)
- [جمع‌بندی مفاهیم](#concept-summary)
- [منابع](#resources)
- [نویسنده](#author)

<br>

---

<h2 id="basics">📖 مفاهیم پایه</h2>

<div dir="rtl" align="right">

### Redis

دیتابیس **Redis** یک data structure server سریع است که داده‌ها را به وسیله‌ی Key و Value در اختیار برنامه قرار می‌دهد و Data Typeهای مختلفی مثل String، List، Hash، Set و Sorted Set را به صورت native ارائه می‌کند.

دیتاببیس Redis در بسیاری از پروژه‌ها برای مواردی مانند:

</div>

- Cache
- Session
- Counter
- Leaderboard
- Queue
- Rate Limiting
- Pub/Sub
- Temporary State
- Distributed Coordination

<div dir="rtl" align="right">

استفاده می‌شود.

منطق اصلی Redis ساده است و داده‌ها بصورت کلید/مقدار ذخیره می‌شوند:

</div>

```text
KEY  ->  VALUE
```

<div dir="rtl" align="right">

اما نوع `VALUE` می‌تواند یکی از Data Structureهای مختلف Redis باشد.

</div>

<br>

### 🔑 Key و Value

برای مثال:


```bash
SET user:name "Kaveh"
GET user:name
```

<div dir="rtl" align="right">

در این مثال:

</div>


```text
Key   = user:name
Value = Kaveh
Type  = String
```

<div dir="rtl" align="right">

یا:

</div>

```bash
HSET event:1 title "Redis Workshop" owner "Bahraam" capacity 10
```

<div dir="rtl" align="right">

در اینجا:

</div>

```text
Key   = event:1
Type  = Hash
Fields:
    title
    owner
    capacity
```


<br>

<div dir="rtl" align="right">

### 🧠 چرا Data Type مناسب مهم است؟

 دیتابیس Redis چند Data Type مختلف دارد چون هرکدام برای یک مدل داده یا عملیات خاص مناسب‌ترند. انتخاب Data Type درست باعث می‌شود:

- مدل داده ساده‌تر شود.
- عملیات موردنیاز مستقیم‌تر باشد.
- تعداد Round Tripها کاهش پیدا کند.
- از پیاده‌سازی‌های پیچیده و غیرضروری جلوگیری شود.

مثلاً برای:

| نیاز | Data Type مناسب |
|------|-----------------|
| یک مقدار ساده یا Counter | String |
| صف یا Stack ساده | List |
| Object کوچک با Field/Value | Hash |
| مجموعه‌ی یکتا | Set |
| Ranking / Leaderboard | Sorted Set |
| جستجو بر اساس مختصات | Geo |
| ارسال پیام Real-time | Pub/Sub |

</div>

<br>

---

<h2 id="project-scenario">🎯 سناریوی پروژه</h2>

<div dir="rtl" align="right">

پروژه یک سیستم بسیار ساده برای **Meetup / Event** است.

کاربر می‌تواند:

1. رویدادهای نزدیک به موقعیت خود را پیدا کند.
2. لیست رویدادهای محبوب را ببیند.
3. در یک رویداد ثبت‌نام کند.
4. وارد چت زنده‌ی همان رویداد شود.
5. به یک رویداد Like بدهد.

برای پیاده‌سازی هر بخش از یک قابلیت Redis استفاده شده است.

</div>

<br>

| قابلیت پروژه | Redis Feature | دلیل استفاده |
|---|---|---|
| اطلاعات رویداد | **Hash** | نگهداری چند Field مرتبط زیر یک Key |
| موقعیت جغرافیایی | **Geo** | جستجوی رویدادها بر اساس فاصله |
| Trending | **Sorted Set** | نگهداری امتیاز و مرتب‌سازی |
| شرکت‌کنندگان | **Set** | جلوگیری از ثبت‌نام تکراری |
| تاریخچه چت | **List** | نگهداری پیام‌ها به ترتیب ورود |
| چت آنلاین | **Pub/Sub** | Broadcast پیام به Subscriberها |
| ثبت‌نام ایمن | **Transaction + WATCH** | جلوگیری از Race Condition در ظرفیت رویداد |

> **📌 نکته:** در خود برنامه‌ی فعلی از **String، Blocking Queue و MONITOR/INFO** استفاده نشده است؛ این موارد در README به عنوان بخش آموزشی Redis پوشش داده شده‌اند تا مرز بین «قابلیت‌های مورد استفاده در پروژه» و «دستورات آموزشی» مشخص باشد.

<br>

---

<h2 id="architecture">🏗️ معماری و ساختار برنامه</h2>

```plaintext
redis-workshop/
│
├── .env.example
├── .gitignore
├── Dockerfile
├── README.md
├── docker-compose.yml
├── main.py
└── requirements.txt
```

<br>

| فایل | توضیح |
|---|---|
| `.env.example` | نمونه متغیرهای محیطی Redis |
| `Dockerfile` | ایمیج اجرای Python برای اجرای کل برنامه در Docker |
| `docker-compose.yml` | اجرای Redis و نسخه Dockerized برنامه |
| `main.py` | منطق اصلی MeetupManager و رابط CLI |
| `requirements.txt` | وابستگی‌های Python |
| `README.md` | مستندات و آموزش پروژه |

<br>

---

<h2 id="key-design">🗝️ طراحی کلیدهای Redis در پروژه</h2>

یکی از مهم‌ترین نکات کار با Redis، طراحی درست Keyها است.

در این پروژه Keyها با یک Naming Convention ساده طراحی شده‌اند:

| Key Pattern | Type | کاربرد |
|---|---|---|
| `event:{id}` | Hash | اطلاعات اصلی Event |
| `events:geo` | Geo | مختصات Eventها |
| `events:trending` | Sorted Set | امتیاز Like |
| `event:{id}:attendees` | Set | کاربران ثبت‌نام‌شده |
| `chat:{id}` | Pub/Sub Channel | کانال چت |
| `chat:{id}:history` | List | تاریخچه پیام‌ها |

<br>

مثال:

```text
event:1
event:2
event:3
...
```

برای یک Event:

```text
event:1
├── title
├── owner
└── capacity
```

و برای شرکت‌کنندگان:

```text
event:1:attendees
```

و تاریخچه چت:

```text
chat:event:1:history
```

این الگو باعث می‌شود Keyها قابل پیش‌بینی، گروه‌بندی‌شده و قابل فهم باشند.

<br>

---

<h2 id="prerequisites">📋 پیش‌نیازها</h2>



### برای روش پیشنهادی این README

<div dir="rtl" align="left">

- Docker
- Docker Compose
- Git

</div>

<br>

---

<h2 id="quick-start">🛠️ راه‌اندازی سریع</h2>

### 1. دریافت پروژه

```bash
git clone https://github.com/imeysam/redis-workshop.git
cd redis-workshop
```

<br>

### 2. تنظیم اتصال Python به Redis

برای اجرای Python خارج از Docker:

```bash
cp .env.example .env
```
<br>

### 3. ساخت و اجرای containerها

```bash
docker compose up -d
```

<br>

### 4. بررسی Redis

```bash
docker exec -it redis redis-cli ping
```

باید خروجی زیر را ببینید:

```text
PONG
```

<br>


### 5. اجرای برنامه

```bash
python main.py
```

<br>

---

<h2 id="redis-commands">📚 آموزش دستورات Redis</h2>

<div dir="rtl" align="right">

در این بخش مهم‌ترین Data Structureهای موردنیاز این Workshop را با `redis-cli` بررسی می‌کنیم.

تمام مثال‌ها را می‌توانید با ورود به CLI اجرا کنید:

</div>
<div dir="rtl" align="left">

```bash
docker exec -it redis redis-cli
```

</div>

<br>

---

<h2 id="string">🧵 String</h2>

<div dir="rtl" align="right">

نوع داده String ساده‌ترین Data Type در Redis است و برای نگهداری مقدارهای متنی، Binary Data و Counterهای عددی بسیار مناسب است.

</div>

<br>

### SET و GET

```bash
SET user:name "Kian"
GET user:name
```

خروجی:

```text
Kian
```

<br>

### بررسی وجود Key

```bash
EXISTS user:name
```

خروجی:

```text
1
```

<br>

### حذف

```bash
DEL user:name
```

<br>

### چند SET همزمان

```bash
MSET user:first_name "Bahram" user:last_name "Irani"
```

خواندن چند مقدار:

```bash
MGET user:first_name user:last_name
```

<br>

### Counter

```bash
SET event:likes 0
INCR event:likes
INCRBY event:likes 5
GET event:likes
```

خروجی نهایی:

```text
6
```

<br>

### کاهش Counter

```bash
DECR event:likes
DECRBY event:likes 2
```

<br>

### APPEND

```bash
SET message "Hello"
APPEND message " Redis"
GET message
```

خروجی:

```text
Hello Redis
```

<br>

### شرط NX

فقط اگر Key وجود نداشته باشد مقدار جدید نوشته می‌شود:

```bash
SET lock:order 123 NX
```

<br>

### ثبت تاریخ انقضا هنگام SET

```bash
SET otp:user:1 123456 EX 60
TTL otp:user:1
```

مقدار بعد از 60 ثانیه منقضی می‌شود.

<br>

### کاربردهای متداول String

| کاربرد | مثال |
|---|---|
| Cache | `page:/products` |
| Counter | `post:10:views` |
| Feature Flag | `feature:new-checkout` |
| OTP | `otp:user:1` |
| Lock | `lock:order:10` |
| Session State | `session:123` |

<br>

---

<h2 id="list">📋 List</h2>

<div dir="rtl" align="right">

نوع داده List یک sequence از Stringها است و برای Queue، Stack، Log و داده‌های ترتیبی مناسب است.

</div>

<br>

### ورود آیتم جدید از سمت چپ (LPUSH)

```bash
LPUSH tasks "task-1"
LPUSH tasks "task-2"
LPUSH tasks "task-3"
```

مقدار List:

```text
task-3
task-2
task-1
```

<br>

### ورود آیتم جدید از سمت راست (RPUSH)

```bash
RPUSH tasks "task-4"
```

<br>

### نمایش تمام آیتم‌های اول تا چهارم List

```bash
LRANGE tasks 0 3
```

<br>

### نمایش تمام آیتم‌های List

```bash
LRANGE tasks 0 -1
```

<br>

### برداشت آیتم توسط LPOP و RPOP

```bash
LPOP tasks
RPOP tasks
```

دستور `LPOP` از سمت چپ و `RPOP` از سمت راست حذف می‌کند.

<br>

### نمایش یک عضو با ایندکس خاص

```bash
LINDEX tasks 0
```

<br>

### نمایش طول List

```bash
LLEN tasks
```

<br>

### محدود کردن اندازه LIST

```bash
LTRIM tasks 0 99
```

یعنی فقط 100 عنصر اول از سمت چپ نگهداری شوند.

این تکنیک دقیقاً در تاریخچه‌ی Chat پروژه استفاده شده است.

<br>

---

<h2 id="hash">🧩 Hash</h2>

<div dir="rtl" align="right">

نوع داده Hash برای نگهداری مجموعه‌ای از Field/Valueها در یک Key استفاده می‌شود.

از نظر مفهومی شبیه یک Dictionary است:

</div>
<div dir="rtl" align="left">

```text
event:1
    title     -> Redis Workshop
    owner     -> Abtin
    capacity  -> 10
```

</div>

<br>

### درج داده جدید

```bash
HSET event:1 title "Redis Workshop" owner "Kambiz" capacity 10
```

<br>

### نمایش یک فیلد

```bash
HGET event:1 title
```

<br>

### نمایش همه فیلدها و داده‌ها

```bash
HGETALL event:1
```

<br>

### بررسی وجود Field

```bash
HEXISTS event:1 title
```

<br>

### حذف Field

```bash
HDEL event:1 owner
```

<br>

### افزایش عدد داخل Hash

```bash
HINCRBY event:1 capacity -1
```

<br>

### گرفتن همه Fieldها یا Valueها

```bash
HKEYS event:1
HVALS event:1
```

<br>

---

<h2 id="set">🟢 Set</h2>

<div dir="rtl" align="right">

نوع داده Set مجموعه‌ای از Memberهای **Unique** است و ترتیب خاصی را تضمین نمی‌کند.

یکی از مهم‌ترین مزیت‌های آن، جلوگیری از مقدار تکراری است.

</div>

<br>

### درج داده جدید

```bash
SADD event:1:attendees user:1
SADD event:1:attendees user:2
SADD event:1:attendees user:1
```

عضو `user:1` فقط یک بار نگهداری می‌شود.

<br>

### بررسی وجود یک عضو در مجموعه

```bash
SISMEMBER event:1:attendees user:1
```

خروجی:

```text
1
```

<br>

### نمایش همه اعضای مجموعه

```bash
SMEMBERS event:1:attendees
```

<br>

### تعداد کل اعضا

تعداد اعضا:

```bash
SCARD event:1:attendees
```

<br>

### حذف عضو

```bash
SREM event:1:attendees user:2
```

<br>

### اشتراک دو مجموعه

```bash
SINTER first second
```

### اجتماع دو مجموعه

```bash
SUNION first second
```

### اختلاف دو مجموعه

```bash
SDIFF first second
```

<br>

---

<h2 id="sorted-set">🏆 Sorted Set</h2>

<div dir="rtl" align="right">

نوع داده Sorted Set شبیه Set است، با این تفاوت که هر Member یک **Score** نیز دارد و Memberها بر اساس Score مرتب می‌شوند.

این Data Type برای:

</div>
<div dir="rtl" align="left">

- Leaderboard
- Ranking
- Trending
- Priority
- امتیازدهی

بسیار مناسب است.

</div>

<br>

### درج داده جدید

```bash
ZADD events:trending 10 event:1
ZADD events:trending 20 event:2
ZADD events:trending 15 event:3
```

<br>

### نمایش اعضا (صعودی)

نمایش اعضای یک مجموعه همراه با مقدار `score` و بر اساس مقدار `score` از کم به زیاد:

```bash
ZRANGE events:trending 0 -1 WITHSCORES
```

<br>

### نمایش اعضا (نزولی)

```bash
ZREVRANGE events:trending 0 -1 WITHSCORES
```

<br>

### افزایش Score

```bash
ZINCRBY events:trending 5 event:1
```

<br>

### گرفتن Score

```bash
ZSCORE events:trending event:1
```

<br>

### نمایش رتبه اعضا

```bash
ZRANK events:trending event:1
ZREVRANK events:trending event:1
```

<br>

---

<h2 id="geo">📍 Geo</h2>

<div dir="rtl" align="right">

قابلیت Geospatial در Redis برای نگهداری Memberها همراه با مختصات Longitude و Latitude و جستجوی مکانی استفاده می‌شود.

این پروژه از Geo برای پیدا کردن Eventهای نزدیک به موقعیت کاربر استفاده می‌کند.

</div>

<br>

### GEOADD

فرمت:

```text
GEOADD key longitude latitude member
```

مثال:

```bash
GEOADD events:geo 51.3890 35.6892 event:1
```

> **📌 نکته:** ترتیب مختصات در Redis برابر **longitude سپس latitude** است، نه برعکس.

<br>

### درج مختصات چند Event

```bash
GEOADD events:geo \
    51.3890 35.6892 event:1 \
    51.4000 35.7000 event:2 \
    51.4100 35.7200 event:3
```

<br>

### جستجو

جستجوی Eventهای داخل شعاع مشخص:

```bash
GEOSEARCH events:geo \
    FROMLONLAT 51.4050 35.7550 \
    BYRADIUS 7 km
```

<br>

### مرتب‌سازی بر اساس فاصله

```bash
GEOSEARCH events:geo \
    FROMLONLAT 51.4050 35.7550 \
    BYRADIUS 7 km \
    ASC
```

<br>

### محدود کردن تعداد نتایج

```bash
GEOSEARCH events:geo \
    FROMLONLAT 51.4050 35.7550 \
    BYRADIUS 7 km \
    ASC \
    COUNT 10
```

<br>

### برگرداندن فاصله در نتیجه جستجو

```bash
GEOSEARCH events:geo \
    FROMLONLAT 51.4050 35.7550 \
    BYRADIUS 7 km \
    ASC \
    WITHDIST
```

<br>

### برگرداندن مختصات در نتیجه جستجو

```bash
GEOSEARCH events:geo \
    FROMLONLAT 51.4050 35.7550 \
    BYRADIUS 7 km \
    ASC \
    WITHCOORD
```

<br>

### محاسبه فاصله

فاصله‌ی بین دو عضو:

```bash
GEODIST events:geo event:1 event:2 km
```

<br>

### نمایش Hash اعضا

```bash
GEOHASH events:geo event:1
```

<br>

### مدل ذهنی Geo در پروژه

```text
events:geo
     │
     ├── event:1 -> (lon, lat)
     ├── event:2 -> (lon, lat)
     └── event:3 -> (lon, lat)

event:1
     ├── title
     ├── owner
     └── capacity
```

Geo فقط مکان را نگه می‌دارد و جزئیات Event در Hash قرار دارد.

<br>

---

<h2 id="pubsub">📡 Pub/Sub</h2>

<div dir="rtl" align="right">

در این الگو Publisher پیام را روی یک Channel ارسال می‌کند و Subscriberهایی که روی آن Channel Subscribe کرده‌اند پیام را دریافت می‌کنند.

</div>

<br>

<div dir="rtl" align="right">

### Subscriber

</div>

در Terminal اول:

```bash
docker exec -it redis redis-cli
```

سپس:

```bash
SUBSCRIBE chat:event:1
```

ترمینال منتظر پیام می‌ماند.

<br>

<div dir="rtl" align="right">

### Publisher

</div>

در Terminal دوم:

```bash
docker exec -it redis redis-cli
```

سپس:

```bash
PUBLISH chat:event:1 "Hello from Redis"
```

و Subscriber پیام را دریافت می‌کند.

<br>

### نقش Channel

کانال (Channel) یک Key معمولی Redis نیست. در اینجا نام کانال را مشخص می‌کند.

```text
chat:event:1
```

<br>


> **⚠️ نکته معماری:** Pub/Sub برای Live Delivery مناسب است، اما اگر نیاز به Durability، Replay، Consumer Group و پردازش قابل‌اعتماد دارید باید Data Structure یا Messaging System مناسب‌تری انتخاب شود.

<br>

---

<h2 id="blocking-queue">⏳ Blocking Queue</h2>

<div dir="rtl" align="right">

نوع داده List می‌تواند با دستورهای Blocking برای ساخت Queue ساده استفاده شود.

دستورهای مهم:

</div>
<div dir="rtl" align="left">

```text
BLPOP
BRPOP
```

این دستورات تا زمانی که داده‌ای برای برداشتن وجود نداشته باشد می‌توانند Client را Block کنند و منتظر باشند تا داده جدید وارد لیست شود.

</div>

<br>

<div dir="rtl" align="right">

### Producer

</div>

وارد کردن داده در صف توسط Producer:

```bash
RPUSH jobs "job-1"
RPUSH jobs "job-2"
```

<br>

<div dir="rtl" align="right">

### Consumer

</div>

و در صورتی که consumer در ترمینال دیگری این دستور را وارد کند داده‌ها به ترتیب دریافت می‌شوند:

```bash
BLPOP jobs 0
```
> **⚠️ نکته:** پارامتر 0 یعنی بدون Timeout و تا زمان رسیدن داده منتظر بمان.

<br>

> **⚠️ نکته مهم درباره Reliability:** وقتی `BLPOP` یک Job را برمی‌گرداند، آن Job از List حذف شده است. اگر Consumer بلافاصله Crash کند، ممکن است Job دیگر در Queue نباشد. برای Queueهای قابل‌اعتماد، باید الگوی مناسب‌تری مانند انتقال به Processing List، Streams یا Message Broker را بررسی کنید.

<br>

---

<h2 id="transaction">🔒 Transaction</h2>

<div dir="rtl" align="right">

در Redis، Transaction معمولاً با:

</div>
<div dir="rtl" align="right">

```text
MULTI
EXEC
DISCARD
WATCH
```

شناخته می‌شود.

هدف Transaction این است که چند Command در یک اجرای اتمیک Redis در کنار هم اجرا شوند.

</div>

دستور `MULTI`: به Redis می‌گویید «از این به بعد، دستورات بعدی را اجرا نکن، فقط آن‌ها را در یک صف (Queue) ذخیره کن.»

دستور `EXEC`: به Redis می‌گویید «حالا تمام دستوراتی که در صف ذخیره کردی را به صورت پشت سر هم و اتمیک (Atomic) اجرا کن.»

دستور `DISCARD`: به Redis می‌گویید «تراکنش را فراموش کن و صف را خالی کن.»


<br>

### MULTI / EXEC

```bash
MULTI
SET transaction:test "hello"
INCR transaction:counter
EXEC
```

دستورهای بین `MULTI` و `EXEC` در یک Transaction جمع می‌شوند.

<br>

### DISCARD

برای لغو:

```bash
MULTI
SET a 1
SET b 2
DISCARD
```

<br>

### WATCH

> دیتابیس Redis از Rollback (بازگشت به عقب) پشتیبانی نمی‌کند! یعنی اگر در بین دستورات داخل یک تراکنش، یک خطای زمانی (مثل جمع کردن یک رشته با عدد) رخ دهد، Redis بقیه دستورات را ادامه می‌دهد و فقط آن دستور خاص خطا می‌دهد. پس تراکنش در Redis یعنی «همه دستورات پشت سر هم اجرا می‌شوند و توسط هیچ دستور دیگری از طرف کاربران دیگر قطع نمی‌شوند»، نه اینکه «همه یا هیچ (All or Nothing)» مانند بانک‌ها.


دستور `WATCH` برای Optimistic Locking استفاده می‌شود و به Redis می‌گوید **«کلیدهایی که `WATCH` شده‌اند را در طول اجرای `MULTI` تحت نظر بگیر و اگر کسی کلید را تغییر داد، تراکنش من را اجرا نکن و به من خطا بده.»**

<br>

### سناریوی Capacity

فرض کنید ظرفیت Event:

```text
capacity = 1
```

دو User همزمان می‌خواهند ثبت‌نام کنند.

بدون هماهنگی مناسب ممکن است هر دو User مقدار یکسانی را ببینند و هر دو فکر کنند ظرفیت وجود دارد.

الگوی پروژه:

```text
WATCH event:{id}
WATCH event:{id}:attendees

READ capacity

CHECK capacity
CHECK duplicate registration

MULTI

HINCRBY capacity -1
SADD attendee user
LPUSH chat history system message
LTRIM history 0 99

EXEC
```

<br>

### پیاده‌سازی اصلی پروژه

```python
with self.redis.pipeline() as pipe:
    while True:
        try:
            pipe.watch(event_id, attendees_key)

            capacity = pipe.hget(
                event_id,
                "capacity"
            )

            if capacity is None:
                return False

            if int(capacity) <= 0:
                return False

            if pipe.sismember(
                attendees_key,
                user_id
            ):
                return False

            pipe.multi()

            pipe.hincrby(
                event_id,
                "capacity",
                -1
            )

            pipe.sadd(
                attendees_key,
                user_id
            )

            pipe.lpush(
                f"chat:{event_id}:history",
                f"System: {user_id} joined the event!"
            )

            pipe.ltrim(
                f"chat:{event_id}:history",
                0,
                99
            )

            pipe.execute()
            return True

        except redis.WatchError:
            continue
```

<br>

### چرا Retry داریم؟

در صورت بروز خطا و رسیدن به این خط:

```python
redis.WatchError
```

یعنی داده‌ای که تحت WATCH بوده قبل از `EXEC` تغییر کرده است. سپس این کد دوباره وضعیت را می‌خواند و تصمیم را از نو می‌گیرد:

```python
except redis.WatchError:
    continue
```

<br>

### نکته مهم درباره Atomicity

داخل پروژه سه تغییر منطقی باید با هم انجام شوند:

```text
1. کاهش ظرفیت
2. اضافه شدن User
3. ثبت پیام System
```

اگر این عملیات جدا از هم انجام شوند، امکان مشاهده‌ی State ناقص وجود دارد.

استفاده از Transaction کمک می‌کند این تغییرات به صورت یک گروه اجرا شوند.

<br>

---

<h2 id="monitor-info">📊 MONITOR و INFO</h2>

<div dir="rtl" align="right">

این دو دستور در خود `main.py` برای Business Logic استفاده نشده‌اند، اما برای یادگیری و Debug کردن Redis بسیار مهم هستند.

</div>

<br>

### MONITOR

دستور `MONITOR` جریان Commandهایی که Redis دریافت می‌کند را به صورت زنده نمایش می‌دهد.

در یک Terminal:

```bash
docker exec -it redis redis-cli MONITOR
```

حالا در Terminal دیگری برنامه را اجرا یا Commandهای Redis را ارسال کنید.

برای مثال:

```bash
SET demo:key hello
GET demo:key
INCR demo:counter
```

در Terminal دارای MONITOR، Commandها را مشاهده خواهید کرد.

<br>

### کاربردهای MONITOR

- Debug
- مشاهده‌ی Requestها
- فهمیدن اینکه Application چه Commandهایی ارسال می‌کند
- یادگیری Redis در زمان توسعه

مناسب است.

> **⚠️ هشدار:** `MONITOR` می‌تواند حجم خروجی بسیار بالایی ایجاد کند و برای Production Monitoring معمولاً ابزار اصلی مناسبی نیست.

<br>

### دستور INFO

برای دریافت اطلاعات بخش‌های مختلف Redis استفاده می‌شود

```bash
INFO
```

<br>

### بخش‌های مهم

Server:

```bash
INFO server
```

Memory:

```bash
INFO memory
```

Clients:

```bash
INFO clients
```

Stats:

```bash
INFO stats
```

Keyspace:

```bash
INFO keyspace
```

Persistence:

```bash
INFO persistence
```

Replication:

```bash
INFO replication
```

<br>


### تفاوت INFO و MONITOR

| دستور | هدف |
|---|---|
| `INFO` | وضعیت و متریک‌های کلی Redis |
| `MONITOR` | مشاهده‌ی Commandهای ورودی به صورت Real-time |

<br>

---

<h2 id="implementation-notes">🧠 نکات مهم پیاده‌سازی</h2>

### 1. ترکیب چند Redis Data Type

قدرت این پروژه فقط در استفاده از یک Data Type نیست.

یک Event از چند ساختار استفاده می‌کند:

```text
Hash         -> Details
Geo          -> Location
Sorted Set   -> Trending
Set          -> Attendees
List         -> Chat History
Pub/Sub      -> Live Chat
```

این دقیقاً یکی از الگوهای قدرتمند Redis است:

> هر بخش از Domain را با Data Structure مناسب خودش مدل کنید.

<br>

### 2. استفاده از Geo برای Search و Hash برای Details

نوع داده Geo فقط برای پیدا کردن Memberهای نزدیک استفاده می‌شود.

<br>

### 3. استفاده از Set برای Idempotency در ثبت‌نام

این خط عضویت را ذخیره می‌کند:

```python
pipe.sadd(attendees_key, user_id)
```


و این خط بررسی می‌کند آیا User قبلاً ثبت‌نام کرده یا خیر:

```python
pipe.sismember(attendees_key, user_id)
```

از آنجا که Set عضو تکراری ندارد، برای این مدل داده مناسب است.

<br>

### 4. استفاده از WATCH برای Concurrency

صرفاً داشتن Transaction همیشه کافی نیست.

در این پروژه قبل از `MULTI/EXEC` باید شرط ظرفیت و ثبت‌نام بررسی شود.

دستور `WATCH` کمک می‌کند اگر State بین Read و Execute تغییر کرد، Client متوجه تغییر شود.

<br>

### 5. استفاده از Thread در Pub/Sub

در این پروژه Listener در یک Thread جدا اجرا می‌شود تا:

```text
Thread 1 -> Listen
Main Thread -> Input / Publish
```

همزمان کار کنند.

<br>

### 6. محدود کردن Chat History

این کد حافظه‌ی History را محدود می‌کند:

```python
LTRIM(
    f"{channel}:history",
    0,
    99
)
```

> اگر داده‌ی دائمی ذخیره می‌کنید، باید رشد Key را از ابتدا کنترل کنید.

<br>

### 7. استفاده از Fake Data

این تابع قبل از منوی اصلی اجرا می‌شود:

```python
seed_fake_events()
```

در نتیجه هر بار اجرای برنامه داده‌ی جدیدی ساخته می‌شود.

<br>

---

<h2 id="concept-summary">🧾 جمع‌بندی مفاهیم</h2>

| Redis Feature | دستورهای کلیدی | کاربرد |
|---|---|---|
| String | `SET`, `GET`, `INCR`, `DECR`, `MSET`, `MGET` | مقدار ساده، Counter، Cache |
| List | `LPUSH`, `RPUSH`, `LPOP`, `RPOP`, `LRANGE`, `LTRIM` | Queue، Stack، History |
| Hash | `HSET`, `HGET`, `HGETALL`, `HINCRBY`, `HDEL` | Object ساده |
| Set | `SADD`, `SISMEMBER`, `SMEMBERS`, `SCARD`, `SREM`, `SINTER` | Unique Members |
| Sorted Set | `ZADD`, `ZINCRBY`, `ZRANGE`, `ZREVRANGE`, `ZSCORE` | Ranking، Leaderboard |
| Geo | `GEOADD`, `GEOSEARCH`, `GEODIST`, `GEOHASH` | Location Search |
| Pub/Sub | `SUBSCRIBE`, `PUBLISH`, `UNSUBSCRIBE` | Real-time Messaging |
| Blocking Queue | `BLPOP`, `BRPOP`, `BLMOVE`, `BLMPOP` | Queue Consumer |
| Transaction | `MULTI`, `EXEC`, `DISCARD`, `WATCH` | Atomic Grouping / Optimistic Locking |
| Monitoring | `MONITOR`, `INFO` | Debug / Observability |

<br>

---

<h2 id="resources">🔗 منابع</h2>

<div dir="rtl" align="right">

برای یادگیری عمیق‌تر از مستندات رسمی Redis استفاده کنید.

</div>

- Redis Documentation: https://redis.io/docs/
- Redis Data Types: https://redis.io/docs/latest/develop/data-types/
- Redis Commands: https://redis.io/docs/latest/commands/
- Redis Lists: https://redis.io/docs/latest/develop/data-types/lists/
- Redis Sorted Sets: https://redis.io/docs/latest/develop/data-types/sorted-sets/
- Redis Geospatial: https://redis.io/docs/latest/develop/data-types/geospatial/
- Redis Python Client: https://redis.readthedocs.io/

<br>

---

<h2 id="author">👨‍💻 نویسنده</h2>

<div dir="rtl" align="right">

این پروژه توسط **Meysam** برای یادگیری و تمرین Redis توسعه داده شده است.

</div>

[@imeysam](https://github.com/imeysam)

<br>

<div align="center">

⭐ اگر این Workshop برای یادگیری Redis مفید بود، خوشحال می‌شوم Repository را Star کنید.

</div>
