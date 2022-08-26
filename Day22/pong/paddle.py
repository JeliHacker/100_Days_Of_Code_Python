from turtle import Turtle

PADDLE_LENGTH = 3

class Paddle:

    def __init__(self, user):
        self.paddle_segments = []
        self.paddle_head = Turtle()
        if user:
            self.create_user_paddle()
            self.paddle_head = self.paddle_segments[0]

    def create_user_paddle(self):
        y_count = 20
        for num in range(PADDLE_LENGTH):
            paddle_segment = Turtle("square")
            paddle_segment.speed("fastest")
            paddle_segment.penup()
            paddle_segment.color("white")
            paddle_segment.goto(-340, y_count)
            self.paddle_segments.append(paddle_segment)
            y_count -= 20

    def up(self):
        for seg in self.paddle_segments:
            seg.setheading(90)
            seg.goto(seg.xcor(), seg.ycor() + 10)

    def down(self):
        for seg in self.paddle_segments:
            seg.setheading(90)
            seg.goto(seg.xcor(), seg.ycor() - 10)
