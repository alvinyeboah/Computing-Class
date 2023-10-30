import turtle

def square(t):
    for _ in range(4):
        t.forward(100)
        t.right(90)

bob = turtle.Turtle()
square(bob)
turtle.done()
