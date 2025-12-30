
def publish_data(vitals, risk_score):
    # Publish the data (for now, just print to console)
    print("Vitals:", vitals)
    print("Risk Score:", risk_score)

if __name__ == '__main__':
    # Example usage
    vitals = {
        "heart_rate": 75,
        "blood_pressure": (120, 80),
        "temperature": 37.0,
        "oxygen_saturation": 98
    }
    risk_score = 1
    publish_data(vitals, risk_score)
