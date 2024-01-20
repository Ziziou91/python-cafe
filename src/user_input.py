"""Logic for user inputs across the cafe app. Handles punctiation, capitalisations and plurals."""
import re
from data.cafe_data import stock

valid_inputs = {
    "app" : ["owner", "customer", "cancel"],
    "owner" : ["help", "exit", "stock", "back", "about", "product"],
    "owner_stock" : ["help", "back", "exit", "amend"],
    "amend_menu" : ["price", "stock", "help", "about", "back", "exit"],
    "owner_product" : ["back", "exit", "help", "about", "add", "remove"]
}

def get_input(prompt: str) -> str:
    """Simple function to return user input."""
    return input(prompt)

def handle_input(prompt: str, called_from: str = "none") -> str:
    """Calls get_input before passing to validate_str and then returns."""
    user_str = get_input(prompt)
    # if called_from == "owner_stock":
    #     return handle_owner_stock_inputs(user_str, prompt, called_from)
    if called_from == "owner_product"  or called_from == "owner_stock":
        return handle_owner_stock_product_inputs(user_str, prompt, called_from)
    elif called_from == "amend_menu":
        return handle_amend_menu_inputs(user_str, prompt, called_from)
    else: 
        validated_str = validate_input(user_str)
        return validated_str

def validate_input(user_input: str) -> str:
    """Checks the passed user_str is valid. If not, recursively ask the user to input again."""
    user_input = re.sub(r"[^\w\s]", "", user_input).lower().strip()
    return  user_input

def handle_owner_stock_product_inputs(user_str: str, prompt: str, called_from: str):
    validated_str = validate_input(user_str)
    if validated_str in valid_inputs[called_from]:
            return validated_str
    input_list =  validated_str.lower().split(" ", 1)
    try:
        if len(input_list) != 2 or input_list[0] not in valid_inputs[called_from]:
            raise ValueError(f"\n{"="*10}ERROR! '{user_str}' is not not a valid command! Please try again.{"="*10}\n")
    except ValueError as e:
            print(e)
            return handle_input(prompt, called_from)
    product_add = called_from == "owner_product" and input_list[0] == 'add'
    product_remove = called_from == "owner_product" and input_list[0] == 'remove'
    amend_stock = called_from == "owner_stock"
    item = input_list[1]
    if product_remove or amend_stock:
        try:
            stock[item]
        except KeyError:
            print(f"\n{"="*10}ERROR! '{item}' is not not on the menu! Please try again.{"="*10}\n")
            input_list = handle_input(prompt, called_from)
    if product_add:
        try:
            if item in stock:
                raise ValueError(f"\n{"="*10}ERROR! '{item}' is already on the menu! Please try again.{"="*10}\n")
        except ValueError as e:
            print(e)
            input_list = handle_input(prompt, called_from)
    return input_list

def handle_amend_menu_inputs(user_str: str, prompt: str, called_from: str) -> list:
    # create testing for this first
    # check what type of input
    single_inputs = ["back", "help", "exit", "about"] 
    print("in handle_amend_menu_inputs")
    if user_str in single_inputs:
        return user_str
    user_list =  user_str.strip().split(" ", 1)
    print(user_list)
    if len(user_list) == 2: 
        if user_list[0] == "price" or user_list[0] == "stock":
            return user_list

# def find_user_input_in_valid_inputs(user_input: str, called_from: str, prompt: str) -> str:
#     "Checks the passed user_input exists in a list under the called_from key in valid_inputs"
#     valid_inputs = {
#         "app" : ["owner", "customer", "cancel"],
#         "owner" : ["help", "exit", "stock", "back", "about", "product"],
#         "owner_stock" : ["help", "back", "exit", "amend"],
#         "amend_menu" : ["price", "stock", "help", "about", "back", "exit"],
#         "owner_product" : ["add", "back", "exit", "help", "about", "remove"]
#     }
#     try:
#         if user_input not in valid_inputs[called_from]:
#             raise ValueError(f"\n{"="*10}ERROR! '{user_input}' is not not a valid command! Please try again.{"="*10}\n")
#     except ValueError as e:
#         print(e)
#         return handle_input(prompt, called_from)
#     else:
#         return user_input
