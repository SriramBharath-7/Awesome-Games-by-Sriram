from turtle import Turtle

class MainScreen:

    def __init__(self):
        self.dash_length = 20
        self.gap_length = 10
        self.number_of_dashes = 40
        self.dashed_line()

    def dashed_line(self):
        turtle = Turtle()
        turtle.color('White')
        turtle.speed(10)
        turtle.pensize(3)
        turtle.penup()
        turtle.goto(0, 400)
        turtle.pendown()
        turtle.setheading(270)


        for _ in range(self.number_of_dashes):
            turtle.forward(self.dash_length)
            turtle.penup()
            turtle.forward(self.gap_length)
            turtle.pendown()


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("White")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100,200)
        self.write(self.l_score,align="center",font= ("Verdana", 80, "bold"))
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("Verdana", 80, "bold"))

    def increase_score_l(self):
        self.l_score += 1
        self.update_scoreboard()

    def increase_score_r(self):
        self.r_score += 1
        self.update_scoreboard()