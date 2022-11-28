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
        canvas.create_rectangle(100,100,200,200,fill='red')

