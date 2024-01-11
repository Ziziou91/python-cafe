import sys
from typing import Callable
from src.user_input import handle_input
from data.cafe_data import menu, stock, price
from .table import create_line, draw_title
# from .user_help import user_help

# Variable to track which part of the app the user is currently in.
# Allows the app to provide contenxtual support with help and about commands

def owner(app: Callable):
    """top level 'owner' menu in cafe app. 
    Routes user to desired functionality, or prints additional info in terminal."""
    owner_functions = {
        "owner": {
            "help" : owner_help,
            "exit": owner_exit,
            "stock": owner_stock,
            "back" : app
        }
    }   
    state = "owner"
    print(f"\n{draw_title('owner')}\n")

    print("""When using this application as owner, you have the following commands available:
          
          * stock - let's you view current stock and amend things like price, stock levels ect.
          * product - allows you to add or rfemove products
          * about - get more information abot currently availble functionality
          * help - get a list of commands
          * back - go back to the previous menu
          * exit - exit the app          
        """)
    # plug in validate_input logic
    while state == "owner":
        usr_input_str = handle_input("Type your input here: ", "owner")
        owner_functions["owner"][usr_input_str]()
        if usr_input_str != "help" and usr_input_str != "about":
            state = usr_input_str
    


def owner_help():
    print("you are in user_help")

def owner_exit():
    sys.exit()

def owner_stock():
    # Should only print the context the first time
    print(f"\n{draw_title('stock')}\n")
    print(f"{'-'*69}")
    print(create_line())
    print(f"{'-'*69}")
    for x in menu:
        print(create_line(x, price[x], stock[x]))
        print(f"{'-'*69}")




# view & manage stock
#   - when in stock view, can amend any of the cells.
#   --    Choose a product to do this
# Add a product
# Remove a product
# Type help to list of commands
# Type about to get explanation of currently available functionality
# Type back to go back to the main owner meny
# type exit to exit