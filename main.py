import turtle
import state_label
import pandas as pd


def check_answer(answer_choice):
    if answer_choice in states:
        return True
    else:
        return False


def get_position(answer_choice):
    position_x = int(df[df["state"] == answer_choice]["x"])
    position_y = int(df[df["state"] == answer_choice]["y"])
    coordinates = (position_x, position_y)
    return coordinates


screen = turtle.Screen()
screen.title("US States Quiz")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

raw_data = pd.read_csv("50_states.csv")
df = pd.DataFrame(raw_data)
states = df["state"].tolist()

score = 0
guessed_answers = []

while score < 50:
    # accepts input from user
    answer = screen.textinput(title=f"{score}/50 Correct",
                              prompt="Guess a state name OR\n type \'exit\' to quit.").title()

    # exits the game and exports missed states
    if answer == "Exit":
        missing_states = [s for s in states if s not in guessed_answers]
        final_data = pd.DataFrame(missing_states)
        final_data = pd.to_csv("missing_states.csv")
        break

    # check if user's choice is correct
    if check_answer(answer):
        if answer not in guessed_answers:
            position = get_position(answer)
            label = state_label.Label(answer, position)
            score += 1
            guessed_answers.append(answer)



