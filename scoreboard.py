from turtle import Turtle

ALIGN = "left"
FONT = ("Arial", 16, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.level = 0
        self.goto(x=-280, y=260)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.level += 1
        self.write(f"Level:{self.level}", font=FONT, align=ALIGN)

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", font=FONT, align="center")