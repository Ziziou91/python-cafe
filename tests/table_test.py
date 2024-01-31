"""Testing for functions in src/table.py"""
from src.table import create_line, create_cell, draw_title

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


# Testing draw_title function
def test_draw_title_returns_string():
    """ensures that create_cell returns a string"""
    assert isinstance(draw_title('Owner'), str)
    assert isinstance(draw_title('Customer'), str)

def test_draw_title_returns_expected_value():
    """ensures that create_cell returns a string"""
    expected_owner_str = f"{'-'*24}\n|{' '*22}|\n|{' '*8}Owner{' '*9}|\n|{' '*22}|\n{'-'*24}"
    expected_customer_str = f"{'-'*24}\n|{' '*22}|\n|{' '*7}Customer{' '*7}|\n|{' '*22}|\n{'-'*24}"
    assert  draw_title("Customer") == expected_customer_str
    assert  draw_title("Owner") == expected_owner_str
