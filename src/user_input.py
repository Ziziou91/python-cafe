
import re

def get_input(prompt: str) -> str:
    """Simple function to return user input."""
    return input(prompt)

def handle_input(prompt: str, called_from: str = "none") -> str:
    """Calls get_input before passing to validate_str and then returns."""
    user_str = get_input(prompt)
    validated_str = validate_input(user_str, called_from, prompt)
    return validated_str

def validate_input(user_input: str, called_from: str, prompt: str) -> str:
    """Checks the passed user_str is valid. If not, recursively ask the user to input again."""
    user_input = re.sub(r"[^\w\s]", "", user_input).lower()
    user_input = find_user_input_in_valid_inputs(user_input, called_from, prompt)
    return  user_input

def find_user_input_in_valid_inputs(user_input: str, called_from: str, prompt) -> str:
    "Checks the passed user_input exists in a list under the called_from key in valid_inputs"
    valid_user_input_str = ""
    for key in valid_inputs[called_from]:
        if user_input in valid_inputs[called_from][key]:
            valid_user_input_str = key
    try:
        if  valid_user_input_str not in valid_inputs[called_from]:
            raise ValueError(f"\n{"="*10}ERROR! '{user_input}' is not not a valid input! Please try again.{"="*10}\n")
    except ValueError as e:
        print(e)
        return handle_input(prompt, called_from)
    else:
        return valid_user_input_str

valid_inputs = {
    "app" : {
        "owner" : ["owners", "owner"],
        "customer" : ["customers", "customer"],
        "cancel": ["cancel", "cancels"]
    }
}
