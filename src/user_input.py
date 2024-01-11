
import re

def get_input(prompt: str) -> str:
    """Simple function to return user input."""
    return input(prompt)

def validate_input(user_input: str, called_from: str = "none") -> str:
    """Checks the passed user_str is valid. If not, recursively ask the user to input again."""
    user_input_no_punc = re.sub(r"[^\w\s]", "", user_input).lower()
    # create tests for all possible "app" inputs.
    # create function to find user_str in valid_inputs. then return the key

    # try:
    #     if user_str_no_punc.lower() not in valid_inputs:
    #         raise ValueError(f"\n{"="*10}ERROR! '{user_str}' is not not a valid input! Please try again.{"="*10}\n")
    # except ValueError as e:
    #     print(e)
    #     user_str_no_punc = handle_input("\nType 'owner' or 'customer' to select, or 'cancel' to exit: ")
    return  user_input_no_punc

def handle_input(prompt: str, called_from: str = "none") -> str:
    """Calls get_input before passing to validate_str and then returns."""
    user_str = get_input(prompt)
    validated_str = validate_input(user_str, called_from)
    return validated_str

valid_inputs = {
    "app" : {
        "owner" : ["owner", "\"owner\"", "owners" , "\"owner\"", "cancel"]
    }
}