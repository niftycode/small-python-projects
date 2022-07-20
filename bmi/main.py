#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
Small Python Projects for Beginners
BMI Calculator
Version: 1.0
Python 3.10+
Date created: July 16th, 2022
Date modified: July 20th, 2022
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
    weight: float = float(input("Please enter your weight (kg): "))
    height: float = float(input("Please enter your height (m): "))

    calculate_bmi(weight, height)


if __name__ == "__main__":
    main()
