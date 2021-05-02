# create paddle
from turtle import Turtle

class Paddle(Turtle): # Paddle class inherit from Turtle, replace all paddle. with self.
    def __init__(self, position):
        super().__init__()
        paddle = Turtle()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position) # paddle object need to be initialized with a tuple for X & Y coordinates

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)