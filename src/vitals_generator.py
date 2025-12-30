
import random

def generate_vitals():
    # Simulate patient vitals
    heart_rate = random.randint(60, 100)
    blood_pressure = (random.randint(110, 140), random.randint(70, 90))  # Systolic, Diastolic
    temperature = round(random.uniform(36.5, 37.5), 1)  # Celsius
    oxygen_saturation = random.randint(95, 100)

    return {
        "heart_rate": heart_rate,
        "blood_pressure": blood_pressure,
        "temperature": temperature,
        "oxygen_saturation": oxygen_saturation
    }

if __name__ == '__main__':
    print(generate_vitals())
