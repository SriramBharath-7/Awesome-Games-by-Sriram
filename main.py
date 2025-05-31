from turtle import Screen
from mainscreen import MainScreen,ScoreBoard
from player import Players
from ball import Ball
import time

screen = Screen()
screen.bgcolor("Black")
screen.screensize(800,600)
screen.title("Pong")


screen.tracer(0)
player1 = Players((-393,0))
player2 = Players((393,0))
ball = Ball()
dash = MainScreen()
score = ScoreBoard()
screen.listen()
screen.onkey(player1.up,"w")
screen.onkey(player1.down,"s")
screen.onkey(player2.up,"Up")
screen.onkey(player2.down,"Down")

game_on = True
while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    if ball.ycor() > 295 or ball.ycor()  < -295:
        ball.bounce_y()

    if ball.distance(player2) < 50 and ball.xcor() > 370 or ball.distance(player1) < 50 and ball.xcor() < -370:
        ball.bounce_x()


    if ball.xcor() > 380:
        ball.ball_reset()
        ball.move_speed = 0.1
        score.increase_score_l()
    if ball.xcor() < -380:
        ball.ball_reset()
        score.increase_score_r()

screen.exitonclick()