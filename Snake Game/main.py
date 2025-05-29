#IMPORTING THE MODULES
from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

#SETTING UP THE SCREEN
screen = Screen()
screen.setup(height=600,width=600)
screen.bgcolor('Black')
screen.title("Py_snake")
screen.tracer(0)

# CREATING AN OBJECT AND INITIATING IT
snake = Snake()
food = Food()
score = ScoreBoard()

#SETTING UP KEYBOARD KEYS SO THAT IT'S FUNCTONAL GAME
screen.listen()
screen.onkey(fun=snake.up,key="Up")
screen.onkey(fun=snake.down,key="Down")
screen.onkey(fun=snake.left,key="Left")
screen.onkey(fun=snake.right,key="Right")

game_on = True
while game_on:

    screen.update()
    time.sleep(0.1)
    # USING A METHOD FROM SNAKE CLASS TO MOVE
    snake.move()
    
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase_score()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_on = False
        score.gameover()

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_on = False
            score.gameover()
screen.exitonclick()