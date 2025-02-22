#!/usr/bin/env python3


"""
Small Python Projects for Beginners

Addition Quiz: The user can enter a new answer until it is correct.
This example has exception handling for invalid input. In addition,
the addition was encapsulated in a function.

Version: 1.0
Python 3.12+
Date created: February 22nd, 2025
Date modified: -
"""

import random


def addition(number1: int, number2: int) -> int:
    return number1 + number2


def main():
    # Generate a random integer between 0 and 90
    number1 = random.randint(0, 90)
    number2 = random.randint(0, 90)

    try:
        answer = int(input(f"What is {number1} + {number2}? "))
    except ValueError as ex:
        print(ex)
        print("Invalid input. Please enter a number.")
        return

    result = addition(number1, number2)

    while result != answer:
        print("Wrong!")
        answer = int(input(f"What is {number1} + {number2}? "))
    print(f"Yes, {number1} + {number2} is {result}.")
    return


if __name__ == "__main__":
    main()
