#!/usr/bin/env python3


"""
Small Python Projects for Beginners
BMI Calculator
Version: 1.1
Python 3.10+
Date created: July 16th, 2022
Date modified: December 18th, 2023
"""


def calculate_bmi(weight: float, height: float):
    """
    Calculates the Body Mass Index (BMI) using the given weight and height.

    Args:
        weight (float): The weight of the person in kilograms.
        height (float): The height of the person in meters.

    Returns:
        None

    Raises:
        None

    """
    bmi: float = weight / (height * height)

    if bmi < 18.5:
        print("Underweight")
    elif bmi >= 25:
        print("Overweight")
    else:
        print("Normal weight")


def main():
    """
    Entry point of this program.
    Get weight and height entered by the user and invoke calculate_bmi().
    """
    weight: float = float(input("Please enter your weight (kg): "))
    height: float = float(input("Please enter your height (m): "))

    calculate_bmi(weight, height)


if __name__ == "__main__":
    main()
