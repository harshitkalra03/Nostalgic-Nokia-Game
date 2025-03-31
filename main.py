from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

game_is_on = True

canvas_height = 600
canvas_width = 600

canvas = Screen()
canvas.setup(width = canvas_width, height = canvas_height)
canvas.bgcolor("black")
canvas.title("Welcome to the Snake🐍 Game🏃‍➡️")
canvas.tracer(n=0)  

snake = Snake()
food = Food()
scoreboard = ScoreBoard()
canvas.listen()

canvas.onkeypress(fun = snake.up, key = "Up")
canvas.onkeypress(fun = snake.down, key = "Down")
canvas.onkeypress(fun = snake.left, key = "Left")
canvas.onkeypress(fun = snake.right, key = "Right")


while game_is_on:
    canvas.update()
    time.sleep(0.05)
    snake.move()   

    # Detect collison of snake with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # Detect Collision with wall
    if snake.head.xcor() > 295 or snake.head.xcor() < -300 or snake.head.ycor() > 270 or snake.head.ycor() < -295:
        scoreboard.reset()
        snake.reset()
        
    # Detect Collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            snake.reset()
            scoreboard.reset()
     # If head collides with any segment in the tail, then trigger game over

canvas.exitonclick()