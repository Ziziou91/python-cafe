import sys
from typing import Callable
from data.cafe_data import stock, customer_print_str
from .route_request import handle_input
from .table import draw_title, draw_stock, draw_item

order = {}

def sum_up_order() -> str:
    """simple function to sum up total value of items in order dictionary"""
    # test this works
    total = 0
    for item, item_props in order.items():
        total += item_props["price"]
    return total

def customer(app: Callable) -> None:
    """Top level 'customer' menu in cafe app. 
    Takes user input, passes to subsequent handles_customer_input and awaits next input."""
    state = "main"
    print(f"\n{draw_title('customer')}\n")
    while state == "main":
        print(customer_print_str["main"])
        usr_input_str = handle_input("Type your input here: ", "customer")
        handle_customer_input(usr_input_str, app)

def handle_customer_input(user_input: str, app: Callable) -> None:
    """Handles user_input, and calls customer functionality."""
    if user_input == "menu":
        draw_stock(stock)
    elif user_input == "back":
        app()
    elif user_input == "exit":
        sys.exit()
    elif user_input == "bill":
        draw_stock(order)
    elif user_input == "pay":
        total = sum_up_order()
        print(f"\nYou owe £{total}.'n")
    elif user_input[0] == "order":
        process_customer_order(user_input[1])

def process_customer_order(item: str) -> None:
    """Handles order customer orders, checks item is in stock and adds to order dictionary."""
    stock_level = stock[item]["stock"]
    if stock_level > 0:
        draw_item(item)
        awaiting_amount = True
        while awaiting_amount:
            order_amount = handle_input("How many would you like to order: ", "customer_order_count")
            if order_amount == "cancel":
                awaiting_amount = False
            elif order_amount <= stock_level:
                print(f"\n{'-'*10}{order_amount} of {item} has been added to your order{'-'*10}\n")
                order[item] = {"price" : stock[item]["price"], "stock" : order_amount}
                stock[item]["stock"] -= order_amount
                awaiting_amount = False
            elif order_amount > stock_level:
                print(f"\nSorry we only have {stock_level} left.\n")
                print("You can either amend your order amount with 'order x', or order something else by entering 'cancel'.")
                order_amount = handle_input("How many would you like to order: ", "customer_order_count")
    else:
        print(f"sorry we've run out of {item}, please choose something else.")
