"""module that contains all of the logic for the owner functionality."""
import sys
from typing import Callable
from src.user_input import handle_input
from data.cafe_data import stock, owner_print_str
from .table import create_line, draw_title, draw_stock

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

# What I'm currently working on
def owner_stock():
    """Prints the current stock and allows the user to amend all properties, such as name, price and stock levels"""
    draw_stock()
    print(owner_print_str["owner_stock"])
    menu_item = handle_input("Type your input here: ", "owner_stock")
    amend_item(menu_item)
 
def amend_item(menu_item):
    draw_item(menu_item)
    print(owner_print_str["amend_item"])
    user_str = handle_input("Type your input here: ", "amend_menu")
    if user_str == "exit":
        sys.exit()
    elif user_str == "back":
        owner_stock()
    #  TODO logic to check second part is valid e.g not a string, is int or float ect.
    if user_str[0] == "price":
        stock[menu_item[0]][user_str[0]] = float(user_str[1])
    elif user_str[0] == "stock":
        stock[menu_item[0]][user_str[0]] = int(user_str[1])
    amend_item(menu_item)

def draw_item(menu_item):
    print(f"\n{'-'*69}")
    print(create_line())
    print(f"{'-'*69}")
    print(create_line(menu_item[0], menu_item[1]["price"], menu_item[1]["stock"]))
    print(f"{'-'*69}\n")

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