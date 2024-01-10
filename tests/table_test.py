"""Testing for functions in src/table.py"""
from src.table import create_line, create_cell

# Testing for create_line function
def test_create_line_returns_string():
    """ensures that create_line returns a string"""
    assert isinstance(create_line(), str)

def test_create_line_returns_default_string():
    """Ensures create_line returns the correct default string when no args.
    
    This should be the top line of the table.
    """
    default = "|      Item      |      Price     |      Stock     |   Stock Value  |"
    assert create_line() == default

# Testing for create_cell function
def test_create_line_returns_cell():
    """ensures that create_cell returns a string"""
    assert isinstance(create_cell('test', 10), str)
