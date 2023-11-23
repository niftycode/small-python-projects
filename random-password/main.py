#!/usr/bin/env python3

"""
Create random passwords in Python
Version: 1.1
Python 3.12
Date created: November 20th, 2023
Date modified: November 23rd, 2023
"""

import random

lower_case_letters = list("abcdefghijklmnopqrstuvwxyz")
upper_case_letters = list("ABCDEFGHJKLMNPQRSTUVWXYZ")
numbers = list("0123456789")
special_characters = list("#!%&$()[]{}=-_+*;:.")

password_characters = (
    lower_case_letters + upper_case_letters + numbers + special_characters
)


def password_generator(length=8):
    """A generator to shuffle the characters and to create a random pssword.

    Args:
        length (int, optional): Generates a random password
        having the specified length. Defaults to 8.

    Returns:
        str: password
    """
    # shuffle characters
    random.shuffle(password_characters)

    # generate random password and convert to string
    random_password = random.choices(password_characters, k=length)
    random_password = "".join(random_password)
    return random_password


my_password = password_generator(14)
print(my_password)
