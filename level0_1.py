from cmu_112_graphics import *
from levelClass import*
from enemyClass import*
from operatorsClass import*
from snipersCollection import*


def level0_1Mode_redrawAll(app,canvas):
    app.level.redraw(app,canvas)
    #The condition for an enemy to emerge
    for enemy in app.level.enemies:
          if enemy.isAlive and app.timerCount>=enemy.emergeTime*1000:
               enemy.redraw(app,canvas)

def level0_1Mode_timerFired(app):
     app.timerCount+=20
     for enemy in app.level.enemies:
          if enemy.isAlive and app.timerCount>=enemy.emergeTime*1000:
               app.level.enemyMove(app,enemy)
     
    

