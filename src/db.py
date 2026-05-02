import sqlite3
from pathlib import Path


DB_PATH = Path("ecommerce_events.db")


def create_connection():
    return sqlite3.connect(DB_PATH)


def create_events_table():
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS events (
            event_id TEXT PRIMARY KEY,
            user_id INTEGER,
            user_name TEXT,
            event_type TEXT,
            product TEXT,
            price REAL,
            timestamp TEXT
        )
    """)

    conn.commit()
    conn.close()


def insert_event(event):
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT OR IGNORE INTO events (
            event_id,
            user_id,
            user_name,
            event_type,
            product,
            price,
            timestamp
        )
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (
        event["event_id"],
        event["user_id"],
        event["user_name"],
        event["event_type"],
        event["product"],
        event["price"],
        event["timestamp"]
    ))

    conn.commit()
    conn.close()
