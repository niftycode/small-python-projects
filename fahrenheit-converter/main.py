#!/usr/bin/env python3


"""
Small Python Projects for Beginners
Convert Fahrenheit to Celsius
Version: 1.0
Python 3.10+
Date created: July 26th, 2022
Date modified: -
"""


def convert(fahrenheit: str):
    try:
        celsius = (float(fahrenheit) - 32.0) * 5.0 / 9.0
        print(f"{celsius} degree Celsius")
    except ValueError as e:
        print(e)


def main():
    fahrenheit: str = input("Enter Fahrenheit temperature: ")

    convert(fahrenheit)


if __name__ == "__main__":
    main()
