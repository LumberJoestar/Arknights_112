
from operatorsClass import*
from graphicsHelpers import*
from cmu_112_graphics import *
from projectileClass import*
#A separate file containing all the sub operable game characters - the snipers

class Exusiai(Marksman):
    def __init__(self):
        super().__init__('Exusiai','Penguin Logistics',1673,630,161,14)
        self.projectile=Projectile(10,'yellow','red')

    
    def redraw(self,app,canvas):
        super().redraw(app,canvas)
        if self.isDeployed:
            if self.direction==(0,-1):
                canvas.create_image(self.x,self.y,image=ImageTk.PhotoImage(app.exusiai_back_attack))
            elif self.direction==(-1,0):
                canvas.create_image(self.x,self.y,image=ImageTk.PhotoImage(app.exusiai_left_attack))
            elif self.direction==(1,0) or self.direction==(0,1):
                canvas.create_image(self.x,self.y,image=ImageTk.PhotoImage(app.exusiai_right_attack))
        elif self.isDeployed==False:
            canvas.create_image(self.barX,self.barY,image=ImageTk.PhotoImage(app.exusiai_head))

class Fartooth(Deadeye):
    def __init__(self):
        super().__init__('Fartooth','Red Pine',1522,1296,163,22)
        self.projectile=Projectile(10,'green','yellow')

    
    def redraw(self,app,canvas):
        super().redraw(app,canvas)
        if self.isDeployed:
            if self.direction==(0,-1):
                canvas.create_image(self.x,self.y,image=ImageTk.PhotoImage(app.fartooth_back_attack))
            elif self.direction==(-1,0):
                canvas.create_image(self.x,self.y,image=ImageTk.PhotoImage(app.fartooth_left_attack))
            elif self.direction==(1,0) or self.direction==(0,1):
                canvas.create_image(self.x,self.y,image=ImageTk.PhotoImage(app.fartooth_right_attack))
        elif self.isDeployed==False:
            canvas.create_image(self.barX,self.barY,image=ImageTk.PhotoImage(app.fartooth_head))
    
    

