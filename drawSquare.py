import turtle
def draw_square():
    window = turtle.Screen()
    window.bgcolor('orange')
    move = turtle.Turtle()
    while True:
        move.forward(100)
        move.right(90)
        move.forward(100)
        move.right(90)
        move.forward(100)
        move.right(90)
        move.forward(100)
        move.right(5)
    window.exitonclick()

draw_square()
