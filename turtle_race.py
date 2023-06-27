from turtle import T

bob = Turtle()
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="which turtle will win the race? Enter a color:")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]

for turtle_index in range(0,6):
    bob.Turtle(shape="turtle")
    bob.color(colors[turtle_index])
    bob.penup()
    bob.goto(x=-230, y=y_positions[turtle_index])
    



screen.exitonclick()
