#!/usr/bin/env python3

"""
Calculate the distance between two points

Version: 1.0
Python 3.12
Date created: December 10th, 2023
Date modified: -
"""


def calculate_distance(x1: float, y1: float, x2: float, y2: float) -> float:
    distance: float = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    return distance


def main():
    point_x1: float = float(input("Enter x1 value: "))
    point_y1: float = float(input("Enter y1 value: "))

    point_x2: float = float(input("Enter x2 value: "))
    point_y2: float = float(input("Enter y2 value: "))

    rval: float = calculate_distance(point_x1, point_y1, point_x2, point_y2)

    print(rval)


if __name__ == "__main__":
    main()
