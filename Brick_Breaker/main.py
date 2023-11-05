from turtle import Screen
import time
from ball import Ball
from paddle import Paddle
from blocks import Block
from scoreboard import ScoreBoard

# ================ CREATE THE SCREEN ======================

screen = Screen()
screen.setup(500, 600)
screen.bgcolor("black")
screen.listen()
screen.tracer(0)

scoreboard = ScoreBoard()

#================= CREATE THE PADDLE =======================
paddle = Paddle()

#=================  CREATE BALL AND MAKE IT MOVE ===============
ball = Ball()
#================= CREATE AND POSITION THE BLOCKS================

blocks = []
for y in range(250, 0, -25):
    for x in range(-230, 230, 57):
        blocks.append(Block((x, y)))


#================= CONTROL THE PADDLE ========================
screen.onkey(key="Right", fun=paddle.move_right)
screen.onkey(key="Left", fun=paddle.move_left)
# screen.onkey(fun=paddle.move_up, key="Up")
# screen.onkey(fun=paddle.move_down, key="Down")

#=================  DETECT COLLISION WITH PADDLE ================
game_is_on = True

while game_is_on:
    time.sleep(0.09)
    screen.update()
    ball.move()
    
    # ======================= DETECT COLLISION WITH WALL ================================
    if ball.xcor() > 235 or ball.xcor() < -235:
        ball.bounce_x()
    elif ball.ycor() > 285:
        ball.bounce_y()
    
    if ball.distance(paddle) < 30 and ball.ycor() < -250 :
        ball.bounce_y()

    # ================  DETECT COLLISION WITH BRICK =================
    for block in blocks:
        if ball.distance(block) <= 25:
            # if 0 <= ball.heading() <= 180
            ball.bounce_y()
            # ball.bounce_brick()
            block.hideturtle()
            blocks.remove(block)


    #================= DETECT WHEN PADDLE MISSES ========================
    if ball.ycor() <= -290:
        game_is_on = False

    # ================ KEEP COUNT OF THE NUMBER OF BLOCKS =================
    if len(blocks) == 0:
        game_is_on = False


screen.exitonclick()