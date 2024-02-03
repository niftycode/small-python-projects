#!/usr/bin/env python3

"""
Quadratic Equation
Version: 1.0
Python 3.11
Date created: May 4th, 2023
Date modified: -
"""

import math


def quadratic_formula(a, b, c):
    """The quadratic formula helps to solve any quadratic equation.
    Here the abc formula is used.

    Args:
        a (int): a value
        b (int): b value
        c (int): c value

    Returns:
        int: x1, x2
    """
    x1 = (-b - math.sqrt(b * b - 4 * a * c)) / (2 * a)
    x2 = -b / a - x1

    return (x1, x2)


if __name__ == "__main__":
    result = quadratic_formula(2, -8, 6)
    print(result)
