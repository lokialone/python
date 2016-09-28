import turtle

def draw_parallelogram(move) :
    move.forward(100)
    move.right(60)
    move.forward(100)
    move.right(120)
    move.forward(100)
    move.right(60)
    move.forward(100)


def draw() :
    window = turtle.Screen()
    window.bgcolor('orange')
    move = turtle.Turtle()
    while True:
        draw_parallelogram(move)
        move.right(115)
draw()
