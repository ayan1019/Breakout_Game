from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from bricks import Bricks
from scoreboard import Scoreboard
from ui import UI
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Breakout Game")
screen.tracer(0)

# Creating the paddle and sending it to location
paddle = Paddle((0, -270))
ball = Ball()
bricks = Bricks()
scoreboard = Scoreboard(lives=5)
ui = UI()
ui.header()

game_paused = False
game_on = True


def pause_game():
    global game_paused
    if game_paused:
        game_paused = False
    else:
        game_paused = True


screen.listen()
screen.onkey(key="Left", fun=paddle.move_left)
screen.onkey(key="Right", fun=paddle.move_right)
screen.onkey(key="space", fun=pause_game)


# detect collision with left and right walls
def detect_collision_with_walls():
    global game_on

    # detect collision with left and right walls:
    if ball.xcor() < -380 or ball.xcor() > 370:
        ball.bounce(x_bounce=True, y_bounce=False)
        return

    # detect collision with upper walls
    if ball.ycor() > 270:
        ball.bounce(x_bounce=False, y_bounce=True)
        return

    # detect collision with bottom wall and reset ball position
    if ball.ycor() < -280:
        ball.reset()
        scoreboard.decrease_lives()
        if scoreboard.lives == 0:
            scoreboard.reset()
            game_on = False
            ui.game_over(win=False)
            return

        ui.change_color()
        return

def detect_collision_with_paddle():

    # check if ball's distance(from its middle)
    # from paddle(from its middle) is less than
    # width of paddle and ball is below a certain
    # coordinate to detect their collision
    if ball.distance(paddle) < 110 and ball.ycor() < -250:

        # paddle is on the right
        if paddle.xcor() > 0:
            if ball.xcor() > paddle.xcor():
                ball.bounce(x_bounce=True, y_bounce=True)
                return
            else:
                ball.bounce(x_bounce=False, y_bounce=True)

        # paddle is on the left
        elif paddle.xcor() < 0:

            if ball.xcor() < paddle.xcor():
                # If ball hits paddles left side it
                # should go back to left
                ball.bounce(x_bounce=True, y_bounce=True)
                return

            else:
                ball.bounce(x_bounce=False, y_bounce=True)

        # paddle is the middle
        else:
            if ball.xcor()> paddle.xcor():
                ball.bounce(x_bounce=True, y_bounce=True)
                return
            elif ball.xcor() < paddle.xcor():
                ball.bounce(x_bounce=True, y_bounce=True)
                return
            else:
                ball.bounce(x_bounce=False, y_bounce=True)
                return

# detecting collision with bricks
def detect_collision_with_bricks():

    for brick in bricks.bricks:
        if ball.distance(brick) < 40:
            brick.quantity -= 1
            if brick.quantity == 0:
                brick.clear()
                brick.goto(2000, 2000)
                bricks.bricks.remove(brick)

            # detect collision with left wall
            if ball.xcor() < brick.left_wall:
                ball.bounce(x_bounce=True, y_bounce=False)

            # detect collision with right wall
            elif ball.xcor() > brick.right_wall:
                ball.bounce(x_bounce=True, y_bounce=False)

            # detect collision from bottom
            elif ball.ycor() < brick.bottom_wall:
                ball.bounce(x_bounce=False, y_bounce=True)

            # detect collision from top
            elif ball.ycor() < brick.upper_wall:
                ball.bounce(x_bounce=False, y_bounce=True)


while game_on:

    if not game_paused:
        screen.update()
        time.sleep(0.01)
        ball.move()

        detect_collision_with_walls()

        detect_collision_with_paddle()

        detect_collision_with_bricks()

        if len(bricks.bricks) == 0:
            ui.game_over(win=True)

    else:
        ui.pause()



screen.exitonclick()