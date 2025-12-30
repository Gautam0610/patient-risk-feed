from kafka import KafkaProducer
import json

KAFKA_TOPIC = 'patient_vitals'
KAFKA_BOOTSTRAP_SERVERS = ['localhost:9092']  # Change if your Kafka broker is running elsewhere

def publish_data(vitals, risk_score, rolling_averages):
    # Publish the data to Kafka
    try:
        producer = KafkaProducer(
            bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS,
            value_serializer=lambda v: json.dumps(v).encode('utf-8')
        )

        message = {
            "vitals": vitals,
            "risk_score": risk_score,
            "rolling_averages": rolling_averages
        }

        producer.send(KAFKA_TOPIC, message)
        producer.flush()  # Ensure message is sent
        print(f"Message published to Kafka topic {KAFKA_TOPIC}")

    except Exception as e:
        print(f"Error publishing to Kafka: {e}")

if __name__ == '__main__':
    # Example usage
    vitals = {
        "heart_rate": 75,
        "blood_pressure": (120, 80),
        "temperature": 37.0,
        "oxygen_saturation": 98
    }
    risk_score = 1
    rolling_averages = [
        {"heart_rate": 72.5, "blood_pressure": (122.5, 81.0), "temperature": 37.1, "oxygen_saturation": 98.5}
    ]
    publish_data(vitals, risk_score, rolling_averages)
