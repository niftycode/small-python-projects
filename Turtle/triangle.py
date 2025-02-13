#!/usr/bin/env python3

"""
Draw a triangle
Version: 1.0
Python 3.12+
Date created: February 1st, 2025
Date modified: -
"""


import turtle
import math


def draw_triangle(point_1, point_2, point_3, angle_a, angle_b, angle_c):
    turtle.goto(point_1)
    turtle.pendown()
    turtle.goto(point_2)
    turtle.color("red")
    turtle.write(f"{angle_b:.2f}°", font=("Arial", 24, "normal"))
    turtle.color("black")
    turtle.goto(point_3)
    turtle.color("red")
    turtle.write(f"{angle_c:.2f}°", font=("Arial", 24, "normal"))
    turtle.color("black")
    turtle.goto(point_1)
    turtle.color("red")
    turtle.write(f"{angle_a:.2f}°", font=("Arial", 24, "normal"))
    turtle.penup()


def calculate_angle(p1, p2, p3):
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3

    a = math.sqrt((x2 - x3) * (x2 - x3) + (y2 - y3) * (y2 - y3))
    b = math.sqrt((x1 - x3) * (x1 - x3) + (y1 - y3) * (y1 - y3))
    c = math.sqrt((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2))

    angle_a = math.degrees(math.acos((b * b + c * c - a * a) / (2 * b * c)))
    angle_b = math.degrees(math.acos((a * a + c * c - b * b) / (2 * a * c)))
    angle_c = math.degrees(math.acos((a * a + b * b - c * c) / (2 * a * b)))

    return angle_a, angle_b, angle_c


def main():
    turtle.pensize(4)
    turtle.penup()

    point_1 = (-180, -20)
    point_2 = (100, -80)
    point_3 = (0, 70)

    angle_a, angle_b, angle_c = calculate_angle(point_1, point_2, point_3)

    draw_triangle(point_1, point_2, point_3, angle_a, angle_b, angle_c)

    turtle.hideturtle()
    turtle.done()


if __name__ == "__main__":
    main()
