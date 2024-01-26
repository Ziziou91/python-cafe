from typing import Callable
from data.cafe_data import valid_inputs, stock
from .user_input import create_num_string, format_input

def route_customer_requests(user_str: str, prompt: str, called_from: str, handle_input: Callable):
    """Uses called_from string to call appropiate customer functionality."""
    if called_from == "customer":
        return handle_customer_inputs(user_str, prompt, called_from, handle_input)
    elif called_from == "customer_order_count":
        return handle_customer_order_count(user_str)


def handle_customer_order_count(user_str: str) -> str or int or float:
    if user_str == "cancel":
        return user_str
    else:
        return create_num_string("stock_count", user_str)

def handle_customer_inputs(user_str: str, prompt: str, called_from: str, handle_input) -> list:
    if user_str in valid_inputs[called_from]:
            return user_str
    input_list =  user_str.lower().split(" ", 1)
    command = format_input(input_list[0])
    try:
        if len(input_list) != 2 or command != "order":
            raise ValueError(f"\n{"="*10}ERROR! '{user_str}' is not not a valid command! Please try again.{"="*10}\n")
    except ValueError as e:
            print(e)
            input_list = handle_input(prompt, called_from)
    item = input_list[1]
    try:
        stock[item]
    except KeyError:
        print(f"\n{"="*10}ERROR! '{item}' is not not on the menu! Please try again.{"="*10}\n")
        input_list = handle_input(prompt, called_from)
    return input_list