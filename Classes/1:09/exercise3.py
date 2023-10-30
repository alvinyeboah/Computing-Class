import turtle

def polygon(t, length, n):
    angle = 360 / n
    for _ in range(n):
        t.forward(length)
        t.right(angle)

bob = turtle.Turtle()
polygon(bob, 100, 6)
turtle.done()
