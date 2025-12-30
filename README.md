# Patient Risk Feed

This project generates simulated patient vitals, calculates a basic risk score, and publishes the data.

## Usage

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/Gautam0610/patient-risk-feed.git
    cd patient-risk-feed
    ```

2.  **Build the Docker image:**

    ```bash
    docker build -t patient-risk-feed .
    ```

3.  **Run the Docker container:**

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
│   └── main.py
├── Dockerfile
└── README.md
```

## Modules

*   `vitals_generator.py`: Generates simulated patient vitals.
*   `risk_calculator.py`: Calculates basic risk scores based on vitals.
*   `publisher.py`: Publishes the data (prints to console).
*   `main.py`: Orchestrates the process.
