import turtle
def draw_square():
    window = turtle.Screen()
    window.bgcolor('orange')
    move = turtle.Turtle()
    move.forward(100)
    move.right(90)
    move.forward(100)
    window.exitonclick()
draw_square()
