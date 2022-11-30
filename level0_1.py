from cmu_112_graphics import *
from levelClass import*
from enemyClass import*
from operatorsClass import*



def level0_1Mode_redrawAll(app,canvas):
    app.level.redraw(app,canvas)
    #The condition for an enemy to emerge
    for enemy in app.level.enemies:
          if enemy.isAlive and app.timerCount>=enemy.emergeTime*1000:
               enemy.redraw(app,canvas)

    for operator in app.level.operators:
          operator.redraw(app,canvas)
    if app.level.life<=0:
          canvas.create_text(app.width/2,app.height/2,text='Mission Failed',font='Arial 80 bold',fill='red')

def level0_1Mode_timerFired(app):
     app.timerCount+=20
     if app.level.life>0:
          for enemy in app.level.enemies:
               if enemy.isAlive and app.timerCount>=enemy.emergeTime*1000:
                    app.level.enemyMove(app,enemy)
          for operators in app.level.operators:
               if operators.isDeployed:
                    for enemy in app.level.enemies:
                         for locations in operators.area:
                              row,col=locations
                              if enemy.isAlive and enemy not in operators.target and app.level.inCell(app,enemy.x,enemy.y,row,col):
                                   operators.target.append(enemy)
                                   break
                              elif enemy in operators.target and (enemy.isAlive==False or app.level.inCell(app,enemy.x,enemy.y,row,col)==False):
                                   operators.target.remove(enemy)
                    if len(operators.target)>0 and almostEqual(app.timerCount%(1000*operators.atkTime), 0, epsilon=10**-7):
                         if operators.damageType=='Physical':
                              operators.attackPhysical(operators.target[0])
                              operators.target[0].checkAlive()
                         elif operators.damageType=='Magical':
                              operators.attackMagical(operators.target[0])
                              operators.target[0].checkAlive()

                         

     if almostEqual(app.timerCount%1000, 0, epsilon=10**-7) and app.level.life>0:
          app.level.cost+=1

def level0_1Mode_mouseDragged(app,event):
     for operator in app.level.operators:
          operator.mouseDragged(app,event)

def level0_1Mode_mouseReleased(app,event):
     for operator in app.level.operators:
          operator.mouseReleased(app,event)
