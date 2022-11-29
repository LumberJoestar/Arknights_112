from cmu_112_graphics import *
from levelClass import*
from enemyClass import*
from operatorsClass import*
from snipersCollection import*


def level0_1Mode_redrawAll(app,canvas):
    app.level.redraw(app,canvas)
    for enemy in app.level.enemies:
     enemy.redraw(app,canvas)
def level0_1Mode_timerFired(app):
     app.timerCount+=33
     for enemy in app.level.enemies:
          app.level.enemyMove(app,enemy)
          print(enemy.path) 
     
    

