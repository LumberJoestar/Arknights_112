from cmu_112_graphics import *
from operatorsClass import*
from enemyClass import*
from levelClass import*
from graphicsHelpers import*
from projectileClass import*
#The operators
from snipersCollection import*
from castersCollection import*

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
        app.timerCount=0
        map=[[Path(),Path(),Path(),Path(),Path(),Origin(),Path(),Path(),Wall()],
         [Path(),Wall(),Path(),HighLand(),Wall(),Path(),Wall(),Path(),Wall()],
         [Path(),Path(),Path(),Path(),Path(),Destination(),Path(),Path(),Path()],
         [Wall(),Path(),HighLand(),Path(),Wall(),Path(),Fence(),HighLand(),Path()],
         [Destination(),NPath(),Path(),Path(),HighLand(),Path(),HighLand(),HighLand(),Origin()],
         [Wall(),Wall(),Wall(),Wall(),Wall(),Wall(),Wall(),Wall(),Wall()]]
        
        originiumSlug1=OriginiumSlug(1,(0,5),(2,5),1,[(0,0),(2,0),(3,1)])
        originiumSlug2=OriginiumSlug(2,(4,8),(4,0),2,[(0,0)])
        originiumSlug3=OriginiumSlug(3,(4,8),(4,0),3,[(0,0)])
        soldier1=Soldier(4,(4,8),(4,0),1,[(0,0)])
        heavy1=heavyGearDefender(5,(4,8),(4,0),15,[(0,7),(0,0)])
        
        Exusi=Exusiai()
        Eyja=Eyjafjalla()
        app.level=Level(map,[originiumSlug1,originiumSlug2,originiumSlug3,soldier1,heavy1],[Exusi,Eyja])
        app.level.cost=30
        for enemy in app.level.enemies:
            enemy.path=enemy.solveEnemyPath(app.level)
            enemy.direction=(enemy.path[1][1]-enemy.path[0][1],enemy.path[1][0]-enemy.path[0][0])
        app.level.setOriginDimensions(app)
        app.mode='level0_1Mode'
       






########################################################
#Main App
########################################################
def appStarted(app):
    app.mode='gameStartMode'
    app.timerDelay=20
    app.timerCount=0
    app.level=None
    app.mouseSelect=None
    app.pause=False


runApp(width=1200,height=900)
