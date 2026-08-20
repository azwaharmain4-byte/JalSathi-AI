from .planner_agent import plan_query
from .data_agent import get_data
from .prediction_agent import get_prediction
from .action_agent import get_action

def run_jalsathi(query: str, location: str, issue_type: str | None = None) -> dict:
    agent_log = []

    # Planner
    plan = plan_query(query, location, issue_type)
    agent_log.append(plan["log"])

    # Data
    data = get_data(plan["issue_type"], plan["location"])
    agent_log.append(data["log"])

    # Prediction
    pred = get_prediction(plan["issue_type"], data)
    agent_log.append(pred["log"])

    # Action
    act = get_action(plan["issue_type"], pred["risk_level"], pred["risk_score"])
    agent_log.append(act["log"])

    return {
        "issue_type": plan["issue_type"],
        "location": plan["location"],
        "risk_level": pred["risk_level"],
        "risk_score": pred["risk_score"],
        "reason": act["reason"],
        "action": act["action"],
        "agent_log": agent_log
    }