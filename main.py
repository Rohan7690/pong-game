from turtle import Turtle, Screen
import time
from scoreboard import Scoreboard
from paddle import Paddle
from ball import Ball

screen = Screen()
screen.bgcolor("black")
ball = Ball()
scoreboard = Scoreboard()
screen.tracer(0)
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
screen.setup(800, 600)
screen.title("pong")
screen.listen()
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

screen.listen()
screen.onkey(r_paddle.l_down, "Down")
screen.onkey(r_paddle.l_up, "Up")

screen.update()

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    # detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    # detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
    # ball misses by the player
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()


screen.exitonclick()
