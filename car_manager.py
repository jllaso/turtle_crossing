from turtle import Turtle
import random

COLORS = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


class CarManager(Turtle):

    SPEED_BONUS = 0
    @classmethod
    def increase_global_speed(cls):
        cls.SPEED_BONUS += MOVE_INCREMENT

    def __init__(self, y=None):
        super().__init__()
        self.penup()
        self.shape("square")  # base vector shape
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.setheading(180)
        if y is None:
            y = random.randrange(-250, 251, 50)
        self.goto(280, y)
        self.color(random.choice(COLORS))
        self.base_speed = STARTING_MOVE_DISTANCE

    def move(self):
        # effective speed = base + global bonus
        self.forward(self.base_speed + CarManager.SPEED_BONUS)

