#From https://www.cs.cmu.edu/~112/notes/notes-animations-part4.html#imageMethods
#import sys
#print(f'"{sys.executable}" -m pip install pillow')
#print(f'"{sys.executable}" -m pip install requests')

from cmu_112_graphics import *
from operatorsClass import*
from enemyClass import*
from levelClass import*
from graphicsHelpers import*
from projectileClass import*
#The operators
from snipersCollection import*
from castersCollection import*
from supporterCollection import*
from specialistCollection import*

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
        heavy1=HeavyGearDefender(5,(4,8),(4,0),7,[(0,7),(0,0)])
        Sgm1=SarkazGreatswordsman(6,(0,5),(2,5),15,[(0,7),(0,0),(2,0),(0,0)])
        cs=Crownslayer(7,(4,8),(4,0),25,[(0,7),(0,0),(0,7)])
        app.exusiai=Exusiai()
        app.eyjafjalla=Eyjafjalla()
        app.gnosis=Gnosis()
        app.fartooth=Fartooth()
        app.gladiia=Gladiia()
        

        app.level=Level(map,[originiumSlug1,originiumSlug2,originiumSlug3,soldier1,heavy1,Sgm1,cs],[app.exusiai,app.eyjafjalla,app.gnosis,app.fartooth,app.gladiia])
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


    #Towers
    app.exusiai=Exusiai()
    app.eyjafjalla=Eyjafjalla()
    app.gnosis=Gnosis()
    app.fartooth=Fartooth()
    app.gladiia=Gladiia()




    #Images for the towers
    
    #Exusiai
    app.exusiai_back_attack=app.scaleImage(app.loadImage('exusiai-back-attack.png'),1/4)
    app.exusiai_right_attack=app.scaleImage(app.loadImage('exusiai-right-attack.png'),1/4)
    app.exusiai_left_attack=app.exusiai_right_attack.transpose(Image.FLIP_LEFT_RIGHT)
    app.exusiai_head=app.scaleImage(app.loadImage('exusiai-head.png'),1/2)

    #Eyja
    app.eyjafjalla_back_attack=app.scaleImage(app.loadImage('eyjafjalla-back-attack.png'),1/4)
    app.eyjafjalla_right_attack=app.scaleImage(app.loadImage('eyjafjalla-right-attack.png'),1/4)
    app.eyjafjalla_left_attack=app.eyjafjalla_right_attack.transpose(Image.FLIP_LEFT_RIGHT)
    app.eyjafjalla_head=app.scaleImage(app.loadImage('eyjafjalla-head.png'),1/2)

    #Gnosis
    app.gnosis_back_attack=app.scaleImage(app.loadImage('gnosis-back-attack.png'),1/4)
    app.gnosis_right_attack=app.scaleImage(app.loadImage('gnosis-right-attack.png'),1/4)
    app.gnosis_left_attack=app.gnosis_right_attack.transpose(Image.FLIP_LEFT_RIGHT)
    app.gnosis_head=app.scaleImage(app.loadImage('gnosis-head.png'),0.85)

    #Fartooth
    app.fartooth_back_attack=app.scaleImage(app.loadImage('fartooth-back-attack.png'),1/4)
    app.fartooth_right_attack=app.scaleImage(app.loadImage('fartooth-right-attack.png'),1/4)
    app.fartooth_left_attack=app.fartooth_right_attack.transpose(Image.FLIP_LEFT_RIGHT)
    app.fartooth_head=app.scaleImage(app.loadImage('fartooth-head.png'),0.75)

    #Gladiia
    app.gladiia_back_attack=app.scaleImage(app.loadImage('gladiia-back-attack.png'),1/4)
    app.gladiia_right_attack=app.scaleImage(app.loadImage('gladiia-right-attack.png'),1/4)
    app.gladiia_left_attack=app.gladiia_right_attack.transpose(Image.FLIP_LEFT_RIGHT)
    app.gladiia_head=app.scaleImage(app.loadImage('gladiia-head.png'),0.75)

    #Image for the enemies
    app.originiumSlug_right=app.scaleImage(app.loadImage('originiumSlug-right.png'),1/4)
    app.originiumSlug_left=app.originiumSlug_right.transpose(Image.FLIP_LEFT_RIGHT)
    app.soldier_right=app.scaleImage(app.loadImage('soldier-right.png'),1/4)
    app.soldier_left=app.soldier_right.transpose(Image.FLIP_LEFT_RIGHT)
    app.heavyDefender_right=app.scaleImage(app.loadImage('heavyDefender-right.png'),1/4)
    app.heavyDefender_left=app.heavyDefender_right.transpose(Image.FLIP_LEFT_RIGHT)
    app.sarkazGreatswordsman_right=app.scaleImage(app.loadImage('sarkazGreatswordsman-right.png'),1/4)
    app.sarkazGreatswordsman_left=app.sarkazGreatswordsman_right.transpose(Image.FLIP_LEFT_RIGHT)
    app.crownslayer_right=app.scaleImage(app.loadImage('crownslayer-right.png'),1/4)
    app.crownslayer_left=app.crownslayer_right.transpose(Image.FLIP_LEFT_RIGHT)
runApp(width=1200,height=900)
