from src.user_input import validate_input
import pytest

# --------validate_input tests--------
def test_validate_input_returns_string():
    """ensures that validate_input returns a string"""
    assert isinstance(validate_input("owner", "app", ""), str)

@pytest.mark.parametrize(
    ("input_str", "called_from", "prompt", "expected"),
    (
        ("owner", "app", "", "owner"),
        ("owner.", "app","", "owner"),
        ("\"owner\"", "app", "", "owner"),
        ("customer", "app", "", "customer"),
        ("customer.", "app", "", "customer"),
        ("\"customer\"", "app", "", "customer"),
        ("\"customer!?,.;", "app", "", "customer"),
        ("cancel", "app", "", "cancel"),
        ("\"cancel\"", "app", "", "cancel"),
        ("help", "owner", "", "help"),
        ("help.", "owner", "", "help"),
        ("help!", "owner", "", "help"),
        ("\"help\"", "owner", "", "help")
    )
)

def test_validate_input_handles_punctuation(input_str, called_from, prompt, expected):
    """ensures that validate_input removes punctuation and handles singular, as well as plural"""
    assert validate_input(input_str, called_from, prompt)  ==  expected

@pytest.mark.parametrize(
    ("input_str", "called_from", "prompt", "expected"),
    (
        ("Owner", "app", "", "owner"),
        ("OWNER.", "app", "", "owner"),
        ("Customer", "app", "", "customer"),
        ("CUSTOMER", "app", "", "customer"),
        ("CuStOmEr\"", "app", "", "customer"),
        ("Cancel", "app", "", "cancel"),
        ("CANCEL", "app", "", "cancel"),
    )
)

def test_validate_input_handles_capitals(input_str, called_from, prompt, expected):
    """ensures that validate_input handles strings with capital letters"""
    assert validate_input(input_str, called_from, prompt)  ==  expected

# Test to validate plurals
@pytest.mark.parametrize(
    ("input_str", "called_from", "prompt", "expected"),
    (
        ("owners", "app", "", "owner"),
        ("owner's", "app","", "owner"),
        ("customers", "app", "", "customer"),
        ("customer's", "app", "", "customer"),
        ("cancels", "app", "", "cancel"),
    )
)

def test_validate_input_handles_plurals(input_str, called_from, prompt, expected):
    """ensures that validate_input handles strings with capital letters"""
    assert validate_input(input_str, called_from, prompt)  ==  expected