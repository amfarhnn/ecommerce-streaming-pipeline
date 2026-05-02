import os

import pandas as pd
import psycopg2
from dotenv import load_dotenv


load_dotenv()

conn = psycopg2.connect(
    dbname=os.getenv("POSTGRES_DB"),
    user=os.getenv("POSTGRES_USER"),
    password=os.getenv("POSTGRES_PASSWORD"),
    host=os.getenv("POSTGRES_HOST"),
    port=os.getenv("POSTGRES_PORT"),
)

print("\n=== Latest Events ===")
events_df = pd.read_sql_query(
    "SELECT * FROM events ORDER BY timestamp DESC LIMIT 10;",
    conn
)
print(events_df)

print("\n=== Product Sales Summary ===")
summary_df = pd.read_sql_query(
    "SELECT * FROM product_sales_summary ORDER BY total_revenue DESC;",
    conn
)
print(summary_df)

conn.close()
