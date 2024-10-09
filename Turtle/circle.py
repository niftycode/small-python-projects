#!/usr/bin/env python3


"""
Small Python Projects for Beginners
Turtle exampe: Draw a circle

Version: 1.0
Python 3.13
Date created: October 9th, 2024
Date modified: -
"""

import turtle


def draw_circle(x: float, y: float, r: float) -> None:
    """
    Draw a circle

    Args:
        x (float): x-coordinate
        y (float): y-coordinate
        r (float): radius
    """
    window = turtle.Screen()
    window.bgcolor("yellow")

    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.circle(r)

    turtle.hideturtle()
    turtle.done

    window.mainloop()


def main():
    """
    Enter x-, y-coordinates and radius and
    invoke draw_circle() function.
    """
    x: float = float(input("Enter the center x-coordinate: "))
    y: float = float(input("Enter the center y-coordinate: "))
    radius: float = float(input("Enter the radius: "))
    draw_circle(x, y, radius)


if __name__ == "__main__":
    main()
