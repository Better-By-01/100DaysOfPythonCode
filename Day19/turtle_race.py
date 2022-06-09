from tkinter import W
from turtle import Turtle, Screen
import random as rd

screen = Screen()

is_race_on = False
# setting up the screen size pixel wise
screen.setup(width = 500, height = 400)

# Making a bet through pop-up window
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

# Making turtles goto the start of the race
turtles = []
ycor = -130 

for i in range(6):
    tim = Turtle(shape = "turtle")
    tim.color(colors[i])
    tim.penup()
    tim.goto(x = -230, y = ycor)
    turtles.append(tim)
    ycor += 50

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")

        random_distance = rd.randint(0,10)
        turtle.forward(random_distance)
        

screen.exitonclick()