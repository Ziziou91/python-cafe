"""module to handle owner functionality. 
The user can view and amend stock, as well as add and remove items.
"""
from re import sub
import sys
from typing import Callable
from decimal import Decimal
from data.cafe_data import stock, owner_print_str
from src.user_input import handle_input, validate_num_string
from .table import draw_title, draw_stock, draw_item
# Multi-line print statements can be found in data module, stored in owner_print_str dictionary.
# TODO - Product
# TODO - Customer

def owner(app: Callable):
    """top level 'owner' menu in cafe app. 
    Routes user to desired functionality, or prints additional info in terminal."""
    owner_functions = {
            "help" :[owner_help,()],
            "exit": [owner_exit,()],
            "stock": [owner_stock, (owner, app)],
            "back" : [app,()],
            "about" : [owner_about,()],
            "product" : [owner_product,(owner, app)]
    }
    state = "main"
    print(f"\n{draw_title('owner')}\n")
    print(owner_print_str["main"])
    while state == "main":
        usr_input_str = handle_input("Type your input here: ", "owner")
        owner_functions[usr_input_str][0](*owner_functions[usr_input_str][1])
        if usr_input_str != "help" and usr_input_str != "about":
            state = usr_input_str

def owner_stock(owner_func: Callable, app: Callable) -> None:
    """Prints the current stock and allows the user to amend all properties, such as name, price and stock levels"""
    print(f"\n{draw_title('stock')}\n")
    draw_stock()
    print(owner_print_str["owner_stock"])
    menu_item = handle_input("Type your input here: ", "owner_stock")
    while not isinstance(menu_item, list):
        if menu_item == "help":
            print(owner_print_str["owner_stock_help"])
        elif menu_item == "about":
            print("owner_stock about")
        elif menu_item == "back":
            owner_func(app)
        elif menu_item == "exit":
            sys.exit()
        menu_item = handle_input("Type your input here: ", "owner_stock")
    print(draw_item(menu_item[1]))
    print(owner_print_str["amend_item"])
    user_input = handle_input("Type your input here: ", "amend_menu")
    resolve_amend_item_inputs(menu_item[1], user_input, owner_stock, app)

def resolve_amend_item_inputs(item: str, user_input: str or list, owner_stock: Callable, app:Callable) -> None:
    """Takes the user input from 'amend_item' and executes the requested logic.
    Creates a command_str string to make logic more readable. 
    """
    print("menu_item in resolve_amend_item_inputs", item)
    # TODO not passing through values when command isn't price or stock 
    try:
        if isinstance(user_input, list):
            command_str, new_value = user_input[0], user_input[1]
            print(command_str, new_value)
        else:
            command_str = user_input
        if command_str == "exit":
            sys.exit()
        elif command_str == "back":
            owner_stock(owner, app)
        elif command_str == "help":
            print(owner_print_str["amend_item"])
        elif command_str == "about":
            print(owner_print_str["amend_item_about"])
        elif command_str == "price" or command_str == "stock":
            stock[item][command_str] = validate_num_string(command_str, new_value)
            print(draw_item(item))
        else:
            raise ValueError(f"\n{"="*10}ERROR! '{user_input}' is not not a valid input! Please try again.{"="*10}\n")
    except ValueError as e:
            print(e)
    else:
        user_input = handle_input("Type your input here: ", "amend_menu")
        resolve_amend_item_inputs(item, user_input, owner_stock, app)

def validate_new_value_type(command_str: str, new_value: str, item: list, owner_stock: Callable, app: Callable) -> int or float:
    """ensures new_value type is a float for price, and integer for stock."""
    try:
        new_value = Decimal(sub(r'[^\d.]', '', new_value))
        if command_str == "price":
            float(new_value)
            if float(new_value) < 0:
                raise ValueError
        elif command_str == "stock":
            int(new_value)
            if int(new_value) < 0:
                raise ValueError
    except Exception:
        print(f"\n{"="*10}ERROR! '{new_value}' should be a positive number! Please try again.{"="*10}\n")
        user_input = handle_input("Type your input here: ", "amend_menu")
        #amend this, should be useable for all numerical values 
        resolve_amend_item_inputs(item, user_input, owner_stock, app)
    else:
        if command_str == "price":
            return float(new_value)
        elif command_str == "stock":
            return int(new_value)
        

            
def owner_product(owner_func, app) -> None:
    """Will allow the user to add and remove products, amending data accordingly"""
    print(f"\n{draw_title('product')}\n")
    draw_stock()
    print(owner_print_str["product"])
    command = handle_input("Type your input here: ", "owner_product")
    if command == "back":
        owner_func(app)
    elif command == "help":
        print(owner_print_str["owner_product"])
    elif command == "exit":
        sys.exit()
    elif command[0] == "add":
        add_product(command[1], owner_product, owner_func, app)
    elif command[0] == "remove":
        del stock[command[1]]
        owner_product(owner_func, app)

    # validate the input
    # if relevant, split the input in 2. Otherwise just print or 
    # Add - check it's not alread in the product menu
    # prompt the user to provide price and initial stock, validate these (reuse code from amend?)
    # Remove - check the prouct exists
    # warning message if they still have stock
    # redraw stock

def add_product(item_name: str, owner_product_func: Callable, owner_func: Callable, app: callable) -> None:
    print(f"\n{draw_title(item_name)}\n")
    price = handle_input("Please enter a price: ", "price")
    stock_count = handle_input("Please enter the number of items in stock: ", "stock_count")
    print(f"{item_name} price", price)
    print(f"{item_name} stock", stock_count)
    stock[item_name] = {"price": price, "stock": stock_count}
    print(draw_item(item_name))
    owner_product_func(owner_func, app)


def remove_product(item_name: str):
    print("in remove_product")
    print(item_name)

def owner_about():
    print("you are in owner_about")

def owner_help():
    print(owner_print_str["owner_stock_help"])

def owner_exit():
    sys.exit()

