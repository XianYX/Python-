from Tkinter import *
import random 
class SnakeGame:
    

    def __init__(self):
        # moving step for snake and food
        self.step=15
        # game score
        self.gamescore=0
        
        # to initialize the snake in the range of (x1,y1,x2,y1)                
        r=random.randrange()
        self.snakeX=[]
        self.snakeY=[]
        
        # to initialize the moving direction
        self.snakeDirection = ' '  
        self.snakeMove = []
        # to draw the game frame 
        window = Tk()
        window.geometry("600x400+10+10")
        window.maxsize(600,400)
        window.minsize(600,400)
        window.title("Snake game")
        
        self.frame1=Frame(... ...)
        self.frame2=Frame(... ...)
        self.canvas=Canvas(... ...)
        self.score_label=Label(... ...)
        
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
        pass
    
    def draw_score(self):
        self.score()                        # score model
        self.score_label.config(... ...)    # score view
        
    def draw_food(self):
        self.canvas.delete("food")
        self.foodx,self.foody=self.random_food()    #food model
        self.canvas.create_rectangle(... ...,fill=... ,tags="food")     #food view

    def draw_snake(self):
        self.canvas.delete("snake")
        x,y=self.snake()                    # snake model
        for i in range(len(x)):             # snake view
            self.canvas.create_rectangle(... ..., fill=...,tags='snake')    
    
    "=== Model Part ==="
    # food model
    def random_food(self):      
        pass
    
    # snake model
    def snake(self):
        pass
        
    #score model    
    def score(self):
        pass
        
    
    "=== Control Part ==="     
    def iseated(self):
        pass
    
    def isdead(self):
        pass
    
    def move(self,event):
        pass
            
    def play(self):
        pass  
    
    def gameover(self):
        pass

    def restart(self,event):
        pass
    
SnakeGame()
