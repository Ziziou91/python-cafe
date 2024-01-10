
import re

def get_input(prompt: str) -> str:
    """Simple function to return user input."""
    return input(prompt)

def validate_input(user_str: str) -> str:
    """Checks the passed user_str is valid. If not, recursively ask the user to input again."""
    valid_inputs = ["letters", "letter", "words", "word", "cancel"]
    #sanitise the input
    user_str_no_punc = re.sub(r"[^\w\s]", "", user_str).lower()
    #check input is in valid_inputs
    try:
        if user_str_no_punc.lower() not in valid_inputs:
            raise ValueError(f"\n{"="*10}ERROR! '{user_str}' is not not a valid input! Please try again.{"="*10}\n")
    except ValueError as e:
        print(e)
        user_str_no_punc = handle_method_input("\nType 'letters' or 'words' to select, or 'cancel' to exit: ")
    return user_str_no_punc

def handle_method_input(prompt: str) -> str:
    """Calls get_input before passing to validate_str and then returns."""
    user_str = get_input(prompt)
    validated_str = validate_input(user_str)
    return validated_str