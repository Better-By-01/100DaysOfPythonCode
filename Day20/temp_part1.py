# Step 1: Create a Snake body
# Step 2: How to move the snake
# Step 3: Control the snake

from turtle import Turtle, Screen
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)                

starting_positions = [(0, 0), (-20, 0), (-40, 0)]

segments = []

for position in starting_positions:
    new_segment = Turtle('square')
    new_segment.color('white')
    new_segment.penup()
    new_segment.goto(position)
    segments.append(new_segment)

# My Try
# tim = Turtle('square')          # default shape 20px x 20px
# tim.color('white')
# x1 = tim.xcor()
# y1 = tim.ycor()

# tim = Turtle('square')
# tim.color('white')
# tim.setposition(x = x1-20, y = y1)

# tim = Turtle('square')
# tim.color('white')
# tim.setposition(x = x1-40, y = y1)


game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    for seg_num in range(len(segments)-1, 0, -1):       # start = 2 , stop = 0, step = -1
        new_x = segments[seg_num-1].xcor()
        new_y = segments[seg_num-1].ycor()
        segments[seg_num].goto(new_x, new_y)
    segments[0].forward(20)

screen.exitonclick()