from operatorsClass import*
from graphicsHelpers import*
from cmu_112_graphics import *
#A separate file containing all the sub operable game characters - the casters

class Eyjafjalla(Core):
    def __init__(self):
        super().__init__('Eyjafjalla','Rhodes Island',1743,735,122,21)
    
    def redraw(self,app,canvas):
        if self.isDeployed:
            canvas.create_rectangle(self.x-25,self.y-25,self.x+25,self.y+25,fill='red',outline='yellow',width=5)
        elif self.isDeployed==False:
            canvas.create_rectangle(self.barX-50,self.barY-50,self.barX+50,self.barY+50,fill='darkred',outline='white',width=5)
            canvas.create_text(self.barX,self.barY-25,text=self.name,fill='white')
            canvas.create_text(self.barX,self.barY+25,text='Core',fill='white')