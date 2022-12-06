from turtle import Turtle
import random
colors = ["violet","blue","green","yellow","orange","red"]
val = []
START_DISTANCE = 3

for i in range(-250,250,20):
    val.append(i)
class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.dis=0
    def create_car(self):
        self.penup()
        self.hideturtle()
        self.shape("square")
        self.shapesize(stretch_wid=1,stretch_len=2)
        self.color(random.choice(colors))
        self.goto(280,random.choice(val))
        self.setheading(180)
        self.showturtle()


    def move_car(self):
        self.forward(START_DISTANCE+self.dis)

    def level_up(self,speed):
        self.dis+=speed



