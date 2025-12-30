from vitals_generator import generate_vitals
from risk_calculator import calculate_risk_score
from publisher import publish_data

if __name__ == '__main__':
    vitals = generate_vitals()
    risk_score = calculate_risk_score(vitals)
    publish_data(vitals, risk_score)
