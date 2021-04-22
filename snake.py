from turtle import Turtle

COORDINATES = [(0, 0), (-10, 0), (-20, 0)]
MOVING_DISTANCE = 10
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:

    def __init__(self):
        self.turtles = []
        self.create_snake()
        self.head = self.turtles[0]

    def create_snake(self):
        for coordinate in COORDINATES:
            self.add_turtle(coordinate)

    def add_turtle(self, coordinate):
        my_turtle = Turtle(shape="square")
        my_turtle.shapesize(0.5, 0.5)
        my_turtle.speed("fastest")
        my_turtle.penup()
        my_turtle.color("navy")
        my_turtle.goto(coordinate)
        self.turtles.append(my_turtle)

    def extend(self):
        self.add_turtle(self.turtles[-1].position())

    def move(self):
        for num in range(len(self.turtles) - 1, 0, -1):
            new_x = self.turtles[num - 1].xcor()
            new_y = self.turtles[num - 1].ycor()
            self.turtles[num].goto(new_x, new_y)
        self.head.forward(MOVING_DISTANCE)
        # self.turtles[0].left(90)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
