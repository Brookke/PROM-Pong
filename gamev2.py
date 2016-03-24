import serialBox, time

window_width = 80
window_height = 20

class Game:
    def __init__(self):
        self.speed = 5
        self.screen = serialBox.screen(window_width,window_height)
        self.scorePlayer1 = 0
        self.scorePlayer2 = 0
        #Initiate variable and set starting positions
        #any future changes made within rectangles
        ball_x = int(window_width/2)
        ball_y = int(window_height/2)
      
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



#extend the line package 

class Paddle(serialBox.line):
    def __init__(self,x,y,length,color, orientation, screen):
        serialBox.line.__init__(self,x,y,length,color,orientation)
        self.screen = screen
        self.draw(self.screen)

    def move(self,y):
        if y < window_height - self.length and y > 0:
            self.clear(self.screen)
            self.y = y
            self.draw(self.screen)

class Ball(serialBox.rect):
    """docstring for Ball"""
    def __init__(self, arg):
        super(Ball, self).__init__()
        
        

game = Game()
time.sleep(1)
import Tkinter as tk
root = tk.Tk()

def motion(event):
    x, y = event.x, event.y
    game.paddles['player1'].move(y/5)

root.bind('<Motion>', motion)
root.mainloop()



print "\033[0m"