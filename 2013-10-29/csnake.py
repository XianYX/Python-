# -*- coding: utf-8 -*-
"""
Created on Sat Nov 02 17:00:05 2013

@author: lenovo
"""

from Tkinter import * #import random class SnakeGame:
import random
class snakeGame:
    def __init__(self): 
        # game score
        self.gamescore=0
        self.gamelevel=1
        # moving step for snake and food self.step=15     
        self.step=15
        # to initialize the snake in the range of (x1,y1,x2,y1) r=random.randrange()         
        self.snakeX=[150,150+self.step,150+self.step*2]
        self.snakeY=[240,240,240]
        self.random_foodx=random.randrange(15,573,self.step)
        self.random_foody=random.randrange(15,358,self.step)
        self.foodX=[self.random_foodx]
        self.foodY=[self.random_foody]
        self.gamespeed=0
        # to initialize the moving direction
        self.snakeDirection = 'left'
        # to draw the game frame 
        window = Tk()
        window.geometry("600x400+10+10")
        window.maxsize(600,400)
        window.minsize(600,400)
        window.title("Snake game")
        self.frame1=Frame(window,width=600,height=380)
        self.frame2=Frame(window,width=600,height=20)
        self.canvas=Canvas(self.frame1,bg='yellow',width=600,height=380)
        self.score_label=Label(self.frame2,text='score=0,level=1')
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
        #draw wall    
    def draw_wall(self):
        self.canvas.create_line((13,13),(13,373),(13,373),(588,373),(588,373),(588,13),(588,13),(13,13),fill='blue',width=3)
    #draw score
    def draw_score(self): 
        self.score() # score model
        self.score_label.config(self.score_label,text='score='+str(self.gamescore)+'level='+str(self.gamelevel))
        if self.gamelevel<17:
            self.gamespeed=200-(self.gamelevel-1)*10
        else:
            self.gamespeed=50
    
    #draw food
    def draw_food(self): 
        self.random_food()
        self.canvas.create_rectangle([[self.foodx,self.foody],[self.foodx+self.step,self.foody+self.step]],fill='red',outline='black',tags="food") #food view
    #draw snake
    def draw_snake(self):
        self.canvas.delete("snake")
        self.snake()
        for i in range(len(self.snakeX)): # snake view 
            self.canvas.create_rectangle([[self.snakeX[i],self.snakeY[i]],[self.snakeX[i]+self.step,self.snakeY[i]+self.step]],fill='orange',outline='black',width=1,tags='snake')
    "=== Model Part ===" 
    #food model    
    def random_food(self):
        self.canvas.delete("food")
        for i in range(0,self.gamelevel):
            self.foodx=random.randrange(15,573,self.step)
            self.foody=random.randrange(15,358,self.step)
            if i<=len(self.foodX):
                self.foodX[i]=self.foodx
                self.foodY[i]=self.foody
            else:
                self.random_food()
                self.foodX.insert(i,self.foodx)
                self.foodY.insert(i,self.foody)
        
    #score model    
    def snake(self):
        self.canvas.bind('<Key>',self.move)


    #score model
    def score(self):
        if self.iseated==True:
            self.gamescore=self.gamescore+10
            if self.gamescore/10.0==1:
                self.gamelevel=self.gamelevel+1                
                
    "=== Control Part ==="
    def iseated(self):
        for i in range(0,len(foodX)+1):
            if foodX[i]==snakeX[0] and foodY[i]==snakeY[0]:
                return true
                
    def isdead(self):
        if self.snakeX[0] < 15 or self.snakeX[0] > 573 or self.snakeY[0] < 15 or self.snakeY[0] > 358:
            return True
        for i in range(1,len(self.snakeX)-1):
            if self.snakeX[i] == self.snakeX[0] and self.snakeY[i] == self.snakeY[0]:
                return True       
        return False
        
    #contronl direction 
    def move(self,event):
        for i in range(len(self.snakeX)):
            if event.keycode=='38' or event.keycode=='87' and snakeDirection!='down':
                self.snakeDirection=='up'
                self.snakeY[i]=self.snakeY[i]+self.step
            elif event.keycode=='40' or event.keycode=='83' and snakeDirection!='up':
                self.snakeDirection=='down'
                self.snakeY[i]=self.snakeY[i]-self.step
            elif event.keycode=='37' or event.keycode=='65' and snakeDirection!='right':
                self.snakeDirection=='left'
                self.snakeX[i]=self.snakeX[i]-self.step
            elif event.keycode=='38' or event.keycode=='87' and snakeDirection!='left':
                self.snakeDirection=='right'   
                self.snakeX[i]=self.snakeX[i]+self.step
    #bunding event
    def play(self):
        while True:
            self.canvas.bind('<Key>',self.move)
            self.canvas.focus_set()
            
            if self.isdead()==True:                    
                break
            self.draw_snake()
            self.canvas.after(self.gamespeed)
            self.canvas.update()
        self.gameover()
        
    def gameover(self):
        canvas.delete('food')
        canvas.delete('snake')
        canvas.create_text(300,100,text='GAMEOVER',font='Verdana 30 bold',tags='text')
        canvas.create_text(300,200,text='Your score = '+str(self.gamescore)+',and your level ='+str(self.gamelevel),font='Verdana 30 bold',tags='text')
        canvas.create_text(300,275,text='Press T to try again',tags='text')
        canvas.bind('<Key>',restart)
    def restart(self,event):
        if event.keycode==84:
            canvas.delete('text')
            # game score
        self.gamescore=0
        # moving step for snake and food self.step=15     
        self.step=15
        # to initialize the snake in the range of (x1,y1,x2,y1) r=random.randrange()         
        self.snakeX=[150,150+step,150+step*2]
        self.snakeY=[240,240,240]
        self.random_foodx=random.randrange(15,573,self.step)
        self.random_foody=random.randrange(15,358,self.step)
        self.foodX=[random_foodx]
        self.foodY=[random_foody]
        # to initialize the moving direction
        self.snakeDirection = 'left'
                
snakeGame()   