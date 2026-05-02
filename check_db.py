import sqlite3
import pandas as pd


conn = sqlite3.connect("ecommerce_events.db")

print("\n=== Latest Events ===")
events_df = pd.read_sql_query(
    "SELECT * FROM events LIMIT 10",
    conn
)
print(events_df)

print("\n=== Product Sales Summary ===")
summary_df = pd.read_sql_query(
    "SELECT * FROM product_sales_summary",
    conn
)
print(summary_df)

conn.close()
