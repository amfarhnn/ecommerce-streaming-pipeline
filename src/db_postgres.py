import os
from dotenv import load_dotenv
import psycopg2
from psycopg2.extras import RealDictCursor

load_dotenv()


def get_connection():
    return psycopg2.connect(
        host=os.getenv("POSTGRES_HOST"),
        database=os.getenv("POSTGRES_DB"),
        user=os.getenv("POSTGRES_USER"),
        password=os.getenv("POSTGRES_PASSWORD"),
        port=os.getenv("POSTGRES_PORT")
    )


def create_events_table():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS events (
            event_id TEXT PRIMARY KEY,
            user_id INTEGER,
            user_name TEXT,
            event_type TEXT,
            product TEXT,
            price REAL,
            timestamp TEXT,
            high_value INTEGER
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS product_sales_summary (
            product TEXT PRIMARY KEY,
            total_purchases INTEGER,
            total_revenue REAL
        )
    """)

    conn.commit()
    conn.close()


def insert_event(event):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO events (
            event_id,
            user_id,
            user_name,
            event_type,
            product,
            price,
            timestamp,
            high_value
        )
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        ON CONFLICT (event_id) DO NOTHING
    """, (
        event["event_id"],
        event["user_id"],
        event["user_name"],
        event["event_type"],
        event["product"],
        event["price"],
        event["timestamp"],
        event["high_value"]
    ))

    conn.commit()
    conn.close()


def update_product_sales_summary(event):
    if event["event_type"] != "purchase":
        return

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO product_sales_summary (
            product,
            total_purchases,
            total_revenue
        )
        VALUES (%s, 1, %s)
        ON CONFLICT (product) DO UPDATE SET
            total_purchases = product_sales_summary.total_purchases + 1,
            total_revenue = product_sales_summary.total_revenue + EXCLUDED.total_revenue
    """, (
        event["product"],
        event["price"]
    ))

    conn.commit()
    conn.close()
