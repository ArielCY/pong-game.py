from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

# Create screen
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Ping Pong Game")
screen.tracer(0) # tracer method control animation, turn off animation by putting

# Create paddle
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

# Create ball
ball = Ball()

# Create scoreboard
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up") # when use a function as a parameter, don't add parentheses
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w") # # l_paddle need to move up & down with "w" & "s" key
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed) # get enough time to see the ball movement
    screen.update() # no animation, need to manually update & refresh
    ball.move()

    # screen is 600px tall, detect collision with top & bottom walls. Change ball's movement direction upon collision
    if ball.ycor() > 280 or ball.ycor() < -280: # Detect collision with wall
        ball.bounce_y() # need to bounce, bouncing in y axis

    # Detect collision with r_paddle & l_paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x() # bouncing in y axis

    # Detect R paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    # Detect L paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()