from confluent_kafka import Consumer, KafkaException, KafkaError

def consume_messages():
    # Kafka consumer configuration
    conf = {
        'bootstrap.servers': 'localhost:9092',  # Update with your Kafka broker address
        'group.id': 'test-group',
        'auto.offset.reset': 'earliest',
    }

    consumer = Consumer(conf)
    topic = 'test-topic'

    try:
        consumer.subscribe([topic])
        print("Listening for messages...")

        while True:
            msg = consumer.poll(timeout=1.0)  # Poll for a message
            if msg is None:
                continue  # No message received
            if msg.error():
                if msg.error().code() == KafkaError._PARTITION_EOF:
                    # End of partition event
                    print(f"End of partition reached {msg.topic()} [{msg.partition()}]")
                elif msg.error():
                    raise KafkaException(msg.error())
            else:
                # Safely handle None values for key and value
                key = msg.key().decode('utf-8') if msg.key() is not None else None
                value = msg.value().decode('utf-8') if msg.value() is not None else None
                print(f"Received message: Key={key}, Value={value}, "
                      f"Partition={msg.partition()}, Offset={msg.offset()}")

    except KeyboardInterrupt:
        print("Consumer interrupted")
    finally:
        consumer.close()  # Close the consumer

if __name__ == '__main__':
    consume_messages()
