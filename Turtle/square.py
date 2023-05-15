#!/usr/bin/env python3


"""
Small Python Projects for Beginners
Turtle exampe: Draw a square

Version: 1.0
Python 3.11
Date created: May 15th, 2023
Date modified: -
"""

import turtle

my_turtle = turtle.Turtle()

for i in range(4):
    my_turtle.forward(100)
    my_turtle.right(90)

turtle.done()
