from turtle import Turtle
from random import randint


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.speed("fastest")
        self.shape("circle")
        self.color("white")
        self.penup()
        self.shapesize(0.5, 0.5)
        self.refresh()

    def refresh(self):
        random_x_coordinate = randint(-480, 480)
        random_y_coordinate = randint(-390, 390)
        self.goto(random_x_coordinate, random_y_coordinate)
