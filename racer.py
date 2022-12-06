from turtle import Turtle


class Racer(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(0,-280)
        self.color("white")
        self.shape("turtle")
        self.setheading(90)
        self.showturtle()

    def move_racer(self):
        self.forward(10)