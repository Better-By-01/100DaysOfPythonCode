from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time
import math


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(fun=r_paddle.move_up, key="Up")
screen.onkey(fun=r_paddle.move_down, key="Down")
screen.onkey(fun=l_paddle.move_up, key="w")
screen.onkey(fun=l_paddle.move_down, key="s")


game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()

    ball.move()

    # Collision detection with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        # needs to bounce
        ball.bounce_y()
    
    # Collision detection with paddle
    # if r_paddle.distance(ball) < 15:      if the ball hits the edge of the paddle the distance will be too much than 15

    distance_max = round(math.sqrt(pow(50,2) + pow(20,2)))

    if ball.distance(r_paddle) < distance_max and ball.xcor() > 320:
        ball.bounce_x()
        scoreboard.r_point()
        scoreboard.update_scoreboard()
        
    if ball.distance(l_paddle) < distance_max and ball.xcor() < -320:
        ball.bounce_x()
        scoreboard.l_point()
        scoreboard.update_scoreboard()
    
    # out of bound detection of ball for R paddle 
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()
        scoreboard.update_scoreboard()

    # out of bound detection of ball for L paddle 
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()
        scoreboard.update_scoreboard()
    

screen.exitonclick()