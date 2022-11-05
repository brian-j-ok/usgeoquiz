import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")

GUESSED_STATES = []

def check_input(answer_state):
    if answer_state not in GUESSED_STATES:
        state_row = data.loc[data['state'] == answer_state]
        state_name = state_row.state.item()
        state_xpos = state_row.x.item()
        state_ypos = state_row.y.item()

        GUESSED_STATES.append(state_name)

        draw_answer(state_name, state_xpos, state_ypos)

def draw_answer(name, x, y):
    state_turtle = turtle.Turtle()
    state_turtle.penup()
    state_turtle.hideturtle()
    state_turtle.setposition(int(x), int(y))
    state_turtle.write(f"{name}", align="center", font=('Arial', 8, 'normal'))


while len(GUESSED_STATES) < 50:
    answer_state = screen.textinput(title="Guess the State", prompt="What's another state's name?").capitalize()

    check_input(answer_state)

    print(len(GUESSED_STATES))
    print(GUESSED_STATES)

turtle.mainloop()
