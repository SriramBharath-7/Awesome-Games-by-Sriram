from turtle import Turtle
ALLIGN = 'center'
FONT = ("Courier New", 18, 'bold')

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0,270)
        self.hideturtle()
        self.update_score()
    def update_score(self):
        self.write(f"Score = {self.score}", move=False, align=ALLIGN, font=FONT)

    def gameover(self):
        self.goto(0,0)
        self.write("GAME OVER", move=False, align=ALLIGN, font=("Courier New", 24, 'bold'))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()