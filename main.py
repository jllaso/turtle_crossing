import random
from turtle import Screen
import time
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

LANES = list(range(-250, 251, 50))  # discrete y positions
MIN_GAP = 70

player = Player()
screen = Screen()
scoreboard = Scoreboard()
screen.setup(600, 600)
screen.listen()
screen.onkey(player.move, 'Up')
screen.tracer(0)


game_is_on = True
cars = []

def can_spawn_in_lane(y_lane):
    # True if no car in this lane is too close to the right edge (spawn point at x=280)
    for c in cars:
        if abs(c.ycor() - y_lane) < 1e-6:
            # c.xcor() near 280 means it was just spawned; ensure space
            if (280 - c.xcor()) < MIN_GAP:
                return False
    return True

while game_is_on:
    time.sleep(0.1)
    screen.update()

    # maybe create 0 or 1 cars this frame
    if random.randint(0, 1) == 1:
        y_choice = random.choice(LANES)
        if can_spawn_in_lane(y_choice):
            cars.append(CarManager(y=y_choice))


    # move cars and remove off-screen ones
    alive = []
    for c in cars:
        if c.xcor() < -320.0:          # off left edge
            c.hideturtle()
            # don't append to alive -> effectively removed
        else:
            if c.distance(player) < 20.0:
                game_is_on = False
                scoreboard.game_over()
            c.move()
            alive.append(c)
    cars = alive

    if player.crossed():
        CarManager.increase_global_speed()  # affects ALL cars now
        scoreboard.next_level()
screen.exitonclick()
