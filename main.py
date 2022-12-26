import turtle
from turtle import Turtle, Screen
import random

is_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title='Make Your Bet', prompt='Who do you think would win?')
colors = ['red', 'green', 'blue', 'cyan', 'light green', 'turquoise', 'light salmon']


if user_bet.lower() in colors:
    is_on = True
else:
    print(f"The turtle of color {user_bet} doesn't exist")

y_axis = [-90, -60, -30, 0, 30, 60, 90]
all_turtles = []

for i in range(len(colors)):
    tim = Turtle('turtle')
    tim.penup()
    tim.color(colors[i])
    tim.goto(x=-235, y=y_axis[i])
    all_turtles.append(tim)


while is_on:
    for turtle in all_turtles:
        if turtle.xcor() > 220:
            if turtle.pencolor() == user_bet.lower():
                print(f"You won. The {turtle.pencolor()} turtle is the winner.")
            else:
                print(f"You lost. The {turtle.pencolor()} turtle is the winner.")
            is_on = False
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)


screen.exitonclick()