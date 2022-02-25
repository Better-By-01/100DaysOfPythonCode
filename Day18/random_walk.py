import turtle as t
import random as rd

tim = t.Turtle()
tim.width(15)
tim.speed("fastest")

# colours = ["CornFlowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

# now using a tuple and r,g,b
t.colormode(255)

def random_color():
    r = rd.randint(0,255)
    g = rd.randint(0,255)
    b = rd.randint(0,255)
    return (r,g,b)                               # a tupple returned

directions = [0, 90, 180, 270]



for i in range(100):
    tim.color(random_color())                    # tim.color(rd.choice(colours))
    tim.forward(30)
    tim.setheading(rd.choice(directions))

screen = t.Screen()
screen.exitonclick()


# Tuple (a datatype in python) whose values can't be changed like a list
# (1,3,8)
# They are immutable

# my_tuple = (1, 3, 8)
# print(my_tuple[0])

# if tuple needed to be changed convert it into a list
# list(my_tuple)                # [1,3,8]

