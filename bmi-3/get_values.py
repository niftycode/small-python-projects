#!/usr/bin/env python3

def get_values() -> tuple:
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

    return weight, height
