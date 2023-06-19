#!/usr/bin/env python3


"""
Small Python Projects for Beginners
BMI Calculator with exception handling in a seperate module
Version: 1.0
Python 3.11+
Date created: June 19th, 2023
Date modified: -
"""

import get_values


def calculate_bmi(weight: float, height: float):
    bmi: float = weight / (height * height)

    if bmi < 18.5:
        print("Underweight")
    elif bmi >= 25:
        print("Overweight")
    else:
        print("Normal weight")


def main():
    weight, height = get_values.get_values()

    calculate_bmi(weight, height)


if __name__ == "__main__":
    main()
