#This file contains all of the map contents

#########################################################################
#Consists of anything that a map could contain
#########################################################################

#Deployable path where operators could be deployed and 
class Path:
    def __init__(self):
        #Keep track of existing operators on it
        self.operator=None
        #Keep track of existing enemies on it
        self.enemies=[]
        #Keep track of the device on it
        self.device=None
        #Keep track of the summons on it
        self.summon=None
        #Keep track of whether the track is still deployable
        self.empty=True
        #Keep track of whether the path could still be passed
        self.couldPass=True
    
    #Keeps track of whether the path block is empty, or updating it
    def updateEmpty(self):
        if self.operator!=None or self.device!=None or self.summon!=None:
            self.empty=False
        else:
            self.empty=True

#A kind of path which enemies could pass but operators could not pass
class NPath:
    def __init__(self):
        self.enemies=[]
        self.couldPass=True
        self.empty=False

#A kind of path which allows floor operators to be deployed but enemies could 
#not pass
class Fence(Path):
    def __init__(self):
        super.__init__(self)
        self.couldPass=False

#Walls and highland classes:
class Wall:
    def __init__(self):
        self.couldPass=False
        self.enemy=[]
        self.empty=False

#The Highland class, where some operators could be deployed
class HighLand:
    def __init__(self):
        self.operator=None
        self.couldPass=False
        self.empty=True
        self.device=None
        self.summon=None

    def updateEmpty(self):
        if self.operator!=None or self.device!=None or self.summon!=None:
            self.empty=False
        else:
            self.empty=True

#The origin and destination class, signals where enemies could be spawned 
#and ends

class Origin:
    def __init__(self):
        self.empty=False
        self.couldPass=True
        self.enemies=[]

class Destination:
    def __init__(self):
        self.empty=False
        self.couldPass=True
        self.enemies=[]

#The class Level that takes in a 2D list map
class Level:
    def __init__(self,map,enemies):
        self.map=map
        self.life=3
        self.enemies=enemies

    #Returns the type of land on the map 
    def location(self,row,col):
        return map[row][col]
    