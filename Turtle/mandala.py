#!/usr/bin/env python3 
import turtle

# Initial setup
screen = turtle.Screen()
screen.bgcolor("white")
mandala = turtle.Turtle()
mandala.speed(0)

# Function to draw a circle
def draw_circle(color, radius, x, y):
    mandala.penup()
    mandala.color(color)
    mandala.goto(x, y)
    mandala.pendown()
    mandala.circle(radius)

# Draw mandala pattern
colors = ["red", "blue", "green", "yellow", "white", "orange"]
radius = 50

for i in range(6):
    draw_circle(colors[i], radius, 0, 0)
    mandala.right(70)

# Finish drawing
mandala.hideturtle()
turtle.done()
