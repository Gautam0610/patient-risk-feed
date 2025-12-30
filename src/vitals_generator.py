import random
import time

def generate_vitals_series(num_vitals=10):
    # Simulate a series of patient vitals over time
    vitals_series = []
    for _ in range(num_vitals):
        heart_rate = random.randint(60, 100)
        blood_pressure = (random.randint(110, 140), random.randint(70, 90))
        temperature = round(random.uniform(36.5, 37.5), 1)
        oxygen_saturation = random.randint(95, 100)

        vitals = {
            "heart_rate": heart_rate,
            "blood_pressure": blood_pressure,
            "temperature": temperature,
            "oxygen_saturation": oxygen_saturation
        }
        vitals_series.append(vitals)
        time.sleep(1)  # Simulate time passing between readings
    return vitals_series

if __name__ == '__main__':
    vitals_data = generate_vitals_series()
    print(vitals_data)
