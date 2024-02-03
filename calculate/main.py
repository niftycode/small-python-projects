#!/usr/bin/env python3

"""
This example shows how to use operators (+, -, *, /).
It also shows how a user input can be realized with input() or a menu.
Version: 1.0
Python 3.12+
Date created: January 8th, 2024
Date modified: February 3rd, 2024
"""

import sys


def add(number_one: float, number_two: float):
    return number_one + number_two


def subtract(number_one: float, number_two: float):
    return number_one - number_two


def multiply(number_one: float, number_two: float):
    return number_one * number_two


def divide(number_one: float, number_two: float):
    return number_one / number_two


def quit_application():
    sys.exit("Goodbye!")


def menu():
    """Check the user's selection and invoke the
    appropriate function

    Returns:
        float: Result of the calculation
    """
    number1 = float(input("Enter the first number: "))
    number2 = float(input("Enter the second number: "))

    print()
    print("----------------------------------------------------------")
    print("Choose an option:")
    print()
    print("Add numbers: -1-")
    print("Subtract numbers: -2-")
    print("Multiply numbers: -3-")
    print("Divide numbers: -4-")
    print("Quit program: -q-")
    print("----------------------------------------------------------")

    while True:
        choice = input("Your choice: ")

        if choice == "1":
            result = add(number1, number2)
            break
        elif choice == "2":
            result = subtract(number1, number2)
            break
        elif choice == "3":
            result = multiply(number1, number2)
            break
        elif choice == "4":
            result = divide(number1, number2)
            break
        elif choice == "q":
            quit_application()
        else:
            print("Unknown input! Try again.")
            continue

    return result


def main():
    """Entry point"""
    rval = menu()
    print(f"Result: {rval}")


if __name__ == "__main__":
    main()
