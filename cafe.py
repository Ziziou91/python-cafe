"""A simple application to practice working with dictonaties and lists.

The app simulates a cafe and the user can interact with it as either:
- The owner: view current stock level and total value, as well as production cost and value of each dish 
- A patron: order items from the menu (unless they've run out), tell the staff your finished and get your bill
"""
import sys
from src.owner import owner
from src.customer import customer
from src.user_input import handle_input
from data.cafe_data import cafe_print_str


def app() -> None:
    """Main function from where other logic is called from"""
    print(f"{'*'*69}")
    print(f"{'='*31}cafe.py{'='*31}")
    print(f"{'*'*69}\n")
    print("""Who is using this app?
        - Owner - view and amend the menu, stock, pricing ect.
        - Customer - Order items from the menu and get a bill when you're done.     
    """)
    user_str = ""
    while user_str != "owner" or "customer":
        user_str = handle_input("Type 'owner' or 'customer' to select, or 'cancel' to exit: ", "app")
        if user_str == "owner":
            owner(app)
        elif user_str == "customer":
            customer(app)
        elif user_str == "help" or user_str == "about":
            print(cafe_print_str[user_str])
        elif user_str == "exit":
            sys.exit()        

app()

print(f"\n{'*'*69}")
print(f"{'='*29}cafe.py END{'='*29}")
print(f"{'*'*69}\n")
