import re
from data.cafe_data import order
from data.cafe_data import stock, customer_print_str, valid_inputs, order, cafe_print_str, owner_print_str

def sum_up_order() -> str:
    """simple function to sum up total value of items in order dictionary"""
    # test this works
    total = 0
    for item, item_props in order.items():
        total += item_props["price"]
    return total

def get_input(prompt: str) -> str:
    """Simple function to return user input."""
    return input(prompt)
    
def format_input(user_input: str) -> str:
    """Checks the passed user_str is valid. If not, recursively ask the user to input again."""
    user_input = re.sub(r"[^\w\s]", "", user_input).lower().strip()
    return  user_input

def update_cafe_data():
    cafe_data_string = f'"""module to store cafe stock """\nstock={stock}\n\nvalid_inputs={valid_inputs}\n\ncafe_print_str={cafe_print_str}\n\nowner_print_str={owner_print_str}\n\ncustomer_print_str={customer_print_str}\n\norder={order}'
    with open("data/cafe_data.py", 'w', encoding='UTF-8') as f:
        f.write(cafe_data_string)