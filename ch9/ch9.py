import turtle as t
from random import random

while True:
    t.penup()
    t.goto(0, 100)
    t.pendown()
    t.begin_fill()
    t.fillcolor("red")
    t.goto(-50, 0)
    t.goto(50, 0)
    t.goto(0, 100)
    t.end_fill()

    t.penup()
    t.goto(-25, 50)
    t.pendown()
    t.begin_fill()
    t.fillcolor("blue")
    t.goto(0, 0)
    t.goto(25, 50)
    t.goto(-25, 50)
    t.end_fill()

    break

t.exitonclick()
