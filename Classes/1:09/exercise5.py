import turtle
import math

def polygon(t, length, n):
    angle = 360 / n
    for _ in range(n):
        t.forward(length)
        t.right(angle)

def arc(t, r, angle):
    circumference = 2 * math.pi * r
    length = circumference * angle / 360
    n = int(angle / 360 * 50)
    polygon(t, length, n)

bob = turtle.Turtle()
arc(bob, 100, 90)
turtle.done()
