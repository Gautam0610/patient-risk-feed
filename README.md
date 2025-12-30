# Patient Risk Feed

This project generates simulated patient vitals, calculates a basic risk score, calculates rolling average vitals, and publishes the data to a Kafka topic.

## Prerequisites

*   Docker
*   Docker Compose (optional, for Kafka setup)
*   Kafka (running locally or accessible via network)

## Setup

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/Gautam0610/patient-risk-feed.git
    cd patient-risk-feed
    ```

2.  **Start Kafka (using Docker Compose - optional):**

    Create a `docker-compose.yml` file (if you don't have one already) with the following content:

    ```yaml
    version: '3.7'
    services:
      zookeeper:
        image: confluentinc/cp-zookeeper:latest
        environment:
          ZOOKEEPER_CLIENT_PORT: 2181
          ZOOKEEPER_TICK_TIME: 2000
      kafka:
        image: confluentinc/cp-kafka:latest
        depends_on: [zookeeper]
        ports:
          - 9092:9092
        environment:
          KAFKA_BROKER_ID: 1
          KAFKA_ZOOKEEPER_CONNECT: zookeeper:2181
          KAFKA_ADVERTISED_LISTENERS: PLAINTEXT://localhost:9092
          KAFKA_OFFSETS_TOPIC_REPLICATION_FACTOR: 1
    ```

    Then, start Kafka using Docker Compose:

    ```bash
    docker-compose up -d
    ```

3.  **Build the Docker image:**

    ```bash
    docker build -t patient-risk-feed .
    ```

4.  **Run the Docker container:**

    ```bash
    docker run patient-risk-feed
    ```

## Project Structure

```
patient-risk-feed/
├── src/
│   ├── vitals_generator.py
│   ├── risk_calculator.py
│   ├── publisher.py
│   ├── rolling_average.py
│   └── main.py
├── Dockerfile
├── requirements.txt
└── README.md
```

## Modules

*   `vitals_generator.py`: Generates simulated patient vitals.
*   `risk_calculator.py`: Calculates basic risk scores based on vitals.
*   `publisher.py`: Publishes the data to a Kafka topic.
*   `rolling_average.py`: Calculates rolling average vitals.
*   `main.py`: Orchestrates the process.
