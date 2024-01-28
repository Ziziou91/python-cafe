"""module to handle owner functionality. 
The user can view and amend stock, as well as add and remove items.
"""
import sys
from typing import Callable
from re import sub
import decimal
from data.cafe_data import stock, owner_print_str, order, valid_inputs
from src.user_input import create_num_string
from .table import draw_title, draw_stock, draw_item
from .unit_functions import update_cafe_data, get_input, format_input

def owner(app: Callable) -> None:
    """top level 'owner' menu in cafe app. 
    Routes user to desired functionality, or prints additional info in terminal."""
    state = "main"
    print(f"\n{draw_title('owner')}\n")
    print(owner_print_str["main"])
    while state == "main":
        usr_input_str = validate_owner_inputs("Type your input here: ")
        handle_owner_inputs(usr_input_str, app)


def validate_owner_inputs(prompt: str) -> list:
    """Takes user input and confirms it's in valid_inputs dictionary before returning"""
    user_str = get_input(prompt)
    print("user_str", user_str)
    try:
        if user_str not in valid_inputs["owner"]:
            raise ValueError(f"\n{'='*10}ERROR! '{user_str}' is not not a valid input! Please try again.{'='*10}\n")
    except ValueError as e:
        print(e)
        return validate_owner_inputs(prompt)
    else:
        return user_str
    
def handle_owner_inputs(user_input: str, app: Callable):
    """Hanldles valid owner inputs. Either prints requested string, or calls required function."""
    if user_input == "help":
        print(owner_print_str["main"])
    elif user_input == "about":
        print(owner_print_str["about"])
    elif user_input == "exit":
        order.clear()
        update_cafe_data()
        sys.exit()
    elif user_input == "back":
        app()
    elif user_input == "stock":
        owner_stock(app)
    elif user_input == "product":
        owner_product(owner, app)

def owner_stock(app: Callable) -> None:
    """Prints the current stock and allows the user to amend all properties, such as name, price and stock levels"""
    print(f"\n{draw_title('stock')}\n")
    draw_stock(stock)
    print(owner_print_str["owner_stock"])
    handle_owner_stock_input(app)

def handle_owner_stock_input(app: Callable):
    print("IN HANDLE_OWNER_STOCK_INPUT")
    user_str = get_input("Type your input here: ")
    user_input = handle_owner_stock_product_inputs(user_str, "Type your input here: ", "owner_stock")
    if user_input == "help":
        print(owner_print_str["owner_stock_help"])
    elif user_input == "about":
        print("owner_stock about")
    elif user_input == "back":
        owner(app)
    elif user_input == "exit":
        order.clear()
        update_cafe_data()
        sys.exit()
    else:
        item = user_input[1]
        draw_item(item)
        print(owner_print_str["amend_item"])
        handle_owner_stock_amend_item(item, app)
    handle_owner_stock_input(app)

def handle_owner_stock_amend_item(item: str, app: Callable) -> None:
    """Requests user input in menu to amend an item's price or stock, validates and then updates 'cafe_data'."""
    user_amend_str = get_input("Type your input here: ")
    if user_amend_str == "exit":
        order.clear()
        update_cafe_data()
        sys.exit()
    elif user_amend_str == "back":
        owner_stock(app)
    elif user_amend_str == "help":
        print(owner_print_str["amend_item"])
    elif user_amend_str == "about":
        print(owner_print_str["amend_item_about"])
    else:
        input_list =  user_amend_str.lower().split(" ", 1)
        command_str = input_list[0]
        if len(input_list) == 2: 
            if command_str == "price" or command_str == "stock":
                new_value = input_list[1]
        try:
            new_num = decimal.Decimal(sub(r'[^\d.]', '', new_value))
        except decimal.InvalidOperation:
            print(f"\n{'='*10}ERROR! '{user_amend_str}' is not not a valid command! Please try again.{'='*10}\n")
            return handle_owner_stock_amend_item(item, app)
        else:
            if command_str == "price":
                stock[item][command_str] = float(new_num)
            elif command_str == "stock":
                stock[item][command_str] = int(new_num)
            update_cafe_data()
            draw_item(item)
            handle_owner_stock_amend_item(item, app)

def owner_product(owner_func, app) -> None:
    """Will allow the user to add and remove products, amending data accordingly"""
    print(f"\n{draw_title('product')}\n")
    draw_stock(stock)
    print(owner_print_str["product"])
    command = handle_input("Type your input here: ", "owner_product")
    if command == "back":
        owner_func(app)
    elif command == "help":
        print(owner_print_str["owner_product"])
    elif command == "exit":
        order.clear()
        update_cafe_data()
        sys.exit()
    elif command[0] == "add":
        add_product(command[1], owner_product, owner_func, app)
    elif command[0] == "remove":
        del stock[command[1]]
    owner_product(owner_func, app)

def add_product(item_name: str, owner_product_func: Callable, owner_func: Callable, app: callable) -> None:
    print(f"\n{draw_title(item_name)}\n")
    price = handle_input("Please enter a price: ", "price")
    stock_count = handle_input("Please enter the number of items in stock: ", "stock_count")
    print(f"{item_name} price", price)
    print(f"{item_name} stock", stock_count)
    stock[item_name] = {"price": price, "stock": stock_count}
    print(draw_item(item_name))
    owner_product_func(owner_func, app)

def owner_about() -> None:
    print("you are in owner_about")

def owner_help() -> None:
    print(owner_print_str["main"])

def handle_input(prompt: str, called_from: str = "none") -> str:
    """Calls get_input before passing to appropiate handler function and then returns."""
    #seperate into owner and customer functionality
    customer_requests = ["customer", "customer_order_count"]
    owner_requests = ["owner", "owner_stock", "owner_product", "amend_menu"]
    user_str = get_input(prompt)
    if called_from == "price" or called_from == "stock_count":
        return create_num_string(called_from, user_str)
    else:
        if called_from == "app":
            return check_input_in_valid_inputs(user_str)
        elif called_from in owner_requests:
            if called_from == "owner_product"  or called_from == "owner_stock":
                return handle_owner_stock_product_inputs(user_str, prompt, called_from)
            elif called_from == "amend_menu":
                pass
                # return handle_amend_menu_inputs(user_str, prompt, called_from)
            elif called_from in customer_requests:
                # return route_customer_requests(user_str, prompt, called_from, handle_input)
                pass

def check_input_in_valid_inputs(user_input):
    """Checks if a given input string from app function exists in the valid input dictionary."""
    try:
        if user_input not in valid_inputs["owner"]:
            raise ValueError(f"\n{'='*10}ERROR! '{user_input}' is not not a valid command! Please try again.{'='*10}\n")
    except ValueError as e:
        print(e)
    return user_input

def handle_owner_stock_product_inputs(user_str: str, prompt: str, called_from: str):
    """takes inputs from both product and stock owner functions, validates and then returns"""
    if user_str in valid_inputs[called_from]:
            return user_str
    input_list =  user_str.lower().split(" ", 1)
    command = format_input(input_list[0])
    try:
        if len(input_list) != 2 or command not in valid_inputs[called_from]:
            raise ValueError(f"\n{'='*10}ERROR! '{user_str}' is not not a valid command! Please try again.{'='*10}\n")
    except ValueError as e:
            print(e)
            return handle_input(prompt, called_from)
    product_add = called_from == "owner_product" and command == 'add'
    product_remove = called_from == "owner_product" and command == 'remove'
    amend_stock = called_from == "owner_stock"
    item = input_list[1]
    if product_remove or amend_stock:
        try:
            stock[item]
        except KeyError:
            print(f"\n{'='*10}ERROR! '{item}' is not not on the menu! Please try again.{'='*10}\n")
            input_list = handle_input(prompt, called_from)
    if product_add:
        try:
            if item in stock:
                raise ValueError(f"\n{"="*10}ERROR! '{item}' is already on the menu! Please try again.{"="*10}\n")
        except ValueError as e:
            print(e)
            input_list = handle_input(prompt, called_from)
    return input_list
