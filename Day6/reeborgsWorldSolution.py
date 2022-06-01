#https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=problem_world3.json&url=user_world%3Aproblem_world3.json


def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def jump_over_wall():
    turn_left()
    while wall_on_right():
        move()
    turn_right()
    move()
    turn_right()
    while front_is_clear():
        move()
    turn_left()

neverRight = True
while not at_goal():
    if wall_on_right():
        neverRight = False
        if front_is_clear():
            move()
        else:
            turn_left()
    else:
        while not wall_on_right():
            if not neverRight:
                turn_right()
                move()
            else:
                if front_is_clear() == True:
                    move()
                else:
                    turn_left()
