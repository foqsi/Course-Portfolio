from turtle import Turtle
import time

t = Turtle()

t.pencolor("blue")
t.hideturtle()

def square(t, length):
    for count in range(4):
        t.forward(length)
        t.left(90)

def hexagon(t, length):
    for count in range(6):
        t.forward(length)
        t.left(60)

def radialHexagons(t, n, length):
    for count in range(n):
        hexagon(t, length)
        t.left(360 / n)

def radialPattern(t, n, length, shape):
    for count in range(n):
        shape(t, length)
        t.left(360 / n)

# square(t, 50)
# time.sleep(5)
# t.clear()
# hexagon(t, 50)
# time.sleep(5)
# t.clear()
# radialHexagons(t, 10, 50)
# time.sleep(5)
radialPattern(t, n = 10, length = 50, shape = square)
time.sleep(5)
