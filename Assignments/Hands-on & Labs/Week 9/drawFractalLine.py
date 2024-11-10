import turtle

def drawFractalLine(t, distance, level):
    if level == 0:
        t.forward(distance)
    else:
        distance /= 3.0
        drawFractalLine(t, distance, level - 1)
        t.left(60)
        drawFractalLine(t, distance, level - 1)
        t.right(120)
        drawFractalLine(t, distance, level - 1)
        t.left(60)
        drawFractalLine(t, distance, level - 1)

def drawKochSnowflake(t, distance, level):
    for angle in [0, -120, 120]:
        t.setheading(angle)
        drawFractalLine(t, distance, level)

if __name__ == "__main__":
    screen = turtle.Screen()
    t = turtle.Turtle()
    t.speed(0)
    
    t.penup()
    t.goto(-150, 100)
    t.pendown()
    
    drawKochSnowflake(t, 300, 2)

    screen.mainloop()
