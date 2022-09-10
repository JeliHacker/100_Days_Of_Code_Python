'''
Create a turtle player that starts at the bottom of the screen and listen for the "Up" keypress to move the turtle
north. If you get stuck, check the video walkthrough in Step 3.

Create cars that are 20px high by 40px wide that are randomly generated along
 the y-axis and move to the left edge of the screen.
 No cars should be generated in the top and bottom 50px of the screen
 (think of it as a safe zone for our little turtle).
 Hint: generate a new car only every 6th time the game loop runs.
 If you get stuck, check the video walkthrough in Step 4.
'''

import time
from turtle import Screen, Turtle
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.colormode(255)

# Draw safe zone lines
drawer = Turtle()
drawer.penup()
drawer.goto(-300, -250)
drawer.pendown()
drawer.forward(600)
drawer.penup()
drawer.goto(-300, 250)
drawer.pendown()
drawer.forward(600)
drawer.hideturtle()

player = Player()
cars = CarManager()
print(cars.cars)

screen.listen()
screen.onkey(player.moveUp, "Up")

game_is_on = True
count = 0
collide_with_car = False
while game_is_on:
    time.sleep(0.1)
    if count % 6 == 0:
        cars.generate_car()
    cars.move()

    screen.update()

    if player.ycor() > 260:
        print("Wins!")
        time.sleep(5)
        player.goto((0, -280))

    for car in cars.cars:
        if player.distance(car) < 20:
            collide_with_car = True
            break
    if collide_with_car:
        game_is_on = False
    count += 1



screen.exitonclick()
