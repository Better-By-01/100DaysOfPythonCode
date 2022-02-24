################################### OOPS ###############################
# classes and objects
# name of class is given in pascal case (like CarBlueprint < no underscore > )

# Object = Class  
# car    = CarBlueprint()

import turtle
from prettytable import PrettyTable

obj_timmy = turtle.Turtle()
# print(obj_timmy)
# <turtle.Turtle object at 0x7f80d69239a0>
obj_timmy.shape("turtle")
obj_timmy.color("coral")
obj_timmy.forward(100)

my_screen = turtle.Screen()
print(my_screen.canvheight) # 300 

my_screen.exitonclick()

# A package is someone's entire code

table = PrettyTable()
table.field_names = ["Pokemon Name", "Type"]
table.add_rows(
    [
        ["Pikachu", "Electric"],
        ["Squirtle", "Water"],
        ["Charmander", "Fire"],
    ]
)
table.align = "l"
print(table)