from src.table import create_line

def test_create_line_returns_string():
    """ensures that capitalize_words returns a string"""
    assert isinstance(create_line(), str)
