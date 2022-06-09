import turtle as t
import random as rd

from matplotlib.pyplot import draw

tim = t.Turtle()
t.colormode(255)
tim.speed("fastest")

def random_color():
    r = rd.randint(0,255)
    g = rd.randint(0,255)
    b = rd.randint(0,255)
    return (r,g,b)

def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)

draw_spirograph(5)

screen = t.Screen()
screen.exitonclick()