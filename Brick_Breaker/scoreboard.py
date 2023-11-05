from turtle import Turtle

class ScoreBoard(Turtle):
    def __inti__(self):
        super().__init__()
        self.color("white")
        # self.shape("square")
        self.penup()
        self.hideturtle()
        self.display_score()
    
    def display_score(self):
        self.goto(0, 280)
        self.write("Score : ", align="center", font=("kinnari", 24, "bold"))
