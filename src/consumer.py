import json
from kafka import KafkaConsumer

from db import create_events_table, insert_event


consumer = KafkaConsumer(
    "ecommerce-events",
    bootstrap_servers="localhost:9092",
    auto_offset_reset="earliest",
    enable_auto_commit=True,
    group_id="ecommerce-consumer-group",
    value_deserializer=lambda m: json.loads(m.decode("utf-8")),
)


if __name__ == "__main__":
    create_events_table()

    print("Starting e-commerce event consumer...")

    for message in consumer:
        event = message.value
        insert_event(event)
        print(f"Saved event to database: {event['event_id']}")
