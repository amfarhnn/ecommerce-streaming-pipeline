import json
import os
import random
import time
from datetime import datetime
from uuid import uuid4

from faker import Faker
from kafka import KafkaProducer
from dotenv import load_dotenv

load_dotenv()

fake = Faker()

PRODUCTS = [
    "Laptop",
    "Smartphone",
    "Headphones",
    "Keyboard",
    "Mouse",
    "Monitor",
    "Tablet",
    "Smartwatch",
]

EVENT_TYPES = ["page_view", "add_to_cart", "purchase"]


producer = KafkaProducer(
    bootstrap_servers=os.getenv("KAFKA_BROKER"),
    value_serializer=lambda v: json.dumps(v).encode("utf-8"),
)


def generate_event():
    event_type = random.choice(EVENT_TYPES)

    return {
        "event_id": str(uuid4()),
        "user_id": random.randint(1, 100),
        "user_name": fake.name(),
        "event_type": event_type,
        "product": random.choice(PRODUCTS),
        "price": round(random.uniform(20, 3000), 2),
        "timestamp": datetime.now().isoformat(),
    }


if __name__ == "__main__":
    print("Starting e-commerce event producer...")

    while True:
        event = generate_event()

        producer.send("ecommerce-events", event)
        producer.flush()

        print(f"Sent event: {event}")

        time.sleep(2)
