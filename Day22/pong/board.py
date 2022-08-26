from turtle import Turtle, Screen
from paddle import Paddle

class Board():
    def __init__(self):
        #self.screen = Screen()

        #self.user_paddle = Paddle(True)

        #self.screen.bgcolor("black")

        self.create_halfway_marker()

    def create_halfway_marker(self):
        half_turtle = Turtle()
        half_turtle.speed("fastest")
        half_turtle.hideturtle()
        half_turtle.penup()
        half_turtle.pensize(8)
        half_turtle.pencolor("white")
        half_turtle.goto(0, 335)
        half_turtle.setheading(270)
        count = 0
        while half_turtle.ycor() > -350:
            if count % 40 == 0:
                half_turtle.pendown()
            else:
                half_turtle.penup()
            half_turtle.forward(20)
            count += 20
        print("out of while loop")


    def update(self):
        self.screen.update()

