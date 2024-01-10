from src.user_input import validate_input
import pytest

# --------validate_input tests--------
def test_validate_input_returns_string():
    """ensures that validate_input returns a string"""
    assert isinstance(validate_input("letters"), str)

@pytest.mark.parametrize(
    ("input_str", "expected"),
    (
        ("letters", "letters"),
        ("!?letters.", "letters"),
        ("words!?,.", "words"),
        ("[]cancel'%$^*():;./", "cancel"),
        ("word", "word"),
        ('letter', "letter"),
        ("LETTER", "letter"),
        ("WORDS", "words"),
        ("CANCEL", "cancel")
    )
)

def test_validate_input_handles_variants(input_str, expected):
    """ensures that validate_input removes punctuation and handles singular, as well as plural"""
    assert validate_input(input_str)  ==  expected