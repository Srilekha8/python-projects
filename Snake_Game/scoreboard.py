from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("highscore.txt") as data:
            self.high_score = int(data.read())
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.update_board()

    def update_score(self):
        self.score+=1
        self.update_board()

    def update_board(self):
        self.clear()
        self.write(f'Score = {self.score} High Score {self.high_score}', False, align="center", font=("Arial", 24, "normal"))


    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("GAME OVER", False, align="center", font=("Arial", 24, "normal"))


    def reset(self):
        if self.score>self.high_score:
            self.high_score = self.score
            with open("highscore.txt",mode="w") as data:
                data.write(str(self.score))
        self.score = 0
        self.clear()
        self.update_board()