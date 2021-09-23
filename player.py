from turtle import Turtle




class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.start_position()
        self.color("green")
        self.move_speed = 10

    def go_forward(self):
        self.forward(self.move_speed)

    def change_speed(self):
        self.move_speed -= 1
        if self.move_speed == 0:
            self.move_speed = 10

    def start_position(self):
        self.goto(x=0, y=-280)
