from typing import Callable
from data.cafe_data import valid_inputs, stock
from .user_input import format_input

def route_owner_requests(user_str, prompt, called_from, handle_input):
    if called_from == "owner":
        return check_input_in_valid_inputs(user_str, called_from)
    elif called_from == "owner_product"  or called_from == "owner_stock":
        return handle_owner_stock_product_inputs(user_str, prompt, called_from, handle_input)
    elif called_from == "amend_menu":
        return handle_amend_menu_inputs(user_str, prompt, called_from)

def handle_owner_stock_product_inputs(user_str: str, prompt: str, called_from: str, handle_input: Callable):
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

def handle_amend_menu_inputs(user_str: str, prompt: str, called_from: str) -> list:
    """handles inputs from the amend function for any menu item"""
    # create testing for this first
    # check what type of input
    single_inputs = ["back", "help", "exit", "about"]
    if user_str in single_inputs:
        return user_str
    input_list =  user_str.lower().split(" ", 1)
    command = format_input(input_list[0])
    if len(input_list) == 2: 
        if command == "price" or command == "stock":
            return input_list
    # TODO - does this need an else statement
        

def check_input_in_valid_inputs(user_input, called_from):
    """Checks if a given input string from app function exists in the valid input dictionary."""
    try:
        if user_input not in valid_inputs[called_from]:
            raise ValueError(f"\n{'='*10}ERROR! '{user_input}' is not not a valid command! Please try again.{'='*10}\n")
    except ValueError as e:
        print(e)
    return user_input
