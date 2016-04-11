import serialBox, time, math

window_width = 80
window_height = 20

class Game:
    def __init__(self):
        self.speed = 1
        self.screen = serialBox.screen(window_width,window_height)
        self.screen.clear()
        self.scorePlayer1 = 0
        self.scorePlayer2 = 0
        self.scoreBoard = {}
        self.scoreBoard['player1'] = Score(window_width/2 - 7, 0, serialBox.colors.WHITE, self.screen, self.scorePlayer1)
        self.scoreBoard['player2'] = Score(window_width/2 + 2, 0, serialBox.colors.WHITE, self.screen, self.scorePlayer2)

        self.scoreBoard['player1'].draw()
        self.scoreBoard['player2'].draw()
        #Initiate variable and set starting positions
        #any future changes made within rectangles
        ball_x = int(window_width/2)
        ball_y = int(window_height/2)
        ball_radius = 1
        ball_color = serialBox.colors.GREEN
        self.ball = Ball(ball_x, ball_y, ball_radius, ball_color, 0.00009, self.screen)
        self.paddles = {}
        paddle_height = 3
        player1_paddle_x = 3
        player1_paddle_y = 3

       	player2_paddle_x = 77 
       	player2_paddle_y = 3

       	player1_color = serialBox.colors.RED
       	player2_color = serialBox.colors.BLUE

        self.paddles['player1'] = Paddle(player1_paddle_x, player1_paddle_y, paddle_height, player1_color, "vertical", self.screen)
        self.paddles['player2'] = Paddle(player2_paddle_x, player2_paddle_y, paddle_height, player2_color, "vertical", self.screen)

    def update(self):
        self.ball.move()
        if self.ball.hit_left():
            self.scorePlayer2 += 1
        elif self.ball.hit_right():
            self.scorePlayer1 += 1 
        if self.paddle_ball_collision():
            self.ball.bounce('x')

        self.scoreBoard['player1'].update_score(self.scorePlayer1)
        self.scoreBoard['player2'].update_score(self.scorePlayer2)

    def paddle_ball_collision(self):
        if self.ball.dir_x == 1 and self.ball.y >= self.paddles['player2'].y and self.ball.y <= (self.paddles['player2'].y + self.paddles['player2'].length) and self.ball.x >= (self.paddles['player2'].x):
            return True
        elif self.ball.dir_x == -1 and self.ball.y >= self.paddles['player1'].y and self.ball.y <= (self.paddles['player1'].y + self.paddles['player1'].length) and self.ball.x <= (self.paddles['player1'].x + 1):
            return True
        else:
            return False


#extend the line package 

class Paddle(serialBox.line):
    def __init__(self,x,y,length,color, orientation, screen):
        serialBox.line.__init__(self,x,y,length,color,orientation)
        self.screen = screen
        self.draw(self.screen)

    def move(self,y):
        if y < window_height - self.length and y > 0:
            if int(self.y != int(y)):
                self.clear(self.screen)
                self.y = y
                self.draw(self.screen)
            else:
                self.y = y

class Ball(serialBox.rect):
    """docstring for Ball"""
    def __init__(self, x, y, radius, color, speed, screen):
        super(Ball, self).__init__(x,y,radius,radius,color)
        self.speed = speed
        self.dir_x = -1
        self.dir_y = -1
        self.screen = screen
        self.draw(self.screen)

    def move(self):
        new_x = self.x + (self.dir_x * self.speed)
        new_y = self.y + (self.dir_y * self.speed)
        if int(new_x) != int(self.x) or int(new_y) != int(self.y):
            self.clear(self.screen)
            self.x = new_x
            self.y = new_y
            self.draw(self.screen)
        else:
            self.x = new_x
            self.y = new_y

        if self.hit_ceiling() or self.hit_floor():
            self.bounce('y')
        if self.hit_left() or self.hit_right():
            self.bounce('x')

    def bounce(self,axis):
        if axis == 'x':
            self.dir_x *= -1
        elif axis == 'y':
            self.dir_y *= -1

    def hit_ceiling(self):
        if self.dir_y == -1 and int(self.y) == 0: 
            return True
        else:
            return False

    def hit_floor(self):
        if self.dir_y == 1 and self.y >= self.screen.height - 1:
            return True
        else:
            return False

    def hit_left(self):
        if self.x <= 1:
            return True
        else:
            return False

    def hit_right(self):
        if self.x >= self.screen.width -1:
            return True
        else:
            return False


class Score(serialBox.text):
    def __init__(self, x, y, color, screen, value):
        super(Score, self).__init__(x,y,color, screen, value)

    def update_score(self, new_score):
        if self.value != new_score:
            self.clear()
            self.value = new_score
            self.draw()

game = Game()

import Tkinter as tk
root = tk.Tk()
while True:
    game.update()
    y = root.winfo_pointery()
    game.paddles['player1'].move(y/10)
    time.sleep(1/24)



print "\033[0m"