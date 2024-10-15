from turtle import Turtle, Screen
from snake import Snake
import time
from snake_food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.title("SNAKEEEEEE")
screen.setup(height=600, width=600)
screen.tracer(0)
screen.listen()
food = Food()
# coordinate = [(0,0),(-20, 0), (-40,0)]
# segment = []
# for x in coordinate:
#     new_segment = Turtle(shape="square")
#     new_segment.color("white")
#     new_segment.penup()
#     new_segment.goto(x)
#     segment.append(new_segment)

tim = Snake()
score = Scoreboard()
screen.onkey(key="Up", fun=tim.go_up)
screen.onkey(key="Left", fun=tim.go_left)
screen.onkey(key="Down", fun=tim.go_down)
screen.onkey(key="Right", fun=tim.go_right)
while tim.boundaries():
    screen.update()
    time.sleep(0.1)
    tim.move()
    if tim.head.distance(food) < 15:
        food.refresh()
        tim.extend()
        score.get_score()
score.game_over()




# move = True
# while move:
#     screen.update()
#     time.sleep(0.1)
#     for position in range(len(segment)-1, 0, -1):
#         new_xcor = segment[position - 1].xcor()
#         new_ycor = segment[position - 1].ycor()
#         segment[position].goto(new_xcor, new_ycor)
#     segment[0].fd(10)
#     if segment[0].xcor() > 280 or segment[0].ycor() > 280:
#         move = False



screen.exitonclick()