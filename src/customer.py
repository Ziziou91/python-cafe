import sys
from typing import Callable
from data.cafe_data import stock, customer_print_str
from src.user_input import handle_input
from .table import draw_title, draw_stock, draw_item

order = {}

def customer(app: Callable) -> None:
    """top level 'customer' menu in cafe app. 
    Routes user to desired functionality, or prints additional info in terminal."""
    state = "main"
    print(f"\n{draw_title('customer')}\n")
    while state == "main":
        print(customer_print_str["main"])
        usr_input_str = handle_input("Type your input here: ", "customer")
        handle_customer_input(usr_input_str, app, customer)

def handle_customer_input(user_input, app, customer: Callable):
    if user_input == "menu":
        # don't print stock value
        # print out of stock instead of 0
        draw_stock()
    elif user_input == "back":
        app()
    elif user_input == "exit":
        sys.exit()
    elif user_input == "bill":
        # develop this into a menu
        print(f"\n{order}\n")
    elif user_input[0] == "order":
        process_customer_order(user_input[1], app, customer)

def process_customer_order(item, app, customer: Callable):
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
                order[item] = {"price" : stock[item]["price"], "order_count" : order_amount}
                # update stock level to remove the ordered items
                awaiting_amount = False
            elif order_amount > stock_level:
                print(f"\nSorry we only have {stock_level} left.\n")
                print("You can either amend your order amount with 'order x', or order something else by entering 'cancel'.")
                order_amount = handle_input("How many would you like to order: ", "customer_order_count")

            # elif order_amount > stock_level:
# 
            #     while order_amount > stock_level and order_amount != "cancel":
            #         print(f"\nsorry we only have {stock_level} left.")
            #         print("""here are the following commands available:
            #             * order x - where x is the amount you'd like to order
            #             * cancel - go back to the previous page
            #             """)
            #         # FIX - needs a value to store it as. Check if it's a number or string
            #         # if number, set to order_amount, if string check it's cancel.
            #         order_amount = handle_input("How many would you like to order: ", "stock_count")
            #     print("order_amount", order_amount, "yay you got out of the while loop")
            #     if order_amount == "cancel":
            #         customer()

            # check there is enough in stock to satisfy order. if not, ask again
            # add amount to order dictionary, update stock
            # should be able to cancel, thereby getting out of while loop 
    else:
        print(f"sorry we've run out of {item}, please choose something else.")



def sum_up_order():
    pass           

        
