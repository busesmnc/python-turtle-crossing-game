import time
from turtle import Screen, Turtle
from car_manager import CarManager
from player import Player
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.title("Turtle Crossing Game")

the_cars = CarManager()
scoreboard = Scoreboard()
tomy = Player()

screen.listen()
screen.onkey(key="Up", fun=tomy.go_f)

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    the_cars.move()
    the_cars.add_cars()

    for i in the_cars.cars:
        if tomy.distance(i) < 15:
            game_is_on = False
            scoreboard.game_over()

    if tomy.ycor() > 280:
        scoreboard.increase_score()
        tomy.reset_pos()
        the_cars.level_up() 

screen.exitonclick()
