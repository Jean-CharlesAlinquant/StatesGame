import turtle
import pandas
FONT = ("Courier", 12, "normal")
TOTAL_STATES = 50

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()


screen = turtle.Screen()
screen.title = "U.S. States Game"
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

printState = turtle.Turtle()
printState.penup()
printState.hideturtle()

guessed_states = []
while len(guessed_states) < TOTAL_STATES:
    answer_state = screen.textinput(f"{len(guessed_states)}/50 States Correct",
                                    "What's another state's name").title()

    if answer_state == "Exit":
        states_to_learn = []
        for state in all_states:
            if state not in guessed_states:
                states_to_learn.append(state)
        new_data = pandas.DataFrame(states_to_learn)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in all_states:
        state_data = data[data["state"] == answer_state]
        x = state_data.x.item()
        y = state_data.y.item()
        printState.goto(x, y)
        printState.write(f"{answer_state}", align="center", font=FONT)
        guessed_states.append(answer_state)
    else:
        print(f"{answer_state} is not a U.S. State")

screen.exitonclick()