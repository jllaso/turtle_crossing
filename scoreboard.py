from turtle import Screen, Turtle
FONT = ('Courier', 24, 'normal')

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-270, 250)
        self.level = 1
        self.color('black')
        self.write(f"Level: {self.level}", False, font= FONT)



    def next_level(self):
        self.clear()
        self.level += 1
        self.write(f"Level = {str(self.level)}", False, font= FONT)

    def game_over(self):
        self.goto(-10, 0)
        self.write("GAME OVER", font = FONT)


