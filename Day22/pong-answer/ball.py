from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.speed = 10
        self.x_move = self.speed
        self.y_move = self.speed

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1

    def reset_position(self):
        self.goto(0, 0)
        self.x_move = self.speed
        self.y_move = self.speed
        self.x_move *= -1

    def increase_speed(self):
        self.x_move *= 1.2
        self.y_move *= 1.2
