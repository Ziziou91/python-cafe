from .user_input import get_input, create_num_string, check_input_in_valid_inputs
from .owner_requests import route_owner_requests
# from .customer_requests import route_customer_requests

def handle_input(prompt: str, called_from: str = "none") -> str:
    """Calls get_input before passing to appropiate handler function and then returns."""
    #seperate into owner and customer functionality
    customer_requests = ["customer", "customer_order_count"]
    owner_requests = ["owner", "owner_stock", "owner_product", "amend_menu"]
    user_str = get_input(prompt)
    if called_from == "price" or called_from == "stock_count":
        return create_num_string(called_from, user_str)
    else:
        if called_from == "app":
            return check_input_in_valid_inputs(user_str, called_from)
        elif called_from in owner_requests:
            return route_owner_requests(user_str, prompt, called_from, handle_input)
        elif called_from in customer_requests:
            # return route_customer_requests(user_str, prompt, called_from, handle_input)
            pass