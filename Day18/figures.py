from turtle import Turtle, Screen               
from random import choice

# from turtle import *              # not a good practice to use it

# aliasing module name
# import turtle as t

tim = Turtle()
tim.width(4)
tim.speed(0)

sides = [3, 4, 5, 6, 7, 8, 9, 10]
colors = ["cyan", "spring green", "lime", "deep sky blue", "red", "yellow", "dark orange", "blue", "pink", "violet"]


for side in sides:
    angle = 360/side
    tim.color(choice(colors))
    while side > 0:
        tim.forward(100)
        tim.right(angle)
        side -= 1

screen = Screen()
screen.exitonclick()

