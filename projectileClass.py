import math
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
        #Projectile direction
        self.dx,self.dy=0,0
        self.angle=0
        self.timeCount=0
    
    def appears(self):
        self.appear=True
        self.timeCount=0
    
    def redraw(self,app,canvas):
        if self.appear:
            canvas.create_oval(self.x-self.r,self.y-self.r,self.x+self.r,self.y+self.r,fill=self.color,outline=self.outline)
    
    def setDirection(self,tarX,tarY):
        self.appears()
        self.dx,self.dy=(tarX-self.x)/5,(tarY-self.y)/5
    
    def move(self):
        if self.appear:
            self.x+=self.dx
            self.y+=self.dy
    
    def isHit(self,tarX,tarY):
        if math.sqrt((tarX-self.x)**2+(tarY-self.y)**2)<=50 and self.appear:
            self.appear=False
            self.x=self.oX
            self.y=self.oY
            return True
    
    def timerFired(self,app):
        self.timeCount+=app.timerDelay/10
    

    
    

    



