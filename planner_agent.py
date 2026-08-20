def plan_query(query: str, location: str, issue_type: str | None = None) -> dict:
    q = (query or "").lower()

    if issue_type:
        detected = issue_type
    elif any(w in q for w in ["flood", "rain", "river", "water level"]):
        detected = "flood"
    elif any(w in q for w in ["drought", "dry", "irrigat", "soil", "rainfall deficit"]):
        detected = "drought"
    elif any(w in q for w in ["leak", "pipeline", "burst", "water loss", "wastage"]):
        detected = "leak"
    else:
        detected = "unknown"

    return {
        "issue_type": detected,
        "location": location,
        "log": f"Planner Agent: Identified issue type as '{detected}'."
    }