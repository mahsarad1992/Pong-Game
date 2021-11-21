import turtle


class Paddle(turtle.Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.resizemode("user")
        self.shapesize(stretch_wid=4, stretch_len=0.8)
        self.speed("fastest")

    def right_paddle(self):
        self.penup()
        self.goto(x=370, y=0)

    def left_paddle(self):
        self.penup()
        self.goto(x=-370, y=0)

    def go_up(self):
        new_y = self.ycor() + 25
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 25
        self.goto(self.xcor(), new_y)
