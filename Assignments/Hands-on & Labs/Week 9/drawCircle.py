import math

def drawCircle(turtle, center_x, center_y, radius):
    turtle.penup()
    turtle.goto(center_x + radius, center_y)
    turtle.pendown()
    
    step_distance = 2.0 * math.pi * radius / 120.0
    
    for _ in range(120):
        turtle.forward(step_distance)
        turtle.right(3)

if __name__ == "__main__":
    import turtle
    
    screen = turtle.Screen()
    t = turtle.Turtle()
    

    drawCircle(t, 0, 0, 100)
    
    screen.mainloop()
