from contacts import add_contact, change_contact, show_phone, show_all

def handle_action(action: str, args: list[str], contacts: dict[str, str]) -> str:
    """
    Handles the action by calling the appropriate function using match...case.

    :param action: The command to execute.
    :param args: The arguments for the action.
    :param contacts: The dictionary of contacts.
    :return: The response string after executing the command.
    """
    match action:
        case "hello":
            return "How can I help you?"
        case "add":
            return add_contact(args, contacts)
        case "change":
            return change_contact(args, contacts)
        case "phone":
            return show_phone(args, contacts)
        case "all":
            return show_all(contacts)
        case "close" | "exit" | "bye":
            return "Good bye!"
        case _:
            return "Invalid command."