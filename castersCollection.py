from operatorsClass import*
from graphicsHelpers import*
from cmu_112_graphics import *
from projectileClass import*
#A separate file containing all the sub operable game characters - the casters

class Eyjafjalla(Core):
    def __init__(self):
        super().__init__('Eyjafjalla','Rhodes Island',1743,735,122,21)
        self.projectile=Projectile(10,'darkred','yellow')

    def redraw(self,app,canvas):
        super().redraw(app,canvas)
        if self.isDeployed:
            if self.direction==(0,-1):
                canvas.create_image(self.x,self.y,image=ImageTk.PhotoImage(app.eyjafjalla_back_attack))
            elif self.direction==(-1,0):
                canvas.create_image(self.x,self.y,image=ImageTk.PhotoImage(app.eyjafjalla_left_attack))
            elif self.direction==(1,0) or self.direction==(0,1):
                canvas.create_image(self.x,self.y,image=ImageTk.PhotoImage(app.eyjafjalla_right_attack))
        elif self.isDeployed==False:
            canvas.create_image(self.barX,self.barY,image=ImageTk.PhotoImage(app.eyjafjalla_head))