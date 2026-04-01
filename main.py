from turtle import *

window = Screen()
window.bgcolor("black")
window.setup(width = 700, height = 700)
t = Turtle()
t.speed(0)
t.color("white")
t.penup()
t.goto(-255,-90)
t.left(90)
t.pendown()
t.forward(255)
t.left(-160)
t.forward(270)
t.right(-160)
t.forward(255)
t.penup()

t.color("blue")
t.goto(-90,-10)
t.pd()
t.right(90)
t.forward(100)
t.left(120)

for i in range(30):
    t.forward(10)
    t.left(10)
t.penup()

t.color("red")
t.goto(90,0)
t.pendown()
t.goto(90,-90)
t.goto(90,50)
t.penup()
t.goto(90,60)
t.pendown()
t.goto(90,70)
t.penup()


t.color("orange")
t.goto(200,-90)
t.setheading(90)
t.pendown()
t.forward(170)
t.penup()

t.color("purple")
t.right(90)
t.forward(100)
t.right(90)
t.pendown()
t.forward(150)
t.pu()
t.forward(10)
t.pendown()
t.forward(10)

t.penup()
t.goto(50,50)













window.mainloop()

