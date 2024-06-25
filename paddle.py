from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.color("#880808")
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=7)
        self.penup()
        # self.speed(speed=10)
        self.goto(position)

    def move_left(self):
        self.backward(70)

    def move_right(self):
        self.forward(70)
