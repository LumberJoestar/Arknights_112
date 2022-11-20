#This class consists of the function of the enemies

class Enemy():
    def __init__(self,subUnit,atkMethod,moveMethod,maxHP,atk,defence,artResis,val,atkTime,range,speed,weight,lifeGain,abResis,origin,destination):
        #These are some of the basic stats that most of the enemies would consist
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
        self.range=range
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

        #Below are some of the default stats that the enemies have
        #A list which puts the enemy's possible targets to attack
        self.target=[]
