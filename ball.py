from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self): # y coordinate is going to reverse, bouncing in y axis
        # new_y = self.ycor() - self.y_move
        # self.goto(self.xcor(), new_y)
        self.y_move = self.y_move * -1

    def bounce_x(self): # x coordinate is going to reverse, bouncing in x axis
        # new_x = self.ycor() - self.x_move
        # self.goto(new_x, self.ycor())
        self.x_move = self.x_move * -1 # self.x_move *= -1
        self.move_speed *= 0.9  # speed up when ball hit paddle

    def reset_position(self):
        self.goto(0,0) # ball go back to center
        self.move_speed = 0.1
        self.bounce_x() # start off at the center and go off in opposite direction