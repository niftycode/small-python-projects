#!/usr/bin/env python3

"""
Volume of a Box Calculator
Formula: length * width * height

This code example shows how to calculate the volume of a box.
The formula for the calculation is very simple and therefore
does not matter much. Rather, it comes down to the following:

-   Input of data by the user
-   Exception handling
-   Using a Class (object-oriented programming)


Version: 1.1
Python 3.12
Date created: March 17th, 2023
Date modified: November 22nd, 2023
"""

import sys


class BoxCalculator:
    """
    Class BoxCalculator

    A class that represents a box calculator with dimensions of length, width, and height.

    Attributes:
        length (int): The length of the box.
        width (int): The width of the box.
        height (int): The height of the box.

    Methods:
        __init__(self, length: int, width: int, height: int) -> None:
            Initializes a new instance of the BoxCalculator class.

        calculate_volume(self) -> int:
            Calculates the volume of the box using the formula length * width * height.

        __repr__(self)
            Returns a string representation of the BoxCalculator object.

    """

    def __init__(self, length: int, width: int, height: int) -> None:
        self.length = length
        self.width = width
        self.height = height

    @property
    def length(self):
        return self.__length

    @length.setter
    def length(self, length):
        self.__length = length

    def __repr__(self):
        return (
            f"{self.__class__.__name__}"
            f"({self.length}, "
            f"{self.width}, "
            f"{self.height})"
        )

    def calculate_volume(self) -> int:
        return self.length * self.width * self.height


def main():
    """ """
    length = input("Enter the length: ")
    width = input("Enter the width: ")
    height = input("Enter the height: ")

    try:
        box_calculator = BoxCalculator(int(length), int(width), int(height))
    except Exception as ex:
        print(f"Wrong type! {ex}")
        sys.exit()

    volume = box_calculator.calculate_volume()
    print(f"The volume is: {volume}")


if __name__ == "__main__":
    main()
