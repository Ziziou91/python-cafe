from data.cafe_data import menu, stock, price
from .table import create_line
from .user_help import user_help




# Variable to track which part of the app the user is currently in.
# Allows the app to provide contenxtual support with help and about commands
state = "main"

def owner():
    print("what would you like to do? ")
    usr_input_str = input("type here: ")
    if usr_input_str == "help":
        user_help()
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