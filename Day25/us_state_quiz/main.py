from turtle import Turtle, Screen
import turtle
import pandas


screen = Screen()
screen.title("U.S. State Quiz")

image = "./Day25/us_state_quiz/blank_states_img.gif"
screen.setup(width=750, height=550)
screen.addshape(image)
turtle.shape(image)



# FOR OBTAINING THE LAT AND LON OF DIFF. STATES
# def get_mouse_click_coor(x,y):
#     print(x,y)

# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()

data = pandas.read_csv("./Day25/us_state_quiz/50_states.csv")
states_list = data["state"].to_list() 

game_is_on = True
correct_guess = [] 

while game_is_on:
    t = Turtle()
    t.hideturtle()
    t.penup()
    guess = screen.textinput(title=f"{len(correct_guess)}/50 States Correct", 
                              prompt="What's another state's name?").title()
    if guess == "Exit":

        # states to learn.csv
        missing_states = []
        for state in states_list:
            if state not in correct_guess:
                missing_states.append(state)

        # df = pandas.DataFrame(missing_states)                 # dataframe can directly be created from this and saved to .csv

        missing_states_dict = {}
        missing_states_dict["states missed"] = missing_states
        df = pandas.DataFrame(missing_states_dict)
        df.to_csv("./Day25/us_state_quiz/missed_states.csv")

        break

    if (guess in states_list) and (guess not in correct_guess):
        correct_guess.append(guess)
        state_info = data[data["state"] == guess]
        t.goto(x = int(state_info['x']), y = int(state_info['y']))
        t.write(state_info["state"].item(), font=('Arial', 12, "bold"))                   # use of item, here I faced program 
    
    if guess not in data["state"].to_list() or len(correct_guess) > 50: 
        game_is_on = False

screen.exitonclick()

