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
          operator.projectile.redraw(app,canvas)
    if app.level.life<=0:
          canvas.create_text(app.width/2,app.height/2,text='Mission Failed',font='Arial 80 bold',fill='red')
    if app.level.isSuccess:
          canvas.create_text(app.width/2,app.height/2,text='Mission Accomplished',font='Arial 80 bold',fill='blue')

def level0_1Mode_timerFired(app):
     if app.pause==False:
          app.timerCount+=app.timerDelay
     if almostEqual(app.timerCount%500, 0, epsilon=10**-7) and app.level.life>0:
          app.level.cost+=1
     if app.level.life>0 and app.level.isSuccess==False:
          if app.pause==False:
               for enemy in app.level.enemies:
                    if enemy.isAlive and app.timerCount>=enemy.emergeTime*1000:
                         app.level.enemyMove(app,enemy)
          for operators in app.level.operators:
               if operators.isDeployed:
                    for enemy in app.level.enemies:
                         for locations in operators.area:
                              row,col=locations
                              if enemy.isAlive and enemy not in operators.target and app.level.inCell(app,enemy.x,enemy.y,row,col) and app.timerCount>=enemy.emergeTime*1000:
                                   operators.target.append(enemy)
                                   break
                              elif enemy in operators.target:
                                   if enemy.isAlive==False:
                                        operators.target.remove(enemy)
                                        break
                                   if app.level.inCell(app,enemy.x,enemy.y,row,col)==False:
                                        pass
                                   elif app.level.inCell(app,enemy.x,enemy.y,row,col):
                                        break
                                   operators.target.remove(enemy)
                    if len(operators.target)>0 and app.pause==False:
                         if almostEqual(operators.atkTimer%(1000*operators.atkTime), 0, epsilon=10**-7):
                              operators.projectile.setDirection(operators.target[0].x,operators.target[0].y)
                         operators.projectile.move()
                         if operators.projectile.isHit(operators.target[0].x,operators.target[0].y):
                              if operators.damageType=='Physical':
                                   operators.attackPhysical(operators.target[0])
                                   operators.target[0].checkAlive()
                              elif operators.damageType=='Magical':
                                   operators.attackMagical(operators.target[0])
                                   operators.target[0].checkAlive()
                         operators.atkTimer+=app.timerDelay
                    elif len(operators.target)==0:
                         operators.atkTimer=0
                         operators.projectile.appear=False
                    
          #Check success conditions
          for enemy in app.level.enemies:
               if enemy.isAlive:
                    app.level.isSuccess=False
                    return
          if app.level.life!=0:
               app.level.isSuccess=True
                         

def level0_1Mode_mousePressed(app,event):
     if app.level.isSuccess:
          app.mode='gameStartMode'

def level0_1Mode_mouseDragged(app,event):
     app.pause=True
     for operator in app.level.operators:
          operator.mouseDragged(app,event)

def level0_1Mode_mouseReleased(app,event):
     app.pause=False
     for operator in app.level.operators:
          operator.mouseReleased(app,event)
