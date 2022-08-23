from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forwards():
    tim.forward(10)

def move_backwards():
    tim.forward(-10)

def turn_right():
    tim.setheading(tim.heading() - 10)

def turn_left():
    tim.setheading(tim.heading() + 10)

def clear():
    # screen.reset()
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


screen.listen()
screen.onkey(key="space", fun=move_forwards)
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="c", fun=clear)


screen.exitonclick()
