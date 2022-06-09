import time
from turtle import Screen
from player import Player
from carmanager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
carmanager = CarManager()

screen.listen()
screen.onkey(fun=player.move, key="Up")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    carmanager.create_car()
    carmanager.move_cars()

    # Detect collision with car
    for car in carmanager.all_cars:
        if car.distance(player) < 20:
            scoreboard.game_over()
            game_is_on = False

    # Detect collision with wall
    if (player.ycor() > 280):
        scoreboard.level_up()
        carmanager.speed_up()
        player.go_to_start()
    

screen.exitonclick()
