import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")

answer_state = screen.textinput(title="Guess the State", prompt="What's another state's name?")

state = data.loc[data['state'] == answer_state]
print(state.get('state').value)

# temp = turtle.Turtle()
# temp.penup()
# temp.hideturtle()
#
# temp.setposition(int(state[1]), int(state[2]))
# temp.write(f"{state[0]}", align='center', font=('Arian', 8, 'normal'))

turtle.mainloop()
