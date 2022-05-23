from turtle import Turtle


class Label(Turtle):

    def __init__(self, answer_choice, position):
        super(Label, self).__init__()
        self.hideturtle()
        self.penup()
        self.color("black")
        self.goto(position)
        self.write(f"{answer_choice}", align="center", font=("Arial", 8, "normal"))

