from turtle import Turtle
ALIGNMENT = "center"
FONT = ('arial', 12, 'normal')

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.score=-1
    def update_level(self):
        self.penup()
        self.color("white")
        self.goto(-250,280)
        self.clear()
        self.score+=1
        self.write(f"level:  {self.score}",align=ALIGNMENT,font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER",align=ALIGNMENT,font=FONT)