# Real-Time E-commerce Event Streaming Pipeline

An end-to-end real-time data engineering project that simulates an e-commerce platform by generating user events, streaming them through a Kafka-compatible system (Redpanda), processing them in real time, storing them in a database, and producing analytics for business insights.

---

## Project Overview

This project demonstrates a real-time streaming pipeline where user interactions such as page views, add-to-cart actions, and purchases are continuously generated and processed.

The system simulates how modern e-commerce platforms track user behavior and convert raw event streams into actionable insights.

---

## Architecture

```
Python Event Producer
        ↓
Redpanda (Kafka Broker)
        ↓
Python Consumer
        ↓
SQLite Database
        ↓
SQL Analytics
        ↓
CSV Exports
        ↓
Power BI Dashboard
```

---

## Tech Stack

- Python
- Redpanda (Kafka-compatible streaming platform)
- Kafka-Python
- Faker
- SQLite
- SQL
- Pandas
- Docker
- Power BI
- Git & GitHub

---

## Key Features

- Simulates real-time e-commerce user events
- Implements producer-consumer architecture
- Uses Redpanda as a lightweight Kafka alternative
- Processes streaming data continuously
- Stores events in a structured SQLite database
- Performs SQL-based analytics
- Exports processed data for reporting
- Visualizes insights using Power BI

---

## Event Structure

```json
{
  "event_id": "abc123",
  "user_id": 45,
  "user_name": "John Doe",
  "event_type": "purchase",
  "product": "Laptop",
  "price": 2999.00,
  "timestamp": "2026-04-30T10:30:00"
}
```

---

## Project Structure

```
ecommerce-streaming-pipeline/
│
├── src/
│   ├── producer.py
│   ├── consumer.py
│   └── db.py
│
├── exports/
│   ├── event_count_by_type.csv
│   ├── top_products_by_purchases.csv
│   ├── total_revenue_by_product.csv
│   └── latest_events.csv
│
├── docker-compose.yml
├── ecommerce_events.db
├── analytics.py
├── export_analytics.py
├── requirements.txt
└── README.md
```

---

## How to Run

1. **Start Redpanda (Kafka)**
   ```bash
   docker compose up -d
   ```

2. **Run Producer**
   ```bash
   python src/producer.py
   ```

3. **Run Consumer**
   ```bash
   python src/consumer.py
   ```

4. **Run Analytics**
   ```bash
   python analytics.py
   ```

5. **Export Data**
   ```bash
   python export_analytics.py
   ```

---

## Dashboard

The Power BI dashboard includes:

- **Event count by type** (page view, add to cart, purchase)
- **Top products by purchases**
- **Revenue analysis by product**
- **Latest events table**

Suggested screenshot path:
```
screenshots/powerbi_dashboard.png
```

---

## Challenges & Solutions

| Challenge | Solution |
|-----------|----------|
| Initial complexity in setting up Kafka-like streaming system | Used Redpanda to simplify local deployment via Docker |
| Implementing producer-consumer pattern for real-time data flow | Created separate producer and consumer modules |
| Ensuring data persistence | Used SQLite database for structured storage |

---

## Skills Demonstrated

- Real-time data streaming
- Event-driven architecture
- Kafka/Redpanda fundamentals
- Producer-consumer design pattern
- Data ingestion and processing
- SQL analytics and aggregation
- Data export and reporting
- Dashboard visualization
- Docker usage

---

## Resume Summary

Built a real-time e-commerce event streaming pipeline using Python and Redpanda (Kafka-compatible), implementing producer-consumer architecture for event ingestion, storing streaming data in SQLite, performing SQL analytics, and generating business insights through Power BI dashboards.

---

## Future Improvements

- Replace SQLite with PostgreSQL or cloud database
- Add stream processing with Apache Spark
- Implement real-time dashboard updates
- Deploy pipeline to cloud environment
- Add monitoring and alerting

---

✅ ATS & Recruiter Friendly  
✅ Production-Ready Documentation
