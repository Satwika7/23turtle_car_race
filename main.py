from turtle import Screen
from racer import Racer
import time
import random
from cars import Car
from scoreboard import Score
scr = Screen()
scr.setup(width=600,height=600)
scr.bgcolor("black")
scr.tracer(0)
game_on =True
racer = Racer()
score = Score()
score.update_level()
scr.listen()
scr.onkey(fun=racer.move_racer,key = "Up")

cars=[]
inc_speed = 0
x=6
while game_on:


    scr.update()
    car = Car()
    time.sleep(0.01)
    random_chance = random.randint(1, x)
    if random_chance == 1:
        car.create_car()
        car.level_up(inc_speed)
        cars.append(car)
    for each_car in cars:
        each_car.move_car()
    #detect collission with car
        if each_car.distance(racer)<20:
            game_on = False
            score.game_over()
            break
    #detect colission with wall
    if racer.ycor()>270:
        #game_on = False
        racer.goto(0,-280)
        score.update_level()
        inc_speed += 3
        if x>1:
            x-=1
        for each_car in cars:
            each_car.level_up(inc_speed)











scr.exitonclick()