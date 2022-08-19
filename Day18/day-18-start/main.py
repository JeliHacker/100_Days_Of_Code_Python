# import turtle
# tim = turtle.Turtle()

# from turtle import Turtle
#
# tim = Turtle()
# tom = Turtle()
# terry = Turtle()

# import turtle as t
# tim = t.Turtle()


# import heroes
# print(heroes.gen())
import turtle
from turtle import Turtle, Screen
import random

screen = Screen()
screen.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

tim = Turtle()
tim.shape("turtle")
tim.color("LightSlateBlue")

# Challenge 3 - Drawing shapes
# def drawShape(sides):
#     randomColor = (int(random.randint(0, 255)), int(random.randint(0, 255)), int(random.randint(0, 255)))
#     tim.pencolor(randomColor)
#
#     angle = 360 / sides
#     for _ in range(sides):
#
#         tim.forward(69)
#         tim.right(angle)
#
#
# for num in range(3, 11):
#     drawShape(num)


tim.speed(0)
tim.pensize(10)

# Challenge 4
# for _ in range(1000):
#     randomColor = (int(random.randint(0, 255)), int(random.randint(0, 255)), int(random.randint(0, 255)))
#     tim.pencolor(random_color())
#     heading = 0
#     direction = random.randint(1, 4)
#     if direction == 1:
#         heading = 0
#     elif direction == 2:
#         heading = 90
#     elif direction == 3:
#         heading = 180
#     elif direction == 4:
#         heading = 270
#
#     tim.setheading(heading)
#     tim.forward(20)

# Challenge 5 - Spirograph

tim.pensize(2)

# count = 0
# while count < 361:
#     if count % 10 == 0:
#         tim.circle(100)
#         tim.setheading(count)
#     count += 1

def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.pencolor(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)

draw_spirograph(5)


screen.exitonclick()