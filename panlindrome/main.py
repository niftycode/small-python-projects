#!/usr/bin/env python3


"""
Small Python Projects for Beginners

Palindrome: Check if a string is a palindrome. A string is a
palindrome if it reads the same forward and backward.

This example shows how to use `break` in a while loop.

Version: 1.0
Python 3.11
Date created: May 3rd, 2023
Date modified: November 17th, 2023
"""


def main(input: str):
    """A palindrome is a word, sentence, verse, or even number
    that reads the same backward or forward.

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

"""
2nd example:
We can use a list to test whether it is a palindrome.

a_string = input("Enter a string: ")
a_string = str_1.casefold()

reversed_string = reversed(a_string)

if list(a_string) == list(reversed_string):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
"""
