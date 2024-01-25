from re import sub
from decimal import Decimal
from typing import Callable
from data.cafe_data import valid_inputs, stock

def route_customer_requests(user_str: str, prompt: str, called_from: str, handle_input: Callable):
    if called_from == "customer":
        return handle_customer_inputs(user_str, prompt, called_from, handle_input)
    elif called_from == "customer_order_count":
        return handle_customer_order_count(user_str)


def handle_customer_order_count(user_str):
    if user_str == "cancel":
        return user_str
    else:
        return create_num_string("stock_count", user_str)
    
def create_num_string(command_str: str, new_value: str,) -> int or float:
    """Returns a float when the input string is a price. Returns an integer when the input string is a stock count."""
    new_value = Decimal(sub(r'[^\d.]', '', new_value))
    if command_str == "price":
        return float(new_value)
    elif command_str == "stock_count":
        return int(new_value)

def handle_customer_inputs(user_str: str, prompt: str, called_from: str, handle_input):
    if user_str in valid_inputs[called_from]:
            return user_str
    input_list =  user_str.lower().split(" ", 1)
    try:
        if len(input_list) != 2 or input_list[0] != "order":
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