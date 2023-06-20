from turtle import Turtle, Screen

tobby = Turtle()
screen = Screen()


def move_forward():
    
    tim.forward(10)
    
screen.listen()
screen.onkey(key="space", fun=move_forward)
screen.onkey()