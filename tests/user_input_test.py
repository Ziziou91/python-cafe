from src.user_input import validate_input
import pytest

# --------validate_input tests--------
def test_validate_input_returns_string():
    """ensures that validate_input returns a string"""
    assert isinstance(validate_input("owner"), str)

@pytest.mark.parametrize(
    ("input_str", "called_from", "expected"),
    (
        ("owner", "app", "owner"),
        ("owner.", "app", "owner"),
        ("\"owner\"", "app", "owner"),
        ("customer", "app", "customer"),
        ("customer.", "app", "customer"),
        ("\"customer\"", "app", "customer"),
        ("\"customer!?,.;", "app", "customer"),
    )
)

def test_validate_input_handles_punctuation(input_str, called_from, expected):
    """ensures that validate_input removes punctuation and handles singular, as well as plural"""
    assert validate_input(input_str)  ==  expected

@pytest.mark.parametrize(
    ("input_str", "called_from", "expected"),
    (
        ("Owner", "app", "owner"),
        ("OWNER.", "app", "owner"),
        ("Customer", "app", "customer"),
        ("CUSTOMER", "app", "customer"),
        ("CuStOmEr\"", "app", "customer"),
    )
)

def test_validate_input_handles_capitals(input_str, called_from, expected):
    """ensures that validate_input handles strings with capital letters"""
    assert validate_input(input_str)  ==  expected