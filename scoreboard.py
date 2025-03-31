from turtle import Turtle

ALIGNMENT = "Center"
FONT = ("Verdana", 20, "normal")

class ScoreBoard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.ht()
        self.score = 0
        self.high_score = 0
        self.penup()
        self.goto(0, 270)
        self.pencolor("white")
        self.update_scoreboard()
        
    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", move = False, align = ALIGNMENT, font = FONT) 
        
    def increase_score(self):
        self.score += 1
        if self.score > self.high_score:
            self.high_score += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto((0,0))
        self.write("Game Over", move = False, align = ALIGNMENT, font = FONT)
    
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.update_scoreboard()