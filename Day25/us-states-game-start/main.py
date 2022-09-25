import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

write = turtle.Turtle()
write.hideturtle()
write.penup()
game_is_on = True


states_data = pandas.read_csv("50_states.csv")
all_states = states_data.state.to_list()
guessed_states = []



while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                    prompt="What's another state's name?").title()

    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    if answer_state in all_states:
        if not answer_state in guessed_states:
            guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = states_data[states_data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)

# states to learn.csv




screen.exitonclick()














# My first attempt
# states_names = states_data["state"]
# states_dict = states_data.to_dict()
# print(states_dict)
#
# correct_guesses = []
#
# while game_is_on:
#
#     answer_state = screen.textinput(title="Guess the State", prompt="What's another state's name?")
#     print(answer_state)
#
#     count = 0
#     for state in states_names:
#         if answer_state.lower() == state.lower():
#             x_cor = states_dict['x'][count]
#             y_cor = states_dict['y'][count]
#             write.goto(x_cor, y_cor)
#             write.write(state)
#
#         count += 1
#
# print("Game Over")

