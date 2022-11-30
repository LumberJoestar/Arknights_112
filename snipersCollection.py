from operatorsClass import*
from graphicsHelpers import*
from cmu_112_graphics import *
#A separate file containing all the sub operable game characters - the snipers

class Exusiai(Marksman):
    def __init__(self):
        super().__init__('Exusiai','Penguin Logistics',1673,630,161,14)
    
    def redraw(self,app,canvas):
        #self.backAttack=loadAnimatedGif('Exusiai_Back_Attack.gif')
        #self.backIdle=loadAnimatedGif('Exusiai_Back_Idle.gif')
        #self.backStart=loadAnimatedGif('Exusiai_Back_Start.gif')
        #self.frontAttack=loadAnimatedGif('Exusiai_Front_Attack.gif')
        #self.frontDie=loadAnimatedGif('Exusiai_Front_Die.gif')
        #self.frontStart=loadAnimatedGif('Exusiai_Front_Start.gif')
        #photoImage=self.backAttack
        #canvas.create_image(200,200,image=photoImage)
        super().redraw(app,canvas)
            
        if self.isDeployed:
            canvas.create_rectangle(self.x-25,self.y-25,self.x+25,self.y+25,fill='red',outline='yellow',width=5)
        elif self.isDeployed==False:
            canvas.create_rectangle(self.barX-50,self.barY-50,self.barX+50,self.barY+50,fill='red',outline='yellow',width=5)
            canvas.create_text(self.barX,self.barY-25,text=self.name,fill='white')
            canvas.create_text(self.barX,self.barY+25,text='Marksman',fill='white')
    
    

