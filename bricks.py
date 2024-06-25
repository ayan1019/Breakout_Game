from turtle import Turtle
import random

color_list = ["#880808", "#AA4A44", "#EE4B2B", "#6E260E", "#800020", "#E97451",
              "#E35335", "#E30B5C", "#FF4433", "#E3735E", "#7C3030", "#630330",
              "#E34234", "#722F37", "#E3735E", "#FAA0A0", "#F33A6A"]

weights = [1, 2, 1, 1, 3, 2, 1, 4, 1, 3,
           1, 1, 1, 4, 1, 3, 2, 2, 1, 2,
           1, 2, 1, 2, 1]


class Brick(Turtle):
    def __init__(self, x_cor, y_cor):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(stretch_wid=1.5, stretch_len=3)
        self.color(random.choice(color_list))
        self.goto(x=x_cor, y=y_cor)

        self.quantity = random.choice(weights)

        # Defining borders of the bricks
        self.left_wall = self.xcor() - 10
        self.right_wall = self.xcor() + 30
        self.upper_wall = self.ycor() + 15
        self.bottom_wall = self.ycor() - 15


class Bricks:
    def __init__(self):
        self.y_start = 0
        self.y_end = 240
        self.bricks = []
        self.create_all_lanes()

    def create_lane(self, y_cor):
        for i in range(-370, 390, 60):
            brick = Brick(i, y_cor)
            self.bricks.append(brick)

    def create_all_lanes(self):
        for i in range(self.y_start, self.y_end, 32):
            self.create_lane(i)
