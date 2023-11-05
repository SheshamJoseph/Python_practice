from turtle import Turtle

class Block(Turtle):

    def __init__(self,position: tuple[int, int]) -> None:
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=2.5)
        self.penup()
        self.goto(position)