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




# How to record mouse clicks on map
# def get_mouse_click_coord(x, y):
#     print(x,y)
#
#
# screen.onscreenclick(get_mouse_click_coord)
# turtle.mainloop()


# import pandas
# data = pandas.read_csv("Squirrel_Data.csv")
# grey_squirrels = data[data["Primary Fur Color"] == 'Gray']
# red_squirrels = data[data["Primary Fur Color"] == 'Cinnamon']
# black_squirrels = data[data["Primary Fur Color"] == 'Black']
# count_grey = len(grey_squirrels)
# count_red = len(red_squirrels)
# count_black = len(black_squirrels)
# d = {
#     "Fur Color": ["grey", "red", "black"],
#     "Count": [count_grey, count_red, count_black]
# }
# new_dataset = pandas.DataFrame(d)
# new_dataset.to_csv("new_dataset.csv")
