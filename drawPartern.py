import turtle
def draw():
    window = turtle.Screen()
    window.bgcolor('gray')
    move = turtle.Turtle()
    move.shape("turtle")
    move.color('orange')
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
