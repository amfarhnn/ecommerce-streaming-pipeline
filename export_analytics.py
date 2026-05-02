import sqlite3
from pathlib import Path
import pandas as pd


EXPORT_DIR = Path("exports")
EXPORT_DIR.mkdir(exist_ok=True)

conn = sqlite3.connect("ecommerce_events.db")

exports = {
    "event_count_by_type.csv": """
        SELECT event_type, COUNT(*) AS total_events
        FROM events
        GROUP BY event_type
        ORDER BY total_events DESC;
    """,

    "top_products_by_purchases.csv": """
        SELECT product, COUNT(*) AS total_purchases
        FROM events
        WHERE event_type = 'purchase'
        GROUP BY product
        ORDER BY total_purchases DESC;
    """,

    "total_revenue_by_product.csv": """
        SELECT product, ROUND(SUM(price), 2) AS total_revenue
        FROM events
        WHERE event_type = 'purchase'
        GROUP BY product
        ORDER BY total_revenue DESC;
    """,

    "latest_events.csv": """
        SELECT *
        FROM events
        ORDER BY timestamp DESC
        LIMIT 100;
    """
}

for filename, query in exports.items():
    df = pd.read_sql_query(query, conn)
    output_path = EXPORT_DIR / filename
    df.to_csv(output_path, index=False)
    print(f"Exported: {output_path}")

conn.close()
