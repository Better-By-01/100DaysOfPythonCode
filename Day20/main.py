from asyncio.constants import SSL_HANDSHAKE_TIMEOUT
from turtle import Screen
from snake import Snake
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()

screen.listen()


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()
    screen.onkey(fun=snake.up, key="Up")            # WARNING: up not up()
    screen.onkey(fun=snake.down, key="Down")
    screen.onkey(fun=snake.left, key="Left")
    screen.onkey(fun=snake.right, key="Right")

    

screen.exitonclick()