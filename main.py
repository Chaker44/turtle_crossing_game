import time, random
from turtle import Screen
from player import Player
from car import Car
from scoreboard import Scoreboard

number_of_car = 10

# Fix the main screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("white")
screen.title("Turtle crossing game")
screen.tracer(0)

# Show the turtle and the scoreboard
player = Player()
scoreboard = Scoreboard()

# Make the turtle move forward
screen.listen()
screen.onkey(player.go_forward, "Up")

game_is_on = True
cars_of_game = []
while game_is_on:
    chance = random.randint(0, 7)
    time.sleep(0.1)
    screen.update()
    if chance == 1:
        car = Car()
        cars_of_game.append(car)
    for i_car in cars_of_game:
        # Detect collision with the turtle
        if player.distance(i_car) < 22:
            scoreboard.game_over()
            game_is_on = False
        else:
            i_car.move()

    if player.ycor() >= 300:
        # update the level
        scoreboard.update_scoreboard()
        # increase the car speed
        for i_car in cars_of_game:
            i_car.increase_speed()
        # dicrease the turtle speed
        player.change_speed()
        player.start_position()

screen.exitonclick()
