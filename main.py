# from turtle import Turtle, Screen
#
# tim = Turtle()
# screen = Screen()
#
# def forward():
#     tim.forward(10)
# def backward():
#     tim.backward(10)
# def turnleft():
#
#     newHeading = tim.heading() + 10
#     tim.setheading(newHeading)
#
# def turnright():
#     newHeading = tim.heading()  - 10
#     tim.setheading(newHeading)
#
# def clear():
#     tim.clear()
#     tim.penup()
#     tim.home()
#     tim.pendown()
#
# screen.listen()
# screen.onkey(forward , "w")
# screen.onkey(backward , "s")
# screen.onkey(turnleft , "d")
# screen.onkey(turnright , "a")
# screen.onkey(clear , "c")
# screen.exitonclick()
import turtle
from turtle import Turtle , Screen
import random

screen = Screen()
screen.setup(height=400 , width=500)

colors = ["red" , "blue" , "yellow" , "purple" , "green" , "orange"]
is_race = False

y_position = [-70 , -40 , -10 , 20 , 50 , 80]
all_turtle = []

for x in range(0 , 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[x])
    new_turtle.penup()
    new_turtle.goto(x=-235 , y=y_position[x])
    all_turtle.append(new_turtle)

user_bet = screen.textinput(title="Make your bet" , prompt="Which turtle wins the race: ")

if user_bet:
    is_race = True

while is_race:

    for turtle in all_turtle:
        if turtle.xcor()> 230:
            is_race = False
            winColor = turtle.pencolor()
            if winColor == user_bet:
                print("You won, congratulations!! ")

            else:
                print("You Loss, Bet Again")
                print(f"{winColor} turtle, won the race....")

        rand_distance = random.randint(0 , 10)
        turtle.forward(rand_distance)

screen.exitonclick()
