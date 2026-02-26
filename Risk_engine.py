# RiskEngine/risk_engine.py
# Combine KYC, AML, and PEP checks into one risk score

def risk_score(age, country, transactions, name):
    score = 0
    
    # KYC check
    if age < 18:
        score += 50
    if country not in ["USA", "India", "UK"]:
        score += 30
    
    # AML check
    for amt in transactions:
        if amt > 100000:
            score += 40
    
    # PEP check
    PEP_LIST = ["John Doe", "Jane Smith"]
    if name in PEP_LIST:
        score += 70
    
    return score

if __name__ == "__main__":
    result = risk_score(17, "USA", [5000, 200000], "John Doe")
    print("Final Risk Score:", result)