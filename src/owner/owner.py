"""module to handle owner functionality. 
The user can view and amend stock, as well as add and remove items.
"""
import sys
from typing import Callable
from src.user_input import handle_input
from data.cafe_data import stock, owner_print_str
from ..table import create_line, draw_title, draw_stock, draw_item

# Multi-line print statements can be found in data module, stored in owner_print_str dictionary.

def owner(app: Callable):
    """top level 'owner' menu in cafe app. 
    Routes user to desired functionality, or prints additional info in terminal."""
    owner_functions = {
            "help" : owner_help,
            "exit": owner_exit,
            "stock": owner_stock,
            "back" : app,
            "about" : owner_about,
            "product" : owner_product
    }
    state = "main"
    print(f"\n{draw_title('owner')}\n")

    print(owner_print_str["main"])
# TODO Put this logic in a differnt function. Will allow me to return the string to print from owner_ functions and test them.
    while state == "main":
        usr_input_str = handle_input("Type your input here: ", "owner")
        owner_functions[usr_input_str]()
        if usr_input_str != "help" and usr_input_str != "about":
            state = usr_input_str

def owner_stock() -> None:
    """Prints the current stock and allows the user to amend all properties, such as name, price and stock levels"""
    draw_stock()
    print(owner_print_str["owner_stock"])
    menu_item = handle_input("Type your input here: ", "owner_stock")
    amend_item(menu_item)
 
def amend_item(menu_item: str):
    # add default value so it can not print
    """Called when the user inputs 'amend `item`' from owner_stock. 
    Takes subsequent user input and then passes it to handle_amend_item_inputs to be processed."""
    draw_item(menu_item)
    print(owner_print_str["amend_item"])
    user_input = handle_input("Type your input here: ", "amend_menu")
    # needs a better name
    handle_amend_item_inputs(menu_item, user_input)


def handle_amend_item_inputs(menu_item: str, user_input: str or list) -> None:
    """Takes the user input from 'amend_item' and executes the requested logic.
    Creates a command_str string to make logic more readable. 
    """
    # not passing through values when command isn't price or stock 
    print(user_input)
    if isinstance(user_input, list):
        command_str, new_value = user_input[0], user_input[1]
    else:
        command_str = user_input
    if command_str == "exit":
        sys.exit()
    elif command_str == "back":
        owner_stock()
    elif command_str == "help":
        print(owner_print_str["amend_item"])
    elif command_str == "about":
         print(owner_print_str["amend_item_about"])
    elif command_str == "price" or command_str == "stock":
        print("user_input", user_input)
        print("new_value", new_value) 
        stock[menu_item[0]][command_str] = validate_new_value_type(command_str, new_value, menu_item)
    amend_item(menu_item)

def validate_new_value_type(command_str: str, new_value: str, menu_item):
    """ensures new_value type is a float for price, and integer for stock"""
    if command_str == "price":
        try:
            float(new_value)
            if float(new_value) < 0:
                raise ValueError
        except ValueError:
            print(f"\n{"="*10}ERROR! '{new_value}' should be a positive number! Please try again.{"="*10}\n")
            return amend_item(menu_item)
        else:
            return float(new_value)
    elif command_str == "stock":
        try:
            int(new_value)
            if int(new_value) < 0:
                raise ValueError
        except ValueError:
            print(f"\n{"="*10}ERROR! '{new_value}' should be a positive integer! Please try again.{"="*10}\n")
            return amend_item(menu_item)
        else:
            return int(new_value)

def owner_product():
    """Will allow the user to add and remove products, amending data accordingly"""
    print("you are in owner_product")

def owner_about():
    print("you are in owner_about")

def owner_help():
    print("you are in owner_help")

def owner_exit():
    sys.exit()


# view & manage stock
#   - when in stock view, can amend any of the cells.
#   --    Choose a product to do this
# Add a product
# Remove a product
# Type help to list of commands
# Type about to get explanation of currently available functionality
# Type back to go back to the main owner meny
# type exit to exit