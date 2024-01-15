from src.owner.owner import owner

# --------validate_input tests--------
def test_validate_input_returns_string():
    """ensures that validate_input returns a string"""
    assert isinstance(validate_input("owner", "app", ""), str)
