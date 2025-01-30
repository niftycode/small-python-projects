#!/usr/bin/env python3

"""
Draw a circle, a square and a pentagon
Fill the square with green color
Version: 1.0
Python 3.12+
Date created: January 29th, 2025
Date modified: -
"""

import turtle


def draw_circle():
    turtle.goto(-200, -20)
    turtle.pendown()
    turtle.circle(30)
    turtle.penup()


def draw_square():
    turtle.goto(-100, -20)
    turtle.pendown()

    # Draw a square and fill it with green color
    turtle.begin_fill()
    turtle.color("green")
    turtle.circle(30, steps=4)
    turtle.end_fill()

    turtle.penup()


def draw_pentagon():
    turtle.color("black")
    turtle.goto(0, -20)
    turtle.pendown()
    turtle.circle(30, steps=5)
    turtle.penup()


def main():
    turtle.pensize(4)
    turtle.penup()

    draw_circle()
    draw_square()
    draw_pentagon()

    turtle.hideturtle()  # make the turtle invisible
    turtle.done()


if __name__ == "__main__":
    main()
