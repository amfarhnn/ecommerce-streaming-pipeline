from src.db_postgres import query_dataframe

queries = {
    "Event count by type": """
        SELECT event_type, COUNT(*) AS total_events
        FROM events
        GROUP BY event_type
        ORDER BY total_events DESC;
    """,

    "Top products by purchases": """
        SELECT product, COUNT(*) AS total_purchases
        FROM events
        WHERE event_type = 'purchase'
        GROUP BY product
        ORDER BY total_purchases DESC;
    """,

    "Total revenue by product": """
        SELECT product, ROUND(SUM(price), 2) AS total_revenue
        FROM events
        WHERE event_type = 'purchase'
        GROUP BY product
        ORDER BY total_revenue DESC;
    """,

    "Latest 10 events": """
        SELECT *
        FROM events
        ORDER BY timestamp DESC
        LIMIT 10;
    """
}

for title, query in queries.items():
    print(f"\n=== {title} ===")
    df = query_dataframe(query)
    print(df)
