from board import Board
from turtle import Screen
from paddle import Paddle

screen = Screen()
screen.bgcolor("black")
board = Board()
user_paddle = Paddle(True)
screen.listen()
screen.onkey(user_paddle.up, "Up")
screen.onkey(user_paddle.down, "Down")



game_is_on = True

while game_is_on:
    screen.update()


