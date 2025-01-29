import turtle as tr
import time
import winsound


class Player:
    def __init__(self):
        self.player = None


    def create_player(self, x, y, up_key, down_key):
        t = tr.Turtle()

        t.speed(0)
        t.shape("square")
        t.color("white")
        t.shapesize(stretch_wid=5, stretch_len=1)
        t.penup()
        t.goto(x, y)

        window.onkey(lambda: self.move_up(), up_key)
        window.onkey(lambda: self.move_down(), down_key)

        self.player = t


    def move_up(self):
        if self.player.ycor() < 200:
            self.player.goto(self.player.xcor(), self.player.ycor() + 20)

    
    def move_down(self):
        if self.player.ycor() > -200:
            self.player.goto(self.player.xcor(), self.player.ycor() - 20)


    def get_coordinates(self):
        return self.player.xcor(), self.player.ycor()


class Ball:
    def __init__(self):
        self.ball = None


    def create_ball(self):
        t = tr.Turtle()

        t.speed(1)
        t.shape("circle")
        t.color("white")
        t.penup()
        t.left(45.0)

        self.ball = t


    def move_forward(self):
        self.ball.forward(2)


    def detect_collision(self, p1_x, p1_y, p2_x, p2_y, score):
        global pace, p1_score, p2_score
    
        if self.ball.ycor() > 240 and self.ball.heading() == 45.0:
            winsound.Beep(600, 20)
            self.ball.right(90)
        elif self.ball.ycor() > 240 and self.ball.heading() == 135.0:
            winsound.Beep(600, 20)
            self.ball.left(90)
        elif self.ball.ycor() < -231 and self.ball.heading() == 225.0:
            winsound.Beep(600, 20)
            self.ball.right(90)
        elif self.ball.ycor() < -231 and self.ball.heading() == 315.0:
            winsound.Beep(600, 20)
            self.ball.left(90)

        if 0 < self.ball.xcor() - p1_x < 20 and p1_y + 47 > self.ball.ycor() and p1_y - 50 < self.ball.ycor() and self.ball.heading() == 225.0:
            winsound.Beep(600, 20)
            self.ball.left(90)
            pace *= 0.75
        elif 0 < self.ball.xcor() - p1_x < 20 and p1_y + 47 > self.ball.ycor() and p1_y - 50 < self.ball.ycor() and self.ball.heading() == 135.0:
            winsound.Beep(600, 20)
            self.ball.right(90)
            pace *= 0.75
        elif 0 < p2_x - self.ball.xcor() < 20 and p2_y + 47 > self.ball.ycor() and p2_y - 50 < self.ball.ycor() and self.ball.heading() == 45.0:
            winsound.Beep(600, 20)
            self.ball.left(90)
            pace *= 0.75
        elif 0 < p2_x - self.ball.xcor() < 20 and p2_y + 47 > self.ball.ycor() and p2_y - 50 < self.ball.ycor() and self.ball.heading() == 315.0:
            winsound.Beep(600, 20)
            self.ball.right(90)
            pace *= 0.75

        if p1_x >= self.ball.xcor():
            p2_score += 1
            score.clear()
            score.write(f"Player 1: {p1_score}    Player 2: {p2_score}", font=("Arial", 16, "bold"))

            self.ball.hideturtle()
            self.create_ball()
            
            pace = 0.02
        elif p2_x <= self.ball.xcor():
            p1_score += 1
            score.clear()
            score.write(f"Player 1: {p1_score}    Player 2: {p2_score}", font=("Arial", 16, "bold"))

            self.ball.hideturtle()
            self.create_ball()
            
            pace = 0.02


def pong_game():
    global window, pace, p1_score, p2_score
    window = tr.Screen()
    window.listen()
    window.title("Pong Game")
    window.bgcolor("black")
    window.setup(width=700, height=500)

    tr.tracer(0)

    player_1 = Player()
    player_1.create_player(-300, 0, "w", "s")

    player_2 = Player()
    player_2.create_player(290, 0, "Up", "Down")

    ball = Ball()
    ball.create_ball()

    p1_score = 0
    p2_score = 0
    score = tr.Turtle()
    score.goto(-120, 200)
    score.color("white")
    score.write(f"Player 1: {p1_score}    Player 2: {p2_score}", font=("Arial", 16, "bold"))
    score.hideturtle()

    pace = 0.02
    while True:
        p1_x, p1_y = player_1.get_coordinates()
        p2_x, p2_y = player_2.get_coordinates()

        ball.move_forward()
        ball.detect_collision(p1_x, p1_y, p2_x, p2_y, score)

        tr.update()
        time.sleep(pace)


pong_game()
tr.done()
