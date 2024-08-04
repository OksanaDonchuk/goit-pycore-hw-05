from parser import parse_input
from handlers import handle_action

def print_help() -> None:
    """
    Prints a help message listing available commands and their usage.
    """
    help_message = """
    Available commands:
    - hello: Displays a greeting message.
    - add <name> <phone>: Adds a new contact with the specified name and phone number.
    - change <name> <new_phone>: Changes the phone number for an existing contact.
    - phone <name>: Shows the phone number for the specified contact.
    - all: Shows all contacts with their phone numbers.
    - close / exit / bye: Exits the program.
    """
    print(help_message)

def main() -> None:
    """
    Main function to run the assistant bot.
    """
    contacts = {}
    print("Welcome to the assistant bot!")
    print_help()
    while True:
        user_input = input("Enter a command: ")
        action, args = parse_input(user_input) 
        response = handle_action(action, args, contacts)  
        print(response)
        if action in ["close", "exit", "bye"]:  
            break

if __name__ == "__main__":
    main()