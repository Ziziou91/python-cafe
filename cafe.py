"""A simple application to practice working with dictonaties and lists.

The app simulates a cafe and the user can interact with it as either:
- The owner: view current stock level and total value, as well as production cost and value of each dish 
- A patron: order items from the menu (unless they've run out), tell the staff your finished and get your bill
"""
from src.table import create_line
from data.cafe_data import menu, stock, price

# testing
# put data in it's own file
# logic to ask if the user is a customer or the restaraunt owner
# help function
# start with owner functionality

def app():
    """Main function from where other logic is called from"""
    print("""Who is using this app?
        - Owner - view and amend the menu, stock, pricing ect.
        - Customer - Order items from the menu and get a bill when you're done.     
    """)
    user_str = get_input("Type 'owner' or 'customer' to select, or 'cancel' to exit: ")
    if user_str == "owner":
        print(user_str)
        print(create_line())
        print(f"{'-'*69}")
        for x in menu:
            print(create_line(x, price[x], stock[x]))
            print(f"{'-'*69}")

def get_input(prompt: str) -> str:
    """Simple function to return user input."""
    return input(prompt)

print(f"{'*'*69}")
print(f"{'='*31}cafe.py{'='*31}")
print(f"{'*'*69}\n")

app()

print(f"\n{'*'*69}")
print(f"{'='*29}cafe.py END{'='*29}")
print(f"{'*'*69}\n")
