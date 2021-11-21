import turtle
import ball
import score
import paddle
import time

# creat game screen or play ground
screen = turtle.Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

# create the middle net of the game
midline = turtle.Turtle()
midline.color("white")
midline.penup()
midline.hideturtle()
midline.goto(x=0, y=300)
midline.seth(270)
for _ in range(0, 70):
    midline.pendown()
    midline.forward(10)
    midline.penup()
    midline.forward(8)

# make paddles
paddle_r = paddle.Paddle()
paddle_r.right_paddle()

paddle_l = paddle.Paddle()
paddle_l.left_paddle()
# make paddles move
screen.listen()
# right paddle moves
screen.onkey(fun=paddle_r.go_up, key="Up")
screen.onkey(fun=paddle_r.go_down, key="Down")
# left paddle moves
screen.onkey(fun=paddle_l.go_up, key="w")
screen.onkey(fun=paddle_l.go_down, key="s")
# creat a ball object
ball = ball.Ball()
# creat score objects
score_l = score.Score((-225, 265))
score_r = score.Score((225, 265))
game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    if (ball.ycor() > 290) or (ball.ycor() < -280):
        ball.bounce_y()

    # detect collision between ball and paddle and getting score for each collision
    if (ball.distance(paddle_l) <= 35) and (ball.xcor() <= -370) and (ball.xcor() > -375):
        ball.bounce_x()
        score_l.point_increase()

    if (ball.distance(paddle_r) <= 35) and (ball.xcor() >= 370) and (ball.xcor() < 375):
        ball.bounce_x()
        score_r.point_increase()

    # if a player missed a ball, their opponent gets a score

    if ball.xcor() > 398:
        score_l.point_increase()
        ball.reset_ball()

    if ball.xcor() < -398:
        score_r.point_increase()
        ball.reset_ball()

screen.exitonclick()
