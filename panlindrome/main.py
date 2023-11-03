#!/usr/bin/env python3


"""
Small Python Projects for Beginners

Palindrome: Check if a string is a palindrome. A string is a
palindrome if it reads the same forward and backward.

This example shows how to use `break` in a while loop.

Version: 1.0
Python 3.11
Date created: May 3rd, 2023
Date modified: November 3rd, 2023
"""


def main(input: str):
    """A palindrome is a word, sentence, verse, or even number
    that reads the same backward or forward. This can be checked
    using the code below.

    Args:
        input (str): A word to be checked.
    """
    low = 0
    high = len(input) - 1

    is_palindrome = True

    while low < high:
        if input[low] != input[high]:
            is_palindrome = False
            break

        low += 1
        high -= 1

    if is_palindrome:
        print(f"The word {input} is a palindrome.")
    else:
        print(f"The word {input} is not a palindrome.")


if __name__ == "__main__":
    user_input = input("Enter a string: ")
    main(user_input.lower())
