
def calculate_risk_score(vitals):
    # Basic risk calculation based on vitals
    heart_rate = vitals["heart_rate"]
    blood_pressure = vitals["blood_pressure"]
    temperature = vitals["temperature"]
    oxygen_saturation = vitals["oxygen_saturation"]

    risk_score = 0

    if heart_rate < 60 or heart_rate > 100:
        risk_score += 1
    if blood_pressure[0] < 110 or blood_pressure[0] > 140 or blood_pressure[1] < 70 or blood_pressure[1] > 90:
        risk_score += 1
    if temperature < 36.5 or temperature > 37.5:
        risk_score += 1
    if oxygen_saturation < 95:
        risk_score += 1

    return risk_score

if __name__ == '__main__':
    # Example usage
    vitals = {
        "heart_rate": 75,
        "blood_pressure": (120, 80),
        "temperature": 37.0,
        "oxygen_saturation": 98
    }
    risk_score = calculate_risk_score(vitals)
    print(f"Risk Score: {risk_score}")
