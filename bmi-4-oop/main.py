#!/usr/bin/env python3


"""
Small Python Projects for Beginners
This code is a simple BMI calculator using OOP principles.
It defines a BMI class with methods to calculate BMI and determine the category.
Version: 1.0
Python 3.13+
Date created: May 20th, 2025
Date modified: -
"""


class BMI:
    """
    A class to represent a Body Mass Index (BMI) calculator.
    Attributes:
        weight (float): The weight of the person in kilograms.
        height (float): The height of the person in meters.
    """

    def __init__(self, weight: float, height: float):
        self.weight = weight
        self.height = height

    def calculate(self) -> float:
        """
        Calculates the Body Mass Index (BMI) using the formula:
        BMI = weight / (height * height)

        Returns:
            float: The calculated BMI value.
        """
        return self.weight / (self.height * self.height)

    def category(self) -> str:
        """
        Determines the BMI category based on the calculated BMI value.

        Returns:
            str: The BMI category as a string.
        """
        bmi_value = self.calculate()
        if bmi_value < 18.5:
            return "Underweight"
        elif bmi_value >= 25:
            return "Overweight"
        else:
            return "Normal weight"


def main() -> None:
    """
    The main function collects user input and creates
    an instance of the BMI class to perform the calculations.
    """
    weight = float(input("Enter your weight in kg: "))
    height = float(input("Enter your height in meters: "))

    bmi = BMI(weight, height)
    print(f"Your BMI is: {bmi.calculate():.2f}")
    print(f"Category: {bmi.category()}")


if __name__ == "__main__":
    main()
