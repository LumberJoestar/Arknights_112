from enemyClass import*
from operatorsClass import*
from cmu_112_graphics import *
from graphicsHelpers import*

#########################################################################
#The Projectile Class
#########################################################################
class Projectile():
    def __init__(self,r,color,outline):
        self.r=r
        self.color=color
        self.outline=outline
        self.x,self.y=None,None
        self.oX,self.oY=self.x,self.y
        self.appear=False
        self.timeCount=0
    
    def appears(self):
        self.appear=True
        self.timeCount=0
    
    def redraw(self,app,canvas):
        if self.appear:
            canvas.create_oval(self.x-self.r,self.y-self.r,self.x+self.r,self.y+self.r,fill=self.color,outline=self.outline)
    
    def move(self,tarX,tarY):
        dx,dy=int((tarX-self.x)/2),int((tarY-self.y)/2)
        self.x,self.y=self.x+dx,self.y+dy
        if almostEqual(self.timeCount%1000,0,epsilon=10**-7):
            self.x=self.oX
            self.y=self.oY
            self.appear=False
    
    def timerFired(self,app):
        self.timeCount+=app.timerDelay/10
    

    
    

    



