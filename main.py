from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Score
import time

screen = Screen()
screen.colormode(255)
screen.title("Snake Game")

screen.setup(width=1000, height=800)
screen.bgcolor((119, 221, 119))
screen.tracer(0)

snake = Snake()

snake.create_snake()

screen.listen()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Right", fun=snake.right)
screen.onkey(key="Left", fun=snake.left)

food = Food()

score = Score()

is_continue = True
while is_continue:
    time.sleep(0.09)
    screen.update()
    snake.move()

    if snake.head.distance(food) < 10:
        food.refresh()
        snake.extend()
        score.increase_score()
    if snake.head.xcor() > 490 or snake.head.xcor() < -490 or snake.head.ycor() > 390 or snake.head.ycor() < -390:
        is_continue = False
        score.game_over()

    for turtle in snake.turtles:
        if turtle == snake.head:
            pass
        elif snake.head.distance(turtle) < 7.5:
            is_continue = False
            score.game_over()


screen.exitonclick()
