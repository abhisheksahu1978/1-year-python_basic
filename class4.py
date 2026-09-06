import turtle
t=turtle.Turtle()
s = turtle.Screen()
s.bgcolor("black")
t.speed(0)
turtle.tracer(4,0)
t.color("cyan")
t.width(2)

for i in range(400):
    t.forward(i*4)
    t.circle(i*0.5)
    t.left(91)
    t.forward(i*0.2)
    t.circle(i*0.1, 90)
    t.up()
    t.goto(0,0)
    t.down()
turtle.done()
