import turtle

ALIGN = "center"
FONT = ("Courier", 14, "normal")


class Score(turtle.Turtle):

    def __init__(self, position):
        super().__init__()
        self.value = 0
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(position)
        self.write(f"Score: {self.value}", align=ALIGN, font=FONT)

    def point_increase(self):
        self.value += 1
        self.clear()
        self.write(f"Score: {self.value}", align=ALIGN, font=FONT)
