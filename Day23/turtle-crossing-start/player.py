from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super(Player, self).__init__("turtle")
        self.penup()
        self.setheading(90)
        self.goto(STARTING_POSITION)
        self.fillcolor("green")

    def moveUp(self):
        self.goto(0, self.ycor() + MOVE_DISTANCE)


