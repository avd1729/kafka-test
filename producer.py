from confluent_kafka import Producer
import time

# Callback for producer delivery reports
def delivery_report(err, msg):
    if err is not None:
        print(f"Message delivery failed: {err}")
    else:
        print(f"Message delivered to {msg.topic()} [{msg.partition()}] at offset {msg.offset()}")

def produce_messages():
    # Kafka configuration
    producer_conf = {
        'bootstrap.servers': 'localhost:9092',  # Kafka broker address
    }

    # Create a Kafka producer
    producer = Producer(producer_conf)

    topic = "test-topic"

    # Produce messages
    for i in range(5):
        key = f"key-{i}"
        value = f"message-{i}"
        producer.produce(topic, key=key, value=value, callback=delivery_report)
        producer.flush()  # Ensure messages are sent before the script exits
        time.sleep(1)

    print("Finished producing messages.")

if __name__ == "__main__":
    produce_messages()
