import json
import logging
from pathlib import Path

from kafka import KafkaConsumer, KafkaProducer

from db import (
    create_events_table,
    insert_event,
    update_product_sales_summary
)


log_dir = Path("logs")
log_dir.mkdir(exist_ok=True)

logging.basicConfig(
    filename=log_dir / "streaming_pipeline.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


consumer = KafkaConsumer(
    "ecommerce-events",
    bootstrap_servers="redpanda:9092",
    auto_offset_reset="earliest",
    enable_auto_commit=True,
    group_id="ecommerce-consumer-group",
    value_deserializer=lambda m: json.loads(m.decode("utf-8")),
)


producer = KafkaProducer(
    bootstrap_servers="redpanda:9092",
    value_serializer=lambda v: json.dumps(v).encode("utf-8"),
)


def validate_event(event):
    required_fields = [
        "event_id", "user_id", "event_type",
        "product", "price", "timestamp"
    ]

    for field in required_fields:
        if field not in event:
            return False

    return True


def transform_event(event):
    event["high_value"] = 1 if event.get("price", 0) >= 1000 else 0
    return event


if __name__ == "__main__":
    create_events_table()

    print("Starting upgraded e-commerce event consumer...")
    logging.info("Consumer started")

    count = 0

    for message in consumer:
        try:
            event = message.value

            if not validate_event(event):
                logging.error("Invalid event schema")
                producer.send("dead-letter-events", event)
                continue

            transformed_event = transform_event(event)

            insert_event(transformed_event)
            update_product_sales_summary(transformed_event)

            count += 1
            if count % 10 == 0:
                print(f"Processed {count} events")

            logging.info(
                f"Processed event_id={transformed_event['event_id']}, "
                f"type={transformed_event['event_type']}, "
                f"product={transformed_event['product']}"
            )

            print(
                f"Processed event: {transformed_event['event_id']} | "
                f"{transformed_event['event_type']} | "
                f"High Value: {transformed_event['high_value']}"
            )

        except Exception as e:
            logging.error(f"Failed event: {event}")
            try:
                producer.send("dead-letter-events", event)
            except Exception:
                logging.error("Failed to send to dead-letter-events")
            print(f"Error processing event: {e}")
