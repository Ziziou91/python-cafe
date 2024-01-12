"""Testing for user_input functions"""
import pytest
from src.user_input import validate_input, find_user_input_in_valid_inputs, create_amend_item_list, handle_owner_stock_inputs

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
        ("\"help\"", "owner", "", "help"),
        ("about", "owner", "", "about"),
        ("about!?'`", "owner", "", "about"),
        ("![]=back!?'`", "owner", "", "back"),
        ("![]exit!?'`", "owner", "", "exit"),
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
        ("HELP", "owner", "", "help"),
        ("STOCK", "owner", "", "stock"),

    )
)

def test_validate_input_handles_capitals(input_str, called_from, prompt, expected):
    """ensures that validate_input handles strings with capital letters"""
    assert validate_input(input_str, called_from, prompt)  ==  expected

@pytest.mark.parametrize(
    ("input_str", "called_from", "prompt", "expected"),
    (
        ("owners", "app", "", "owner"),
        ("owner's", "app","", "owner"),
        ("customers", "app", "", "customer"),
        ("customer's", "app", "", "customer"),
        ("cancels", "app", "", "cancel"),
        ("stocks", "owner", "", "stock"),
        ("products", "owner", "", "product"),
    )
)

def test_validate_input_handles_plurals(input_str, called_from, prompt, expected):
    """ensures that validate_input handles strings with capital letters"""
    assert validate_input(input_str, called_from, prompt)  ==  expected

# --------find_user_input_in_valid_inputs tests--------
def test_find_user_input_in_valid_inputs_returns_string():
    """ensures that find_user_input_in_valid_inputs returns a string"""
    assert isinstance(find_user_input_in_valid_inputs("owner", "app", ""), str)

@pytest.mark.parametrize(
    ("input_str", "called_from", "prompt", "expected"),
    (
        ("owner", "app", "", "owner"),
        ("customer", "app","", "customer"),
        ("cancel", "app", "", "cancel"),
        ("stock", "owner", "", "stock"),
        ("help", "owner", "", "help"),
        ("about", "owner", "", "about"),
        ("product", "owner", "", "product"),
        ("exit", "owner", "", "exit"),
    )
)

def test_find_user_input_in_valid_inputs(input_str, called_from, prompt, expected):
    """returns input_str when it's found in valid_inputs"""
    assert find_user_input_in_valid_inputs(input_str, called_from, prompt)  ==  expected

# --------create_amend_item_list tests--------
def test_create_amend_item_list_returns_list():
    """ensures that create_amend_item_list returns a list"""
    assert isinstance(create_amend_item_list("amend pasta", "app", ""), list)

@pytest.mark.parametrize(
    ("input_str", "expected"),
    (
        ("amend pasta", ["amend", "pasta"]),
        ("amend baked potato", ["amend", "baked potato"]),
        ("amend chips", ["amend", "chips"]),
    )
)
def test_create_amend_item_list_returns_expected(input_str, expected):
    """returns input_str when it's found in valid_inputs"""
    assert create_amend_item_list(input_str, "", "") == expected

# --------handle_owner_stock_inputs tests--------
def test_handle_owner_stock_inputs_returns_list():
    """ensures that handle_owner_stock_inputs returns a list"""
    assert isinstance(handle_owner_stock_inputs("amend pasta", "", ""), list)

@pytest.mark.parametrize(
    ("input_str", "expected"),
    (
        ("amend pasta", ['pasta', {'price': 5.0, 'stock': 5}]),
        ("amend baked potato", ['baked potato', {'price': 4.5, 'stock': 3}]),
        ("amend chips", ['chips', {'price': 2.5, 'stock': 0}]),
    )
)
def test_handle_owner_stock_inputs_returns_expected(input_str, expected):
    """returns input_str when it's found in valid_inputs"""
    assert handle_owner_stock_inputs(input_str, "", "") == expected

@pytest.mark.parametrize(
    ("input_str", "expected"),
    (
        ("AMEND PASTA", ['pasta', {'price': 5.0, 'stock': 5}]),
        ("AMEND BAKED POTATO", ['baked potato', {'price': 4.5, 'stock': 3}]),
        ("amend CHIPS", ['chips', {'price': 2.5, 'stock': 0}]),
    )
)
def test_handle_owner_stock_inputs_handles_capitilisation(input_str, expected):
    """returns input_str when it's found in valid_inputs"""
    assert handle_owner_stock_inputs(input_str, "", "") == expected

