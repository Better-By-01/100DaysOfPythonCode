from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")
file_path = "/home/better-by-01/100DaysOfPythonCode/Day21/snake_game/data.txt"

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        with open(file_path, mode="r") as data:
            self.highscore = int(data.read())
        self.goto(0, 260)
        self.update_scoreboard()
        self.hideturtle()
    
    def update_scoreboard(self):
        self.clear()
        self.write(f"Score : {self.score} High Score: {self.highscore}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open(file_path, mode="w") as data:
                data.write(f"{self.highscore}")
        self.score = 0
        self.update_scoreboard()


    # def game_over(self):
    #     self.goto(0.0, 0.0)
    #     self.write(f"GAME OVER !", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
