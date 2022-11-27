from cmu_112_graphics import *
from levelClass import*
from enemyClass import*
from operatorsClass import*

def level0_1Mode_redrawAll(app,canvas):
    canvas.create_oval(app.width/2-10,app.height/2-10,app.width/2+10,app.height/2+10,fill='black')