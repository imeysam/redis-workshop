# 🚀 Local Meetups & Live Chat (Redis Project)

A lightweight, educational CLI application built with Python and Redis to demonstrate advanced data structures and real-time capabilities.

## 🌟 Features
- **Geo-Spatial Search:** Find events near a specific location using `GEOSEARCH`.
- **Real-time Chat:** Live chat rooms for events using `Pub/Sub` and multi-threading.
- **Atomic Transactions:** Safe event registration using `WATCH` and `MULTI/EXEC` pipelines to prevent race conditions.
- **Trending Events:** Leaderboard system using `Sorted Sets`.
- **Data Structures:** Utilizes Hashes, Lists, Sets, Strings, and Geo.

## 🛠️ Prerequisites
- Python 3.8+
- Docker & Docker Compose

## 🏃 How to Run

1. **Clone the repository:**
   ```bash
   git clone https://github.com/YOUR_USERNAME/redis-meetup-project.git
   cd redis-meetup-project