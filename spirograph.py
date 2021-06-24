import turtle as t
from turtle import Screen
import random

turtle = t.Turtle()

t.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


for circle in range(72):
    turtle.speed(0)
    turtle.color(random_color())
    turtle.circle(100)
    turtle.right(5)
my_screen = Screen()
my_screen.exitonclick()
