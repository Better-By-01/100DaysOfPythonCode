from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forwards():
    tim.forward(100)

screen.listen()                             # to start listening for events

# Turtle Event Listeners
screen.onkey(fun = move_forwards, key = "space")        # remember to write the fun. name only 
                                                        # similar to any < def function_b(function_a): > 
                                                        # def calculator (n1, n2, func): func(n1,n2)            # fun may be of multiply, add, ...
# idea of higher order function -> a function that can work with other functions. (like calculator act as higher order function)

screen.exitonclick()


# state of any object
# state of timmy ( an object ) color attribute is green
# state of tommy ( an object ) color attribute is purple

# they have different states in terms of their attribute or their appearence
# they may differ in states based on what they are doing like when timmy is moving tommy remains stationary