def get_prediction(issue_type: str, data: dict) -> dict:
    # Placeholder risk logic; later replace with Azwa’s models.
    risk_score = 50
    risk_level = "Medium"

    if issue_type == "flood":
        risk_score = 70
        risk_level = "High"
    elif issue_type == "drought":
        risk_score = 60
        risk_level = "Medium"
    elif issue_type == "leak":
        risk_score = 40
        risk_level = "Low"

    return {
        "risk_score": risk_score,
        "risk_level": risk_level,
        "log": "Prediction Agent: Calculated risk score."
    }