
from cmu_112_graphics import *
from levelClass import*
from operatorsClass import*
from projectileClass import*
#This class consists of the function of the enemies

class Enemy():
    def __init__(self,name,levelNo,subUnit,atkMethod,moveMethod,maxHP,atk,defence,artResis,val,atkTime,atkrange,speed,weight,lifeGain,abResis,origin,destination,emergeTime,checkPoints):
        #These are some of the basic stats that most of the enemies would consist
        #Defines the enemy's name
        self.name=name
        #Defines the enemy's number in a level
        self.levelNo=levelNo
        #Defines a classification of the enemy
        self.subUnit=subUnit
        #Defines the enemy's attack method
        self.atkMethod=atkMethod
        #Defines how the enemy moves, whether through the ground or flying
        self.moveMethod=moveMethod
        #Defines the enemy's maximum health point
        self.maxHP=maxHP
        #Defines the enemy's attack stat
        self.atk=atk
        #Defines the enemy's resistence to physical damage
        self.defence=defence
        #Defines the enemy's resistence to magical damage
        self.artResis=artResis
        #Defines the enemy's damage to the level HP
        self.val=val
        #Defines the basic time that an enemy take to take another attack
        self.atkTime=atkTime
        #Defines the enemy's range
        self.atkrange=atkrange
        #Defines the enemy's speed
        self.speed=speed
        #Defines the enemy's weight
        self.weight=weight
        #Defines the enemy's lifegain per second
        self.lifeGain=lifeGain
        #A list containing the enemy's resistance to abnormal status
        self.abResis=abResis
        #Defines the enemy's origin in a level
        self.origin=origin
        #Defines the enemy's destination in a level
        self.destination=destination
        #Defines the enemy's emerge time within the level
        self.emergeTime=emergeTime
        #Defines the series of check points the enemy need to go through before approaching destination
        self.checkPoints=checkPoints

        #Below are some of the default stats that the enemies have
        
        #A list which puts the enemy's possible targets to attack
        self.target=[]
        #A list recording the enemy's current HP
        self.currentHP=self.maxHP
        #Records whether the enemy is alive or not:
        self.isAlive=True
        #Defines the enemie's taunt level
        self.taunt=0
        #Initialize an attack speed measurement to 100
        self.atkSpeed=100
        #A list containing the buffs
        self.buff=[]
        #And one containing debuffs
        self.debuffs=[]
        #Determines whether the enemy is blocked
        self.isBlocked=False
        #The enemy's current location
        self.x,self.y=(-1,-1)
        
        #The enemy's direction:
        self.direction=(0,0)
        #A list containing the enemy's path
        self.path=[]

        
    ############################################################################
    #Enemy Methods:
    ############################################################################  
    
    #Returns the enemy's path:
    def solveEnemyPath(self,level):
        path=[]
        if len(self.checkPoints)==0:
            path=level.solvePath(self.origin,self.destination)
            return path
        else:
            path.extend(level.solvePath(self.origin,self.checkPoints[0]))
            for i in range(1,len(self.checkPoints)):
                path.extend(level.solvePath(path[-1],self.checkPoints[i])[1:])
            path.extend(level.solvePath(self.checkPoints[-1],self.destination)[1:])
            return path

        #Checks whether the enemy is alive by checking the currentHP
    def checkAlive(self):
        if self.currentHP<0:
            self.isAlive=False
    
    def attackPhysical(self,operator):
        if self.isAlive:
            operator.currentHP-=max((self.atk-operator.defence),0.05*self.atk)
    
    def attackMagical(self,operator):
        if self.isAlive:
            operator.currentHP-=max(0.05*self.attack,(self.atk*(100-operator.artResis)))
    
    
    
    
#The normal enemy class
class NormalEnemy(Enemy):
    def __init__(self,name,levelNo,subUnit,atkMethod,moveMethod,maxHP,atk,defence,artResis,val,atkTime,atkrange,speed,weight,lifeGain,abResis,origin,destination,emergeTime,checkPoints):
        super().__init__(name,levelNo,subUnit,atkMethod,moveMethod,maxHP,atk,defence,artResis,val,atkTime,atkrange,speed,weight,lifeGain,abResis,origin,destination,emergeTime,checkPoints)


#The Elite enemy class
class EliteEnemy(Enemy):
    def __init__(self,name,levelNo,subUnit,atkMethod,moveMethod,maxHP,atk,defence,artResis,val,atkTime,atkrange,speed,weight,lifeGain,abResis,origin,destination,emergeTime,checkPoints):
        super().__init__(name,levelNo,subUnit,atkMethod,moveMethod,maxHP,atk,defence,artResis,val,atkTime,atkrange,speed,weight,lifeGain,abResis,origin,destination,emergeTime,checkPoints)

#The Leader class
class LeaderEnemy(Enemy):
    def __init__(self,name,levelNo,subUnit,atkMethod,moveMethod,maxHP,atk,defence,artResis,val,atkTime,atkrange,speed,weight,lifeGain,abResis,origin,destination,emergeTime,checkPoints):
        super().__init__(name,levelNo,subUnit,atkMethod,moveMethod,maxHP,atk,defence,artResis,val,atkTime,atkrange,speed,weight,lifeGain,abResis,origin,destination,emergeTime,checkPoints)



#######################################################################################################################
#The Enemies:
#######################################################################################################################

#Our favourite originium slug:
class OriginiumSlug(NormalEnemy):
    def __init__(self,levelNo,origin,destination,emergeTime,checkPoints):
        super().__init__('Originium Slug',levelNo,'Infected Creature',('Melee'),('Ground'),550,180,0,0,1,1.0,0,0.5,0,0,[],origin,destination,emergeTime,checkPoints)

    def redraw(self,app,canvas):
        if self.direction[0]==-1:
            canvas.create_image(self.x,self.y,image=ImageTk.PhotoImage(app.originiumSlug_left))
        else:
            canvas.create_image(self.x,self.y,image=ImageTk.PhotoImage(app.originiumSlug_right))
        canvas.create_text(self.x,self.y+35,text=f'{self.currentHP}',font='Arial 12 bold',fill='red')

#Normal Reunium Soldiers
class Soldier(NormalEnemy):
    def __init__(self,levelNo,origin,destination,emergeTime,checkPoints):
        super().__init__('Soldier',levelNo,None,('Melee'),('Ground'),1650,200,100,0,1,2.0,0,1.0,1,0,[],origin,destination,emergeTime,checkPoints)
    
    def redraw(self,app,canvas):
        if self.direction[0]==-1:
            canvas.create_image(self.x,self.y,image=ImageTk.PhotoImage(app.soldier_left))
        else:
            canvas.create_image(self.x,self.y,image=ImageTk.PhotoImage(app.soldier_right))
        canvas.create_text(self.x,self.y+35,text=f'{self.currentHP}',font='Arial 12 bold',fill='red')

#Shield, needs magical damage
class HeavyGearDefender(EliteEnemy):
    def __init__(self,levelNo,origin,destination,emergeTime,checkPoints):
        super().__init__('HeavyGearDefender',levelNo,None,('Melee'),('Ground'),6000,600,800,0,1,2.6,0,0.5,3,0,[],origin,destination,emergeTime,checkPoints)

    def redraw(self,app,canvas):
        if self.direction[0]==-1:
            canvas.create_image(self.x,self.y,image=ImageTk.PhotoImage(app.heavyDefender_left))
        else:
            canvas.create_image(self.x,self.y,image=ImageTk.PhotoImage(app.heavyDefender_right))
        canvas.create_text(self.x,self.y+35,text=f'{self.currentHP}',font='Arial 12 bold',fill='red')

#Sarkaz, high magical resistance, need physical damage       
class SarkazGreatswordsman(EliteEnemy):
    def __init__(self,levelNo,origin,destination,emergeTime,checkPoints):
        super().__init__('Sarkaz Greatswordsman',levelNo,'Sarkaz',('Melee'),('Ground'),7500,600,230,50,1,2.0,0,1.0,2,0,[],origin,destination,emergeTime,checkPoints)

    def redraw(self,app,canvas):
        if self.direction[0]==-1:
            canvas.create_image(self.x,self.y,image=ImageTk.PhotoImage(app.sarkazGreatswordsman_left))
        else:
            canvas.create_image(self.x,self.y,image=ImageTk.PhotoImage(app.sarkazGreatswordsman_right))
        canvas.create_text(self.x,self.y+35,text=f'{self.currentHP}',font='Arial 12 bold',fill='red')

#A boss in the game: CrownSlayer
class Crownslayer(LeaderEnemy):
    def __init__(self,levelNo,origin,destination,emergeTime,checkPoints):
        super().__init__('Crownslayer',levelNo,None,('Melee'),('Ground'),10000,550,150,50,2,2.8,0,2.0,1,0,[],origin,destination,emergeTime,checkPoints)

    def redraw(self,app,canvas):
        if self.direction[0]==-1:
            canvas.create_image(self.x,self.y,image=ImageTk.PhotoImage(app.crownslayer_left))
        else:
            canvas.create_image(self.x,self.y,image=ImageTk.PhotoImage(app.crownslayer_right))
        canvas.create_text(self.x,self.y+35,text=f'{self.currentHP}',font='Arial 12 bold',fill='red')