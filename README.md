# Real-Time E-commerce Event Streaming Pipeline

An end-to-end real-time data engineering project that simulates an e-commerce platform by generating user events, streaming them through a Kafka-compatible system (Redpanda), processing them in real time, storing them in PostgreSQL, and producing analytics for business insights.

## 🚀 Project Overview

This project demonstrates a real-time streaming pipeline using producer-consumer architecture.

It simulates user activity such as page views, add-to-cart actions, and purchases, and transforms raw event streams into analytics-ready insights.

## 🧠 Architecture

```
Python Producer
      ↓
Redpanda (Kafka Broker)
      ↓
Python Consumer
      ↓
Real-Time Processing (Filter + Transform)
      ↓
PostgreSQL Database
      ↓
Aggregation Table
      ↓
Analytics → Power BI Dashboard
```

## 🛠️ Tech Stack

- Python
- Redpanda (Kafka-compatible streaming platform)
- Kafka-Python
- Faker (data simulation)
- PostgreSQL
- SQL
- Pandas
- Docker & Docker Compose
- python-dotenv (.env configuration)
- Power BI
- Git & GitHub

## 🔥 Key Features

- Real-time event streaming using producer-consumer pattern
- Kafka-compatible message broker (Redpanda)
- Event-driven architecture
- Data transformation and filtering in streaming consumer
- High-value transaction detection
- Real-time aggregation (revenue & purchases)
- PostgreSQL integration for production-level storage
- Environment-based configuration using .env
- Full containerization using Docker Compose
- Dashboard visualization with Power BI

## 📦 Event Structure

Example event:

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

## 🗂️ Project Structure

```
ecommerce-streaming-pipeline/
│
├── src/
│   ├── producer.py
│   ├── consumer.py
│   ├── db_postgres.py
│
├── exports/
│   ├── event_count_by_type.csv
│   ├── top_products_by_purchases.csv
│   ├── total_revenue_by_product.csv
│   └── latest_events.csv
│
├── docker-compose.yml
├── Dockerfile
├── .env
├── .gitignore
├── analytics.py
├── export_analytics.py
├── requirements.txt
└── README.md
```

## 🔐 Environment Configuration (.env)

```
POSTGRES_HOST=postgres
POSTGRES_DB=ecommerce_db
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_PORT=5432

KAFKA_BROKER=redpanda:9092
```

## ▶️ How to Run (Docker)

```bash
docker compose up --build
```

## 🧪 Local Development

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run Producer

```bash
python src/producer.py
```

### Run Consumer

```bash
python src/consumer.py
```

## 📊 Analytics

Run SQL-based analytics:

```bash
python analytics.py
```

## 📁 Export Data

```bash
python export_analytics.py
```

## 📈 Dashboard

Power BI dashboard includes:

- Event distribution by type
- Top-selling products
- Revenue by product
- Latest events table

## ⚙️ Real-Time Processing Logic

- Filters and processes events in real time
- Adds high_value flag for expensive transactions
- Updates aggregation table continuously

## 🧱 Database Design

### events table

- Stores all streaming events
- Includes transformation fields (e.g. high_value)

### product_sales_summary table

- Stores aggregated results
- Updates in real time

## 🧠 Challenges & Solutions

| Challenge | Solution |
|-----------|----------|
| Kafka setup complexity | Solved using Redpanda |
| Docker networking issues | Solved using service names (redpanda, postgres) |
| Data consistency | Handled with INSERT conflict strategies |
| Fault tolerance | Implemented retry logic |
| Configuration security | Migrated to .env variables |

## 💡 Skills Demonstrated

- Real-time data streaming
- Kafka/Redpanda fundamentals
- Producer-consumer architecture
- Event-driven system design
- Data ingestion and transformation
- PostgreSQL database integration
- SQL analytics and aggregation
- Docker containerization
- Environment configuration (.env)
- Dashboard reporting

## 📄 Resume Summary

Built a real-time streaming data pipeline using Python, Redpanda (Kafka-compatible), and PostgreSQL. Implemented producer-consumer architecture for event ingestion, real-time transformation and aggregation, secure configuration using environment variables, and analytics visualization using Power BI.

## 🔮 Future Improvements

- Integrate Apache Spark Streaming
- Add real-time dashboard updates
- Deploy pipeline to Azure Container Apps
- Implement monitoring (Datadog / Prometheus)
- Add CI/CD using GitHub Actions

---

✅ **Technically Strong**  
✅ **Production-Style**  
✅ **Secure (.env)**  
✅ **Scalable (consumer group)**  
✅ **Recruiter-Ready**
