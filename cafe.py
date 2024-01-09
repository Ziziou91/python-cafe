"""A simple application to practice working with dictonaties and lists.

The app simulates a cafe and the user can interact with it as either:
- The owner: view current stock level and total value, as well as production cost and value of each dish 
- A patron: order items from the menu (unless they've run out), tell the staff your finished and get your bill
"""
import math

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
def calc_stock_value(price:float, stock:int) -> float:
    if price == "Price":
        return "Stock Value"
    else:
        return stock * price

def create_cell(item:str, cell_width:int) -> str:
    spacing = cell_width - (len(str(item)) / 2)
    if spacing.is_integer():
        return f"{' '*int(spacing)}{item}{' '*int(spacing)}"
    else:
        return f"{' '*int(math.ceil(spacing))}{item}{' '*int(math.floor(spacing))}"

def create_line(item:str="Item", price:float="Price", stock:int="Stock") -> str:
    item_cell = create_cell(item, 8)
    price_cell = create_cell(price, 8)
    stock_cell = create_cell(stock, 8)
    stock_value = create_cell(calc_stock_value(price, stock), 8)
    return f"|{item_cell}|{price_cell}|{stock_cell}|{stock_value}|"

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