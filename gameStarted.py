from cmu_112_graphics import *
from operatorsClass import*
from enemyClass import*
from levelClass import*
from graphicsHelpers import*

#The Levels:
from level0_1 import*

###############################################################
#The gameStartMode
def gameStartMode_redrawAll(app,canvas):

    canvas.create_text(app.width/2,app.height/4,font='Arial 50 bold',text='Arknights')
    canvas.create_rectangle(app.width/2-40,app.height/3*2-15,
                            app.width/2+40,app.height/3*2+15,
                            fill='black')
    canvas.create_text(app.width/2,app.height/3*2,text='Start',font='Arial 26 bold',fill='white')

def gameStartMode_mousePressed(app,event):
    if app.width/2-40<event.x<app.width/2+40 and app.height/3*2-15<event.y<app.height/3*2+15:
        app.mode='level0_1Mode'
       






########################################################
#Main App
########################################################
def appStarted(app):
    app.mode='gameStartMode'
    app.timerDelay=33


runApp(width=1200,height=800)
