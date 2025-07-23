import turtle
import math

t = turtle.Turtle()
t.speed(0)
t.color("red")
turtle.bgcolor("black")

def corazon(n):
    x = 16 * math.sin(n)**3
    y = 13 * math.cos(n) - 5 * math.cos(2 * n) - 2 * math.cos(3 * n) - math.cos(4 * n)
    return x, y

t.penup()
t.goto(0, 0)
t.pendown()

scale = 20

for n in range(0, 360):
    angle = math.radians(n)
    x, y = corazon(angle)
    t.goto(x * scale, y * scale)

t.hideturtle()
turtle.done()