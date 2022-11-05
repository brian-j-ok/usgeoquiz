import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")

GUESSED_STATES = []

while len(GUESSED_STATES) < 50:
    answer_state = screen.textinput(title="Guess the State", prompt="What's another state's name?")

    state_row = data.loc[data['state'] == answer_state]
    state_name = state_row.state.item()
    state_xpos = state_row.x.item()
    state_ypos = state_row.y.item()

    state_turtle = turtle.Turtle()
    state_turtle.penup()
    state_turtle.hideturtle()
    state_turtle.setposition(int(state_xpos), int(state_ypos))
    state_turtle.write(f"{state_name}", align="center", font=('Arial', 8, 'normal'))

turtle.mainloop()
