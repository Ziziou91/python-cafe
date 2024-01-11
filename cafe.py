"""A simple application to practice working with dictonaties and lists.

The app simulates a cafe and the user can interact with it as either:
- The owner: view current stock level and total value, as well as production cost and value of each dish 
- A patron: order items from the menu (unless they've run out), tell the staff your finished and get your bill
"""
from src.owner import owner
from src.user_input import handle_input
# testing
# put data in it's own file
# logic to ask if the user is a customer or the restaraunt owner
# help function
# start with owner functionality

def app() -> None:
    """Main function from where other logic is called from"""
    print("""Who is using this app?
        - Owner - view and amend the menu, stock, pricing ect.
        - Customer - Order items from the menu and get a bill when you're done.     
    """)
    user_str = handle_input("Type 'owner' or 'customer' to select, or 'cancel' to exit: ", "app")
    if user_str == "owner":
        owner()


print(f"{'*'*69}")
print(f"{'='*31}cafe.py{'='*31}")
print(f"{'*'*69}\n")

app()

print(f"\n{'*'*69}")
print(f"{'='*29}cafe.py END{'='*29}")
print(f"{'*'*69}\n")