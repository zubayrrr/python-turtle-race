from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(500, 400)

# asking user to place a bet on a turtle
bet = screen.textinput(title="Choose your turtle", prompt="Which turtle would you like to place a bet on? ")
print(f"You've placed your bet on {bet} turtle.")
# Coloring individual turtles
race = False
colors = ['orange', 'yellow', 'blue', 'green', 'red','purple']
turtles = []
position_y = -100

for i in range(0, 6):
    turtle = Turtle(shape="turtle")
    turtle.penup()
    turtle.color(colors[i])
    turtle.goto(x=-230, y=position_y)
    position_y -= -40
    turtles.append(turtle)

if bet:
    race = True

while race:
    for t in turtles:
        if t.xcor() > 230:
            race = False
            winner = t.pencolor()
            if bet == winner:
                print(f"You've won! The winner is {winner} turtle.")
            else:
                print(f"You've lost! The winner is {winner} turtle.")
        distance = random.randint(0, 10)
        t.forward(distance)


screen.exitonclick()

