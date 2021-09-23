from turtle import Turtle
import random

COLORS = ["blue", "green", "red", "yellow", "purple"]



class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(1, 2)
        self.color(random.choice(COLORS))
        self.penup()
        self.y = random.randint(-260, 261)
        self.goto(300, self.y)
        self.move_speed = 10
        self.speed("fastest")

    def move(self):
        self.backward(self.move_speed)

    def increase_speed(self):
        self.move_speed += 1