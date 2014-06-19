#-* coding: gbk -*
from Tkinter import *
import random 
import sys
class SnakeGame:
    """
    It will go one more step before turning
    """

    def __init__(self):
        # moving step for snake and food
        self.step = 15
        # game score
        self.gamescore = 0
        # game level
        self.gamelevel = 0
        self.leveltime = 510
        self.firststarted = True
        # to initialize the snake in the range of (x1,y1,x2,y1)                
        #r=random.randrange(29, 540, step = 15)
        r = 29 + 15 * 15
        self.snakeX=[r, r + self.step, r + self.step*2]
        self.snakeY=[150,150,150]
        
        # to initialize the moving direction
        # self.snakeMove[1]=up [2]=down [3]=left [4]=right; [0]=dx, [1]=dy
        self.snakeDirection = 3  #go left normally
        self.snakeMove = [[], [0, -self.step], [0, self.step], [-self.step, 0], [self.step, 0]]

        # to draw the game frame
        window = Tk()
        window.geometry("600x400+10+10")
        window.maxsize(600,400)
        window.minsize(600,400)
        window.title("snake game")
        self.frame1=Frame(window, borderwidth = 4, relief = RIDGE)
        self.frame2=Frame(window, borderwidth = 2, relief = RAISED, bg = "white")
        self.canvas=Canvas(self.frame1, width = 600, height = 368, bg = "yellow")
        self.score_label=Label(self.frame2)
        
        self.frame1.pack()
        self.frame2.pack(fill=BOTH)
        self.score_label.pack(side=LEFT)
        self.canvas.pack(fill=BOTH)
         
        self.draw_wall()
        self.draw_score()
        self.draw_food()
        self.draw_snake()
        
        self.play()
        
        window.mainloop()
    "=== View Part ==="        
    def draw_wall(self):
        """
            get a 570*345 game area:
            (14,15)   (584,15)
            (14,360)  (584,360)
        """
        self.canvas.create_line(11,10,
                                11,360, width = 6, fill = "blue")
        self.canvas.create_line(8,364,
                                590,364, width = 8, fill = "blue")
        self.canvas.create_line(587,10,
                                587,360, width = 6, fill = "blue")
        self.canvas.create_line(8,12,
                                590,12, width = 6, fill = "blue")
    def draw_score(self):
        #self.score()                        # score model
        self.score_label.config(text = "Level: " + str(self.gamelevel) \
        + " Score: " + str(self.gamescore))    # score view
        
    def draw_food(self):
        self.canvas.delete("food")
        self.foodx,self.foody=self.random_food()    #food model
        self.canvas.create_rectangle(self.foodx, self.foody, 
                                     self.foodx + self.step, self.foody + self.step, fill="red" , tags="food")     #food view

    def draw_snake(self):
        x,y=self.snake()                    # snake model
        if not self.isdead():
            self.canvas.delete("snake")
            for i in range(0,len(x)):             # snake view
                self.canvas.create_rectangle(x[i], y[i],
                                             x[i]+self.step, y[i]+self.step, \
                                             fill = "orange", tags = "snake")
        else:
            self.gameover()
    "=== Model Part ==="
    # food model
    def random_food(self):      
        while True:
            x, y = random.randrange(14,570, step = 15), random.randrange(15, 346, step = 15)
            if not (x in self.snakeX) and not (y in self.snakeY):
                return x, y
    # snake model
    def snake(self, mode = "forward"):
        """   
            Calculate next position of every part according to direction.
        """        
        length = len(self.snakeX)
        if mode == "back":
            for i in range(0, len(self.snakeX)-1):
                self.snakeX[i] = self.snakeX[i+1]
                self.snakeY[i] = self.snakeY[i+1]
            self.snakeX[len(self.snakeX)-1] -= self.snakeMove[self.snakeDirection][0]
            self.snakeY[len(self.snakeY)-1] -= self.snakeMove[self.snakeDirection][1]
        else:
            for i in range(length-1, 0, -1):
                self.snakeX[i] = self.snakeX[i-1]
                self.snakeY[i] = self.snakeY[i-1]
            self.snakeX[0] += self.snakeMove[self.snakeDirection][0]
            self.snakeY[0] += self.snakeMove[self.snakeDirection][1]
        if self.isdead():
            self.gameover()
        return self.snakeX, self.snakeY
        
    #score model    
    def score(self):
        """
            When the snake scores.
        """
        self.gamescore += 10
        self.gamelevel = self.gamescore / 100
        if self.gamelevel > 50:
            self.gamelevel = 50
        self.leveltime = 510 - self.gamelevel * 10
        self.snakeX.append(2*self.snakeX[0] - self.snakeX[1])
        self.snakeY.append(2*self.snakeY[0] - self.snakeY[1])
        
    
    "=== Control Part ==="     
    def iseated(self):
        self.score()
        self.draw_score()
        self.draw_food()
        
    def isdead(self):
        if self.snakeX[0] < 14 or self.snakeX[0] > 569 or self.snakeY[0] < 15 or self.snakeY[0] > 345:
            return True
        
        length = len(self.snakeX)
        for i in range(length-1, 0, -1):
            if self.snakeX[i] == self.snakeX[0] and self.snakeY[i] == self.snakeY[0]:
                return True
        
        return False
        
    def move(self,event):

        if (event.keycode == 38 or event.char == 'w') \
          and (self.snakeDirection == 3 or self.snakeDirection == 4):
            #self.back()
            self.snake("back")
            self.snakeDirection = 1
            self.draw_snake()
            self.canvas.update()
                
        elif (event.keycode == 40 or event.char == 's') \
          and (self.snakeDirection == 3 or self.snakeDirection == 4):
            self.snake("back")
            self.snakeDirection = 2
            self.draw_snake()
            self.canvas.update()
                        
        elif (event.keycode == 37 or event.char == 'a') \
          and (self.snakeDirection == 1 or self.snakeDirection == 2 or self.firststarted):
            self.snake("back")
            self.snakeDirection = 3
            self.draw_snake()
            self.canvas.update()                       
        
        elif (event.keycode == 39 or event.char == 'd') \
          and (self.snakeDirection == 1 or self.snakeDirection == 2):
            self.snake("back")
            self.snakeDirection = 4
            self.draw_snake()
            self.canvas.update()
            
        self.firststarted = False
        
    def play(self):
        self.canvas.config(highlightthickness = 0)
        self.canvas.focus_set()
        self.firststarted = True
        self.canvas.bind("<Key>", self.move)
        while not self.isdead():
                self.draw_score()
                if self.snakeX[0]+self.snakeMove[self.snakeDirection][0]== self.foodx and self.snakeY[0]+self.snakeMove[self.snakeDirection][1] == self.foody:
                    self.iseated()
                self.draw_snake()
                self.canvas.update()
                
                self.canvas.after(self.leveltime)
        
    def gameover(self):
        self.canvas.create_text(300, 150, \
          text = "You lose! Score: " + str(self.gamescore) \
          + ", level: " + str(self.gamelevel), \
          font = "Times 20 bold", tags = "lose")
        self.score_label.config(text = "Press <q> to quit, any other key to restart...")
        self.canvas.bind("<Key>", self.restart)
    def restart(self,event):
        if event.char != 'q':
            self.canvas.delete(ALL)
            #re-initialize
            self.gamescore = 0
            self.gamelevel = 0
            self.leveltime = 510
            r = 29 + 15 * 15
            self.snakeX=[r, r + self.step, r + self.step*2]
            self.snakeY=[150,150,150]
            self.snakeDirection = 3
            self.draw_wall()
            self.draw_score()
            self.draw_food()
            self.draw_snake()
            
            self.play()
        else:
            sys.exit()
SnakeGame()