import turtle
def draw():
    window = turtle.Screen()
    window.bgcolor('orange')
    move = turtle.Turtle()
    i = 20
    while True:
        deg = 5
        move.forward(i)
        move.right(120)
        move.forward(i)
        move.right(120)
        move.forward(i)
        move.left(deg)
        i = i + 10
draw()
