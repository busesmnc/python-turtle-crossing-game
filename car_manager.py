from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.cars = []
        self.hideturtle()
        self.create_car()
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        for i in range(20):
            car = Turtle()
            car.shape("square")
            car.penup()
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.color(random.choice(COLORS))
            car.setposition(x=random.randint(-280, 280), y=random.randint(-280, 280))
            car.setheading(180)
            self.cars.append(car)

    def move(self):
        for i in self.cars:
            i.forward(self.car_speed)

    def add_cars(self):
        rand_num = random.randint(1, 7)
        if rand_num == 1:
            car = Turtle()
            car.shape("square")
            car.penup()
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.color(random.choice(COLORS))
            car.setposition(x=random.randint(280, 506), y=random.randint(-280, 280))
            car.setheading(180)
            self.cars.append(car)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT