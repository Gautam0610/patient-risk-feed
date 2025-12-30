from vitals_generator import generate_vitals_series
from risk_calculator import calculate_risk_score
from publisher import publish_data
from rolling_average import calculate_rolling_average

if __name__ == '__main__':
    vitals_series = generate_vitals_series()
    rolling_averages = calculate_rolling_average(vitals_series)
    if rolling_averages:
        # Only publish if rolling averages are available
        for i in range(len(rolling_averages)):
            vitals = vitals_series[i + 2]  # Vitals corresponding to the rolling average
            risk_score = calculate_risk_score(vitals)
            publish_data(vitals, risk_score, [rolling_averages[i]])  # Pass rolling average as a list
    else:
        print("Not enough data to calculate rolling averages.")
