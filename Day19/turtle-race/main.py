import turtle
from turtle import Turtle, Screen
import random


is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []


y = -100
for color in colors:
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(color)
    new_turtle.goto(x=-230, y=y)
    y = y + 40
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

winner = ""
# My solution
# while is_race_on:
#
#     for turtle in all_turtles:
#         rand_distance = random.randint(0, 10)
#         turtle.forward(rand_distance)
#         if turtle.xcor() >= 245:
#             print("race is over")
#             is_race_on = False
#             winner = turtle.fillcolor()
#             print(f"{winner.title()} is the winner!")

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")

        rand_distance = random.randint(0, 6)
        turtle.forward(rand_distance)

screen.exitonclick()
