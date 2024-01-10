"""A simple application to practice working with dictonaties and lists.

The app simulates a cafe and the user can interact with it as either:
- The owner: view current stock level and total value, as well as production cost and value of each dish 
- A patron: order items from the menu (unless they've run out), tell the staff your finished and get your bill
"""
from src.table import create_line

menu = ["Pasta", "Sandwich", "Baked potato", "Chips", "Coffee", "Tea"]

stock = {
    "Pasta" : 5,
    "Sandwich": 2,
    "Baked potato": 3,
    "Chips": 0,
    "Coffee": 10,
    "Tea": 7
}

price = {
    "Pasta" : 5.00,
    "Sandwich": 4.50,
    "Baked potato": 4.50,
    "Chips": 2.50,
    "Coffee": 2.00,
    "Tea": 1.50
}

def app():
    print(create_line())
    print(f"{'-'*69}")
    for x in menu:
        print(create_line(x, price[x], stock[x]))
        print(f"{'-'*69}")


print(f"{'*'*69}")
print(f"{'='*31}cafe.py{'='*31}")
print(f"{'*'*69}\n")

app()

print(f"\n{'*'*69}")
print(f"{'='*29}cafe.py END{'='*29}")
print(f"{'*'*69}\n")