from data.cafe_data import menu, stock, price
from .table import create_line


def owner():
    print(create_line())
    print(f"{'-'*69}")
    for x in menu:
        print(create_line(x, price[x], stock[x]))
        print(f"{'-'*69}")
