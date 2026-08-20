from agents import run_jalsathi

def test_flood_query():
    result = run_jalsathi("Will Assam face flooding after heavy rainfall?", "Assam")
    assert result["issue_type"] == "flood"
    assert result["location"] == "Assam"
    assert result["risk_level"] in ["Low", "Medium", "High"]
    assert "action" in result
    assert len(result["agent_log"]) == 4

def test_drought_query():
    result = run_jalsathi("Should farmers in Mandya irrigate today?", "Mandya")
    assert result["issue_type"] == "drought"

def test_leak_query():
    result = run_jalsathi("There is unusual water usage in Indore. Could it be a leak?", "Indore")
    assert result["issue_type"] == "leak"