import sys
from typing import Callable
from re import sub
import decimal
from data.cafe_data import stock, customer_print_str, valid_inputs, order
from .table import draw_title, draw_stock, draw_item
from .unit_functions import sum_up_order, get_input, format_input, update_cafe_data

def customer(app: Callable) -> None:
    """Top level 'customer' menu in cafe app. 
    Takes user input, passes to subsequent handles_customer_input and awaits next input."""
    state = "main"
    print(f"\n{draw_title('customer')}\n")
    while state == "main":
        print(customer_print_str["main"])
        usr_input_str = validate_customer_inputs("Type your input here: ")
        handle_customer_input(usr_input_str, app)

def handle_customer_input(user_input: str, app: Callable) -> None:
    """Handles user_input, and calls customer functionality."""
    if user_input == "menu":
        draw_stock(stock)
    elif user_input == "back":
        app()
    elif user_input == "exit":
        order.clear()
        update_cafe_data()
        sys.exit()
    elif user_input == "bill":
        draw_stock(order)
    elif user_input == "pay":
        total = sum_up_order()
        print(f"\nYou owe £{total}.'n")
    elif user_input[0] == "order":
        stock_order_quantity(user_input[1])
    
def validate_customer_inputs(prompt: str) -> list:
    """takes inputs for customer menu, validates and then passes back to customer."""
    user_str = get_input(prompt)
    if user_str in valid_inputs["customer"]:
            return user_str
    input_list =  user_str.lower().split(" ", 1)
    command = format_input(input_list[0])
    try:
        if len(input_list) != 2 or command != "order":
            raise ValueError(f"\n{'='*10}ERROR! '{user_str}' is not not a valid command! Please try again.{'='*10}\n")
    except ValueError as e:
            print(e)
            return validate_customer_inputs(prompt)
    else:
        item = input_list[1]
    try:
        stock[item]
    except KeyError:
        print(f"\n{'='*10}ERROR! '{item}' is not not on the menu! Please try again.{'='*10}\n")
        return validate_customer_inputs(prompt)
    else:
        return input_list

def stock_order_quantity(item: str) -> None:
    """Checks stock level for 'item' is >0. If so, draws the item and then calls handle_order_quantity."""
    stock_level = stock[item]["stock"]
    print("stock_level", stock_level, type(stock_level))
    if stock_level > 0:
        draw_item(item)
        handle_order_quantity(item, stock_level)
    else:
        print(f"Sorry we've run out of {item}, please choose something else.")

def handle_order_quantity(item: str, stock_level: int) -> None:
    """Takes user input and handles. If order quantity checks there is enough stock before passing to update_order_stock"""
    awaiting_amount = True
    while awaiting_amount:
        user_str = get_input("How many would you like to order: ")
        if user_str == "cancel":
            return user_str
        elif user_str == "exit":
            order.clear()
            update_cafe_data()
            sys.exit()
        else:
            try:
                new_value = decimal.Decimal(sub(r'[^\d.]', '', user_str))
            except decimal.InvalidOperation:
                print(f"\n{'='*10}ERROR! '{user_str}' is not not a valid command! Please try again.{'='*10}\n")
                return handle_order_quantity(item, stock_level)
            else:
                order_amount = int(new_value)
                if order_amount <= stock_level:
                    update_order_stock(order_amount, item)
                    awaiting_amount = False
                elif order_amount > stock_level:
                    print(f"\nSorry we only have {stock_level} left.\n")
                    print("You can either enter a new order amount, or order something else by entering 'cancel'.")
                    return handle_order_quantity(item, stock_level)

def update_order_stock(order_amount: int, item: str) -> None:
    """Updates both order and stock dictionaries before calling update_cafe_data to write changes to file."""
    print(f"\n{'-'*10}{order_amount} of {item} has been added to your order{'-'*10}\n")
    order[item] = {"price" : stock[item]["price"], "stock" : order_amount}
    stock[item]["stock"] -= order_amount
    update_cafe_data()