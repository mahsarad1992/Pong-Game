import turtle


class Ball(turtle.Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(1)
        self.color("yellow")
        # set initial sleep time for ball movement
        self.move_speed = 0.07
        self.penup()
        self.x_step = 10
        self.y_step = 10

    def move(self):
        x_new = self.xcor() + self.x_step
        y_new = self.ycor() + self.y_step
        self.goto(x_new, y_new)
        # bouncing the ball

    def bounce_y(self):
        self.y_step *= -1

    def bounce_x(self):
        self.x_step *= -1
        # the balls speed increases by each collision with the paddles
        # as the sleep time decreases by * 0.8 each time
        self.move_speed *= 0.8

    def reset_ball(self):
        """
        if a player miss a ball, the ball would reset
        """
        self.goto(0, 0)
        # when reset the ball, it moves with our initiated speed
        self.move_speed = 0.07
        self.x_step *= -1
        self.y_step *= -1
        self.move()
