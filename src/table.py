"""The logic to produce a table of enu items, prices, stock and stock value."""
import math

def calc_stock_value(price:float, stock:int) -> float:
    """Calculates the total value of stock. If not args then returns default string."""
    if price == "Price":
        return "Stock Value"
    else:
        return stock * price

def create_cell(item:str, cell_width:int) -> str:
    """Creates each cell to populate a table of values generated by create_line."""
    spacing = cell_width - (len(str(item)) / 2)
    if spacing.is_integer():
        return f"{' '*int(spacing)}{item}{' '*int(spacing)}"
    else:
        return f"{' '*int(math.ceil(spacing))}{item}{' '*int(math.floor(spacing))}"

def create_line(item:str="Item", price:float="Price", stock:int="Stock") -> str:
    """Creates each line in a table of menu items, prices, stock and stock value."""
    item_cell = create_cell(item, 8)
    price_cell = create_cell(price, 8)
    stock_cell = create_cell(stock, 8)
    stock_value = create_cell(calc_stock_value(price, stock), 8)
    return f"|{item_cell}|{price_cell}|{stock_cell}|{stock_value}|"

def draw_user(user:str):
    """draws a box to confirm if the user is using the app as either 'owner' or 'customer'"""
    if user == "owner":
        return f"{'-'*24}\n|{' '*22}|\n|{' '*9}Owner{' '*8}|\n|{' '*22}|\n{'-'*24}"
    elif user == "customer":
        return f"{'-'*24}\n|{' '*22}|\n|{' '*7}Customer{' '*7}|\n|{' '*22}|\n{'-'*24}"
