from src.db_postgres import query_dataframe

print("\n=== Latest Events ===")
events_df = query_dataframe(
    "SELECT * FROM events LIMIT 10",
)
print(events_df)

print("\n=== Product Sales Summary ===")
summary_df = query_dataframe(
    "SELECT * FROM product_sales_summary",
)
print(summary_df)
