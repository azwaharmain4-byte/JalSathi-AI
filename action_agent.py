def get_action(issue_type: str, risk_level: str, risk_score: int) -> dict:
    if issue_type == "flood":
        if risk_level == "High":
            action = "Avoid low-lying areas and follow local disaster alerts."
        elif risk_level == "Medium":
            action = "Monitor water levels and prepare evacuation routes."
        else:
            action = "No immediate flood risk; continue routine monitoring."
    elif issue_type == "drought":
        if risk_level == "High":
            action = "Prioritize essential irrigation and reduce non-critical water use."
        elif risk_level == "Medium":
            action = "Use water-saving irrigation methods and schedule watering wisely."
        else:
            action = "Normal irrigation practices; monitor soil moisture."
    elif issue_type == "leak":
        if risk_level == "High":
            action = "Inspect pipelines immediately and report suspected leaks to authorities."
        elif risk_level == "Medium":
            action = "Check for unusual water usage and monitor for possible leaks."
        else:
            action = "Usage appears normal; continue regular pipeline checks."
    else:
        action = "No specific action available."

    reason = (
        f"Risk level is {risk_level} with score {risk_score} for {issue_type}."
    )

    return {
        "reason": reason,
        "action": action,
        "log": "Action Agent: Generated guidance."
    }