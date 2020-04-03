import turtle
import os

class Pong:
    #initialize game with 0 for human control or 1 for AI control 
    def __init__(self, player=0, train=False):
        self.player = player
        self.train = train 
        self.score_a = 0
        self.score_b = 0
    
    def paddle_up(self, paddle):
        y = paddle.ycor()
        y += 20
        paddle.sety(y)

    def paddle_down(self, paddle):
        y = paddle.ycor()
        y -= 20
        paddle.sety(y)

    def draw_screen(self):
        self.wn = turtle.Screen()
        self.wn.title("Pong")
        self.wn.bgcolor("black")
        self.wn.setup(width=800, height=600)
        self.wn.tracer(0)
    
    def draw_paddles(self):
        #Paddle A
        self.paddle_a = turtle.Turtle()
        self.paddle_a.speed(0)
        self.paddle_a.shape("square")
        self.paddle_a.color("white")
        self.paddle_a.shapesize(stretch_wid=5,stretch_len=1)
        self.paddle_a.penup()
        self.paddle_a.goto(-350, 0)

        # Paddle B
        self.paddle_b = turtle.Turtle()
        self.paddle_b.speed(0)
        self.paddle_b.shape("square")
        self.paddle_b.color("white")
        self.paddle_b.shapesize(stretch_wid=5,stretch_len=1)
        self.paddle_b.penup()
        self.paddle_b.goto(350, 0)

    def draw_ball(self):
          # Ball
        self.ball = turtle.Turtle()
        self.ball.speed(0)
        self.ball.shape("square")
        self.ball.color("white")
        self.ball.penup()
        self.ball.goto(0, 0)
        self.ball.dx = 2
        self.ball.dy = 2
    
    def draw_pen(self):
         # Pen
        self.pen = turtle.Turtle()
        self.pen.speed(0)
        self.pen.shape("square")
        self.pen.color("white")
        self.pen.self.penup()
        self.pen.hideturtle()
        self.pen.goto(0, 260)
        self.pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))





    
    def play(self):
       self.draw_screend()
       self.draw_paddles()
       self.draw_pen()

       while True:
            self.wn.update()
            
            # Move the ball
            self.ball.setx(self.ball.xcor() + self.ball.dx)
            self.ball.sety(self.ball.ycor() + self.ball.dy)

            # Border checking

            # Top and bottom
            if self.ball.ycor() > 290:
                self.ball.sety(290)
                self.ball.dy *= -1
                
            
            elif self.ball.ycor() < -290:
                self.ball.sety(-290)
                self.ball.dy *= -1
                

            # Left and right
            if self.ball.xcor() > 350:
                score_a += 1
                pen.clear()
                pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
                self.ball.goto(0, 0)
                self.ball.dx *= -1

            elif self.ball.xcor() < -350:
                score_b += 1
                pen.clear()
                pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
                self.ball.goto(0, 0)
                self.ball.dx *= -1

            # Paddle and self.ball collisions
            if self.ball.xcor() < -340 and self.ball.ycor() < self.paddle_a.ycor() + 50 and self.ball.ycor() > self.paddle_a.ycor() - 50:
                self.ball.dx *= -1 
                
            
            elif self.ball.xcor() > 340 and self.ball.ycor() < self.paddle_b.ycor() + 50 and self.ball.ycor() > self.paddle_b.ycor() - 50:
                self.ball.dx *= -1