import json
import logging
import os
from pathlib import Path

from kafka import KafkaConsumer
from dotenv import load_dotenv

from db_postgres import (
    create_events_table,
    insert_event,
    update_product_sales_summary
)

load_dotenv()

log_dir = Path("logs")
log_dir.mkdir(exist_ok=True)

logging.basicConfig(
    filename=log_dir / "streaming_pipeline.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

consumer = KafkaConsumer(
    "ecommerce-events",
    bootstrap_servers=os.getenv("KAFKA_BROKER"),
    auto_offset_reset="earliest",
    enable_auto_commit=True,
    group_id="ecommerce-consumer-group",
    value_deserializer=lambda m: json.loads(m.decode("utf-8")),
)


def transform_event(event):
    event["high_value"] = 1 if event["price"] >= 1000 else 0
    return event


def process_event(event):
    retries = 3

    for attempt in range(retries):
        try:
            inserted = insert_event(event)
            if inserted:
                update_product_sales_summary(event)
            return True
        except Exception as e:
            logging.error(f"Retry {attempt + 1}/{retries} failed: {e}")

    return False


if __name__ == "__main__":
    create_events_table()

    print("Starting upgraded e-commerce event consumer...")
    logging.info("Consumer started")

    for message in consumer:
        try:
            event = message.value

            transformed_event = transform_event(event)

            success = process_event(transformed_event)

            if success:
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
            else:
                logging.error(f"Failed permanently: {transformed_event['event_id']}")
                print(f"Failed to process event after retries: {transformed_event['event_id']}")

        except Exception as e:
            logging.error(f"Error processing message: {e}")
            print(f"Error processing message: {e}")
