from turtle import T

bob = Turtle()
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="which turtle will win the race? Enter a color:")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
all_tutles = []

for turtle_index in range(0,6):
    bob.Turtle(shape="turtle")
    bob.color(colors[turtle_index])
    bob.penup()
    bob.goto(x=-230, y=y_positions[turtle_index])
    all_tutles.append(new_turtle)
    
if user_bet:
    is_race_on = True
    
while is_race_on:
    
    for turtle in all_tutles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the Winner!" )
            else: 
                print(f"You've lost! The {winning_color} turtle is the Winner!" )

            rand_distance = random.randint(0, 10)
            turtle.forward(rand_distance)
            

screen.exitonclick()
