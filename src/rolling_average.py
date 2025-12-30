def calculate_rolling_average(vitals_series, window_size=3):
    # Calculate the rolling average of vitals
    if len(vitals_series) < window_size:
        return None  # Not enough data to calculate rolling average

    rolling_averages = []
    for i in range(window_size - 1, len(vitals_series)):
        window = vitals_series[i - window_size + 1:i + 1]
        heart_rates = [v["heart_rate"] for v in window]
        blood_pressures = [v["blood_pressure"] for v in window]
        temperatures = [v["temperature"] for v in window]
        oxygen_saturations = [v["oxygen_saturation"] for v in window]

        avg_heart_rate = sum(heart_rates) / window_size
        avg_systolic_bp = sum([bp[0] for bp in blood_pressures]) / window_size
        avg_diastolic_bp = sum([bp[1] for bp in blood_pressures]) / window_size
        avg_temperature = sum(temperatures) / window_size
        avg_oxygen_saturation = sum(oxygen_saturations) / window_size

        rolling_averages.append({
            "heart_rate": avg_heart_rate,
            "blood_pressure": (avg_systolic_bp, avg_diastolic_bp),
            "temperature": avg_temperature,
            "oxygen_saturation": avg_oxygen_saturation
        })
    return rolling_averages


if __name__ == '__main__':
    # Example usage
    vitals_series = [
        {"heart_rate": 70, "blood_pressure": (120, 80), "temperature": 37.0, "oxygen_saturation": 98},
        {"heart_rate": 75, "blood_pressure": (125, 82), "temperature": 37.2, "oxygen_saturation": 99},
        {"heart_rate": 80, "blood_pressure": (130, 85), "temperature": 37.4, "oxygen_saturation": 97},
        {"heart_rate": 85, "blood_pressure": (135, 88), "temperature": 37.6, "oxygen_saturation": 96}
    ]
    rolling_averages = calculate_rolling_average(vitals_series)
    print(rolling_averages)
