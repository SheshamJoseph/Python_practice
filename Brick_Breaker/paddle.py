from turtle import Turtle

class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_len=3, stretch_wid=1)
        self.color("white")
        self.penup()
        self.goto(0, -270)
        
    
    def move_right(self):
        if self.xcor() >= 220:
            pass
        else:
            new_x = self.xcor() + 20
            self.goto(new_x, self.ycor())
        

    def move_left(self):
        if self.xcor() <= -220:
            pass
        else:
            new_x = self.xcor() - 20
            self.goto(new_x, self.ycor())

    # def move_up(self):
    #     new_y = self.ycor() + 10
    #     self.goto(self.xcor(), new_y)

    # def move_down(self):
    #     new_y = self.ycor() - 10
    #     self.goto(self.xcor(), new_y)
