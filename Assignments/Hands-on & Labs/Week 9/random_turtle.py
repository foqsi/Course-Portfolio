from turtle import Turtle
import random
import time

def randomWalk(t, turns, distance = 20):
    for x in range(turns):
        degrees = random.randint(0, 270)
        if x % 2 == 0:
            t.left(degrees)
        else:
            t.right(degrees)
        t.forward(distance)

def main():
    t = Turtle()
    t.shape("turtle")
    randomWalk(t, 40, 30)
    time.sleep(5)

if __name__ == "__main__":
    main()