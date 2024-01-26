"""Logic for user inputs across the cafe app. Handles punctiation, capitalisations and plurals."""
import re
from re import sub
from decimal import Decimal
from data.cafe_data import valid_inputs

def get_input(prompt: str) -> str:
    """Simple function to return user input."""
    return input(prompt)
    
def format_input(user_input: str) -> str:
    """Checks the passed user_str is valid. If not, recursively ask the user to input again."""
    user_input = re.sub(r"[^\w\s]", "", user_input).lower().strip()
    return  user_input

def create_num_string(command_str: str, new_value: str,) -> int or float:
    """Returns a float when the input string is a price. Returns an integer when the input string is a stock count."""
    new_value = Decimal(sub(r'[^\d.]', '', new_value))
    if command_str == "price":
        return float(new_value)
    elif command_str == "stock_count" or command_str == "stock":
        return int(new_value)
    
def check_input_in_valid_inputs(user_input: str, called_from: str) -> str:
    """Checks if a given input string from app function exists in the valid input dictionary."""
    formatted_input = format_input(user_input)
    try:
        if formatted_input not in valid_inputs[called_from]:
            raise ValueError(f"\n{"="*10}ERROR! '{user_input}' is not not a valid command! Please try again.{"="*10}\n")
    except ValueError as e:
        print(e)
    return formatted_input