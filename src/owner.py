"""module to handle owner functionality. 
The user can view and amend stock, as well as add and remove items.
"""
import sys
from typing import Callable
from re import sub
import decimal
from data.cafe_data import stock, owner_print_str, order, valid_inputs
from .table import draw_title, draw_stock, draw_item
from .unit_functions import update_cafe_data, get_input

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
    try:
        if user_str not in valid_inputs["owner"]:
            raise ValueError(f"\n{'='*10}ERROR! '{user_str}' is not not a valid input! Please try again.{'='*10}\n")
    except ValueError as e:
        print(e)
        return validate_owner_inputs(prompt)
    else:
        return user_str
    
def handle_owner_inputs(user_input: str, app: Callable) -> None:
    """Handles valid owner inputs. Either prints requested string, or calls required function."""
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
        owner_product(app)

def owner_stock(app: Callable) -> None:
    """Prints the current stock and allows the user to amend all properties, such as name, price and stock levels"""
    print(f"\n{draw_title('stock')}\n")
    draw_stock(stock)
    print(owner_print_str["owner_stock"])
    handle_owner_stock_input(app)

def handle_owner_stock_input(app: Callable) -> None:
    """Requests user input in owner stock meny, handles and passes to 'handle_owner_stock_amend_item'."""
    user_str = get_input("Type your input here: ")
    if user_str == "help":
        print(owner_print_str["owner_stock_help"])
    elif user_str == "about":
        print("owner_stock about")
    elif user_str == "back":
        owner(app)
    elif user_str == "exit":
        order.clear()
        update_cafe_data()
        sys.exit()
    else:
        input_list =  user_str.lower().split(" ", 1)
        command, item = input_list[0], input_list[1]
        try:
            if item not in stock or command != "amend":
                raise ValueError(f"\n{'='*10}ERROR! '{user_str}' is not not a valid command! Please try again.{'='*10}\n")
        except ValueError as e:
            print(e)
            return handle_owner_stock_input(app)
        else:
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

def owner_product(app: Callable) -> None:
    """Prints the current stock and allows the user to amend all properties, such as name, price and stock levels"""
    print(f"\n{draw_title('product')}\n")
    draw_stock(stock)
    print(owner_print_str["product"])
    handle_owner_product_input(app)

def handle_owner_product_input(app: Callable) -> None:
    """Takes user input, validates and passes to add_product if required. Otherwise prints string or removes product from stock."""
    user_str = get_input("Type your input here: ")
    if user_str == "help":
        print(owner_print_str["owner_product"])
    elif user_str == "back":
        owner(app)
    elif user_str == "exit":
        order.clear()
        update_cafe_data()
        sys.exit()
    else:
        input_list =  user_str.lower().split(" ", 1)
        command, item = input_list[0], input_list[1]
        print("command: ", command, "Item: ", item)
        # Checks that the first part of the user input (command) is either 'add' or 'remove'.
        try:
            if command != "add" and command != "remove":
                raise ValueError(f"\n{'='*10}ERROR! '{user_str}' is not not a valid command! Please try again.{'='*10}\n")
        except ValueError as e:
            print(e)
            return handle_owner_product_input(app)
        else:
            if command == "add":
                # Checks that item isn't already in stock dictionary. If it is, ask user to start again.
                try:
                    if item in stock:
                        raise ValueError(f"\n{"="*10}ERROR! '{item}' is already on the menu! Please try again.{"="*10}\n")
                except ValueError as e:
                    print(e)
                    return handle_owner_product_input(app)
                else:
                    add_product(item, app)
            elif command == "remove":
                # Checks that item is already in stock dictionary. If it is, ask user to start again.
                try:
                    if item not in stock:
                        raise ValueError(f"\n{"="*10}ERROR! '{item}' is not on the menu! Please try again.{"="*10}\n")
                except ValueError as e:
                    print(e)
                    return handle_owner_product_input(app)
                else:
                    del stock[item]
                    print(f"\n{item} successfully removed! Returning you to product menu.\n")
                    update_cafe_data()
                    print(f"\n{draw_title('product')}\n")
    handle_owner_product_input(app)
            
def add_product(item: str, app: Callable) -> None:
    """Takes user inputs for price and stock, validates and then adds the product to stock dictionary."""
    print(f"\n{draw_title(item)}\n")
    new_price, new_stock = 0, 0
    price_str = get_input("Please enter a price: ")
    try:
        new_price = decimal.Decimal(sub(r'[^\d.]', '', price_str))
    except decimal.InvalidOperation:
        print(f"\n{'='*10}ERROR! '{new_price}' is not not a valid price! Please try again.{'='*10}\n")
        return add_product(item, app)
    stock_str = get_input("Please enter the number of items in stock: ")
    try:
        new_stock = decimal.Decimal(sub(r'[^\d.]', '', stock_str))
    except decimal.InvalidOperation:
        print(f"\n{'='*10}ERROR! '{stock_str}' is not not a valid stock count! Please try again.{'='*10}\n")
        return add_product(item, app)
    stock[item] = {"price": float(new_price), "stock": int(new_stock)}
    draw_item(item)
    update_cafe_data()
    print(f"\n{item} successfully added! Returning you to product menu.\n")
    print(f"\n{draw_title('product')}\n")
