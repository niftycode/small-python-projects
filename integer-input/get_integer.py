#!/usr/bin/env python3


def get_integer(prompt: str, error_message: str = "") -> int:
    """Ask for an integer and check if the input value is an integer.

    Args:
        prompt (str): integer value
        error_message (str, optional):
        Show error message if the input value is not an integer.
        Defaults to "".

    Returns:
        int: input value
    """
    while True:
        try:
            return int(input(prompt))
        except ValueError as ex:
            print(ex)
            print(error_message)
