#!/usr/bin/env python3


"""
Small Python Projects for Beginners
BMI Calculator with Exception Handling
Version: 1.0
Python 3.11+
Date created: June 19th, 2023
Date modified: -
"""


def calculate_bmi(weight: float, height: float):
    bmi: float = weight / (height * height)

    if bmi < 18.5:
        print("Underweight")
    elif bmi >= 25:
        print("Overweight")
    else:
        print("Normal weight")


def main():
    # old code
    # weight: int = float(input("Please enter your weight (kg): "))
    # height: int = float(input("Please enter your height (m): "))

    # new code (with exception handling)
    weight = None
    while weight is None:
        try:
            weight = float(input("Please enter your weight (kg): "))
        except ValueError as err:
            print("Invalid input value!")
            print(err)

    height = None
    while height is None:
        try:
            height = float(input("Please enter your height (m): "))
        except ValueError as err:
            print("Invalid input value!")
            print(err)

    calculate_bmi(weight, height)


if __name__ == "__main__":
    main()
