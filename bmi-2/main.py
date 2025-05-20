#!/usr/bin/env python3


"""
Small Python Projects for Beginners
BMI Calculator with Exception Handling
Version: 1.0
Python 3.11+
Date created: June 19th, 2023
Date modified: December 18th, 2023
"""


def calculate_bmi(weight: float, height: float):
    """
    Calculates BMI (Body Mass Index) based on weight and height.

    Args:
        weight (float): The weight in kilograms.
        height (float): The height in meters.

    """
    bmi: float = weight / (height * height)

    if bmi < 18.5:
        print("Underweight")
    elif bmi >= 25:
        print("Overweight")
    else:
        print("Normal weight")


def main() -> None:
    """
    Entry point of this program.
    Get weight and height entered by the user,
    check whether it is a valid input and invoke calculate_bmi().
    """

    # old code
    # weight: int = float(input("Please enter your weight (kg): "))
    # height: int = float(input("Please enter your height (m): "))

    # new code (with exception handling)
    weight = None
    while weight is None:
        try:
            weight = float(input("Please enter your weight (kg): "))
        except ValueError as ex:
            print("Invalid input value!")
            print(ex)

    height = None
    while height is None:
        try:
            height = float(input("Please enter your height (m): "))
        except ValueError as ex:
            print("Invalid input value!")
            print(ex)

    calculate_bmi(weight, height)


if __name__ == "__main__":
    main()
