import sqlite3
import pandas as pd


conn = sqlite3.connect("ecommerce_events.db")

df = pd.read_sql_query(
    "SELECT * FROM events LIMIT 10",
    conn
)

print(df)

conn.close()
