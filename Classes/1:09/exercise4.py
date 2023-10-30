import turtle
import math

def polygon(t, length, n):
    angle = 360 / n
    for _ in range(n):
        t.forward(length)
        t.right(angle)

def circle(t, r):
    circumference = 2 * math.pi * r
    n = 50
    length = circumference / n
    polygon(t, length, n)

bob = turtle.Turtle()
circle(bob, 100)
turtle.done()
