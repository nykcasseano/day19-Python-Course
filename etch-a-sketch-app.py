from turtle import Turtle, Screen

bob = Turtle()
screen = Screen()

def move_forwards():
    bob.forward(10)
    
def move_backwards():
    bob.backward(10)

def turn_left():
    new_heading = bob.heading() + 10
    bob.setheading(new_heading)
    
def turn_right():
    new_heading = bob.heading() - 10
    bob.setheading(new_heading)

def clear_screen():
    bob.clear()
    bob.penup()
    bob.home()
    bob.pendown()

screen.listen()
screen.onkey(move_forwards, "w")
screen.onkey(move_backwards, "s")
screen.onkey(turn_left, "a")
screen.onkey(turn_right, "d")
screen.onkey(clear, "c")

screen.exitonclick()