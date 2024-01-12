"""Logic for user inputs across the cafe app. Handles punctiation, capitalisations and plurals."""
import re
from data.cafe_data import stock


def get_input(prompt: str) -> str:
    """Simple function to return user input."""
    return input(prompt)

def handle_input(prompt: str, called_from: str = "none") -> str:
    """Calls get_input before passing to validate_str and then returns."""
    user_str = get_input(prompt)
    if called_from == "owner_stock":
        return handle_owner_stock_inputs(user_str, prompt, called_from)
    elif called_from == "amend_menu":
        return handle_amend_menu_inputs(user_str, prompt, called_from)
    else: 
        validated_str = validate_input(user_str, called_from, prompt)
        return validated_str

def validate_input(user_input: str, called_from: str, prompt: str) -> str:
    """Checks the passed user_str is valid. If not, recursively ask the user to input again."""
    user_input = re.sub(r"[^\w\s]", "", user_input).lower().removesuffix("s")
    user_input = find_user_input_in_valid_inputs(user_input, called_from, prompt)
    return  user_input

def find_user_input_in_valid_inputs(user_input: str, called_from: str, prompt: str) -> str:
    "Checks the passed user_input exists in a list under the called_from key in valid_inputs"
    valid_inputs = {
        "app" : ["owner", "customer", "cancel"],
        "owner" : ["help", "exit", "stock", "back", "about", "product"],
        "owner_stock" : ["help", "back", "exit", "amend"],
        "amend_menu" : ["price", "stock", "help", "about", "back", "exit"]
    }
    try:
        if user_input not in valid_inputs[called_from]:
            raise ValueError(f"\n{"="*10}ERROR! '{user_input}' is not not a valid commans! Please try again.{"="*10}\n")
    except ValueError as e:
        print(e)
        return handle_input(prompt, called_from)
    else:
        return user_input

# owner_stock logic - currently only handles inputs that start with 'amend'
def handle_owner_stock_inputs(user_str: str, prompt: str, called_from: str) -> list:
    """Handles the owner_stock input"""
    amend_item_list = create_amend_item_list(user_str, prompt, called_from)
    try:
        stock[amend_item_list[1]]
    except KeyError:
        print(f"\n{"="*10}ERROR! '{amend_item_list[1]}' cannot be foundin the cafe's stock.{"="*10}\n")
    else:
        return [amend_item_list[1], stock[amend_item_list[1]]]

def create_amend_item_list(user_str: str, prompt: str, called_from: str) -> list:
    """Ensures the use input is valid splits it into a list"""
    amend_item_list =  user_str.lower().strip().split(" ", 1)
    try:
        if amend_item_list[1] not in stock or amend_item_list[0] != "amend":
            raise ValueError(f"\n{"="*10}ERROR! '{user_str}' is not not a valid input! Please try again.{"="*10}\n")
    except ValueError as e:
        print(e)
        return create_amend_item_list(get_input(prompt), prompt, called_from)
    else:
        return amend_item_list


# amend menu item logic 
def handle_amend_menu_inputs(user_str: str, prompt: str, called_from: str) -> list:
    # create testing for this first
    # check what type of input
    if user_str == "exit":
        return user_str
    user_list =  user_str.strip().split(" ", 1)
    if len(user_list) == 2: 
        if user_list[0] == "price" or user_list[0] == "stock":
            # handle_price_stock_input(user_list)
            return user_list
# if user_list[0] is price or stock
# - check there is a second item in the list
# - check it's the right data type
# - 