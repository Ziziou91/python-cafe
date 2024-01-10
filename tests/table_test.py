"""Testing for functions in src/table.py"""
from src.table import create_line, create_cell, draw_user

# Testing create_line function
def test_create_line_returns_string():
    """ensures that create_line returns a string"""
    assert isinstance(create_line(), str)

def test_create_line_returns_default_string():
    """Ensures create_line returns the correct default string when no args.
    
    This should be the top line of the table.
    """
    default = "|      Item      |      Price     |      Stock     |   Stock Value  |"
    assert create_line() == default

# Testing create_cell function
def test_create_cell_returns_string():
    """ensures that create_cell returns a string"""
    assert isinstance(create_cell('test', 10), str)


# Testing draw_user function
def test_draw_user_returns_string():
    """ensures that create_cell returns a string"""
    assert isinstance(draw_user('owner'), str)
    assert isinstance(draw_user('customer'), str)

def test_draw_user_returns_expected_value():
    """ensures that create_cell returns a string"""
    expected_owner_str = f"{'-'*24}\n|{' '*22}|\n|{' '*9}Owner{' '*8}|\n|{' '*22}|\n{'-'*24}"
    expected_customer_str = f"{'-'*24}\n|{' '*22}|\n|{' '*7}Customer{' '*7}|\n|{' '*22}|\n{'-'*24}"
    assert  draw_user("customer") == expected_customer_str
    assert  draw_user("owner") == expected_owner_str
