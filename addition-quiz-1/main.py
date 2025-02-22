#!/usr/bin/env python3


"""
Small Python Projects for Beginners

Addition Quiz: The user can enter a new answer until it is correct.
This program has no exception handling. So when the user types a letter, the program crashes.

Version: 1.2
Python 3.12+
Date created: April 22nd, 2023
Date modified: February, 22nd, 2025
"""

import random


def main():
    # Generate a random integer between 0 and 90
    number1 = random.randint(0, 90)
    number2 = random.randint(0, 90)

    result = number1 + number2

    answer = int(input(f"What is {number1} + {number2}? "))

    while result != answer:
        print("Wrong!")
        answer = int(input(f"What is {number1} + {number2}? "))

    print(f"Yes, {number1} + {number2} is {result}.")


if __name__ == "__main__":
    main()
