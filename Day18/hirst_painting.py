from tkinter import W
import colorgram
import turtle as t
import random as rd

# rgb_colors = []
# dir = '/home/better-by-01/100DaysOfPythonCode/Day18/damien-hirst-spot-painting.jpg'
# colors = colorgram.extract(dir, 30)

# def rgb_values(color_rgb):
#     r = color_rgb.r
#     g = color_rgb.g
#     b = color_rgb.b
#     return (r,g,b)

# for color in colors:
#     rgb_colors.append(rgb_values(color.rgb))

# print(rgb_colors)         # just needed for extracting the colors
def random_color():
    color_list = [(212, 154, 98), (53, 107, 131), (199, 142, 34), (178, 78, 33), (116, 156, 171), (124, 79, 98), (123, 175, 157), (190, 88, 109), (12, 49, 64), (56, 39, 19), (40, 168, 128), (50, 126, 121), (199, 123, 143), (166, 21, 30), (225, 93, 78), (244, 163, 160), (38, 32, 34), (3, 25, 25), (79, 147, 169), (163, 26, 21), (19, 79, 91), (235, 166, 170), (171, 207, 190), (102, 127, 158), (163, 203, 211)]
    return rd.choice(color_list)

tim = t.Turtle()
tim.hideturtle()
tim.speed(0)
t.colormode(255)

tim.setheading(225)             # as it's starting should be b/w 180 & 270
tim.penup()
tim.forward(250)
tim.setheading(0)
for i in range(10):
    x = tim.xcor()
    y = tim.ycor()
    for j in range(10):
        color = random_color()
        print(color)
        tim.dot(20, color)
        tim.penup()
        tim.forward(50)
    tim.setposition(x, y+50)

screen = t.Screen()
screen.exitonclick()


