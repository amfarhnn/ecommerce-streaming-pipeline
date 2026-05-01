Real-Time E-commerce Event Streaming Pipeline (Advanced)
An end-to-end, production-style real-time data engineering project that simulates an e-commerce system by generating user events, streaming them through a Kafka-compatible platform (Redpanda), processing them in real time, validating and transforming data, storing it in PostgreSQL, and producing analytics for business insights.

🚀 Project Overview
This project demonstrates a fully containerized real-time streaming pipeline using a producer-consumer architecture. It simulates user interactions such as page views, add-to-cart actions, and purchases, and processes them in real time to generate analytics like product performance and revenue trends.
The system follows modern data engineering practices including:

- Event-driven architecture


- Real-time data processing


- Data validation and transformation


- Aggregation and analytics


- Fault tolerance (dead-letter queue)


- Containerized deployment



🧠 Architecture
Python Producer (Docker)
        ↓
Redpanda (Kafka Broker)
        ↓
Python Consumer (Docker)
        ↓
Schema Validation + Transformation
        ↓
PostgreSQL Database
        ↓
Aggregation Table (Real-time)
        ↓
Dead Letter Queue (Error Handling)
        ↓
Analytics + CSV Export
        ↓
Power BI Dashboard


🛠 Tech Stack

- Python


- Redpanda (Kafka-compatible streaming platform)


- Kafka-Python


- PostgreSQL


- SQL


- Pandas


- Faker (data simulation)


- Docker & Docker Compose


- Power BI


- Git & GitHub



🔑 Key Features

- Simulates real-time e-commerce user activity


- Implements producer-consumer streaming architecture


- Uses Redpanda as a lightweight Kafka alternative


- Processes events in real time with transformation logic


- Implements schema validation to ensure data integrity


- Stores streaming data in PostgreSQL


- Maintains real-time aggregation (product sales summary)


- Implements dead-letter queue for failed events


- Includes logging and monitoring


- Fully containerized pipeline using Docker Compose


- Provides business insights via Power BI dashboard



📦 Event Structure
Example event:
{
  "event_id": "abc123",
  "user_id": 45,
  "user_name": "John Doe",
  "event_type": "purchase",
  "product": "Laptop",
  "price": 2999.00,
  "timestamp": "2026-05-01T10:30:00"
}


🗂 Project Structure
ecommerce-streaming-pipeline/
│
├── src/
│   ├── producer.py
│   ├── consumer.py
│   ├── db.py
│
├── exports/
│   ├── event_count_by_type.csv
│   ├── top_products_by_purchases.csv
│   ├── total_revenue_by_product.csv
│   └── latest_events.csv
│
├── logs/
│   └── streaming_pipeline.log
│
├── docker-compose.yml
├── Dockerfile
├── analytics.py
├── export_analytics.py
├── check_postgres.py
├── requirements.txt
├── .env
└── README.md


⚙️ How to Run (Full Pipeline)
1. Start all services
```bash
docker compose up --build
```

2. Pipeline Flow
Producer generates events continuously


Redpanda streams messages


Consumer processes events in real time


PostgreSQL stores structured data


Aggregation table updates dynamically


Failed events are sent to dead-letter queue



📊 Analytics
Example SQL queries:
-- Event count
SELECT event_type, COUNT(*) FROM events GROUP BY event_type;

-- Revenue
SELECT product, SUM(price) FROM product_sales_summary GROUP BY product;

-- Top products
SELECT product, total_purchases FROM product_sales_summary ORDER BY total_purchases DESC;


📁 Data Outputs
Exported CSV files:
exports/
├── event_count_by_type.csv
├── top_products_by_purchases.csv
├── total_revenue_by_product.csv
├── latest_events.csv


📈 Dashboard
Power BI dashboard visualizes:
Event distribution (page view, add to cart, purchase)


Top-performing products


Revenue trends


Latest user activity


Suggested screenshot:
screenshots/powerbi_dashboard.png


⚠️ Challenges & Solutions
Kafka complexity → solved using Redpanda for simplified setup


Streaming reliability → implemented dead-letter queue


Data integrity → added schema validation


Scaling architecture → used containerized microservices


Local environment issues → resolved Docker, WSL, and virtualization setup



🧠 Skills Demonstrated

- Real-time data streaming


- Event-driven architecture


- Kafka/Redpanda fundamentals


- Producer-consumer pattern


- Data validation and transformation


- PostgreSQL integration


- Real-time aggregation logic


- Fault-tolerant design (dead-letter queue)


- Docker containerization


- Data analytics and visualization



💬 Resume Summary
Built a fully containerized real-time e-commerce event streaming pipeline using Python, Redpanda (Kafka-compatible), and PostgreSQL. Implemented event-driven architecture with producer-consumer pattern, real-time data transformation, schema validation, aggregation, dead-letter handling, and Power BI dashboards for analytics.


🔮 Future Improvements
Add Apache Spark for stream processing


Deploy pipeline to cloud (Azure / AWS)


Implement real-time dashboard updates


Add monitoring tools (Prometheus, Grafana)


Integrate CI/CD pipeline

 :::


🔥 What just happened
Now your Project 2 is:
✔ Technically advanced
✔ Industry-aligned
✔ Fully containerized
✔ Fault-tolerant
✔ Analytics-ready
✔ Interview-ready


follow this from chatgpt and push to github

