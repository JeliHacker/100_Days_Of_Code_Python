# import colorgram
#
# print("first this")
# rgb_colors = []
# colors = colorgram.extract('image.jpg', 10)
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)

from turtle import Turtle, Screen
import random
color_list = [(1, 13, 31), (52, 25, 17), (219, 127, 106), (9, 105, 160), (242, 214, 69), (150, 84, 39)]


t = Turtle()
t.hideturtle()
t.penup()
t.setheading(270)
t.forward(100)
t.setheading(180)
t.forward(100)
t.setheading(0)
screen = Screen()
screen.colormode(255)
dot_width = 15
t.speed("fastest")

for i in range(10):
    for j in range(10):
        color = random.choice(color_list)
        t.color(color)
        t.pencolor(color)
        t.forward(dot_width * 2)
        t.dot(dot_width)
    t.setheading(t.heading() + 90)
    t.forward(dot_width * 2)
    t.setheading(t.heading() + 90)
    t.forward(10 * dot_width * 2)
    t.setheading(t.heading() + 180)



screen.exitonclick()




# Angela's solution:
#
# import turtle as turtle_module
# import random
#
# turtle_module.colormode(255)
# tim = turtle_module.Turtle()
# color_list = [(1, 13, 31), (52, 25, 17), (219, 127, 106), (9, 105, 160), (242, 214, 69), (150, 84, 39)]
#
# tim.setheading(225)
# tim.forward(300)
# tim.setheading(0)
# number_of_dots = 100
#
# for dot_count in range(1, number_of_dots):
#     tim.dot(20, random.choice(color_list))
#     tim.forward(50)
#
#     if dot_count % 10 == 0:
#         tim.setheading(90)
#         tim.forward(50)
#         tim.setheading(180)
#         tim.forward(500)
#         tim.setheading(0)