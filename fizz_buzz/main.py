#!/usr/bin/env python3


"""
Small Python Projects for Beginners
FizzBuzz - Let's take a look at the rules:

* If a number is divisible by 3, print the word 'Fizz' instead of the number.
* If the number is divisible by 5, print the word 'Buzz' instead of the number.
* Finally, if the number is divisible by both 3 and 5, print 'FizzBuzz' instead of the number.
* Otherwise, just print the number.

Version: 1.0
Python 3.12
Date created: February 19th, 2024
Date modified: -
"""


def check_number(number: int):

    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(f"{number}")


def main():
    try:
        number = int(input("Enter a number: "))
        check_number(number)
    except ValueError as e:
        print(e)
        print("Invalid input! Please enter a valid number.")


if __name__ == "__main__":
    main()
