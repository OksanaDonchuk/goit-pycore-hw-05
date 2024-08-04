def parse_input(user_input: str) -> tuple[str, list[str]]:
    """
    Parses the input string into a command and arguments.

    :param user_input: Input string from the user.
    :return: A tuple containing the command and a list of arguments.
    """
    action, *args = user_input.split()
    action = action.strip().lower()
    return action, args