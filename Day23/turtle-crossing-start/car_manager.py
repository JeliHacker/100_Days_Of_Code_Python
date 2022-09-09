from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


def random_color():
    return random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)


class CarManager:
    def __init__(self):
        self.cars = []

    def generate_car(self):
        car = Turtle("square")
        car.penup()
        car.forward(MOVE_INCREMENT)
        car.goto(300, random.randint(-235, 235))
        car.shapesize(1, 2, 1)
        car.setheading(180)
        car.fillcolor(random_color())
        self.cars.append(car)

    def move(self):
        for car in self.cars:
            car.forward(MOVE_INCREMENT)

