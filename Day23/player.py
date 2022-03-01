from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)
    
    def move(self):
        """Moves the player upward"""
        self.forward(MOVE_DISTANCE)

    def go_to_start(self):
        """Sends back the player to it's starting position"""
        self.goto(STARTING_POSITION)



