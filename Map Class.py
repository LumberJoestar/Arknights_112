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
class Fence:
    def __init__(self):
        self.operator=None
        self.enemies=[]
        self.device=None
        self.summon=None
        self.empty=True
        self.couldPass=False
    def updateEmpty(self):
        if self.operator!=None or self.device!=None or self.summon!=None:
            self.empty=False
        else:
            self.empty=True

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
        return self.map[row][col]
    
    #Check whether a move is valid
    def validMove(self,start,direction):
        row,col=start
        drow,dcol=direction
        newRow,newCol=row+drow,col+dcol
        if newRow<0 or newRow>=len(self.map) or newCol<0 or newCol>=len(self.map[0]):
            return False
        if self.map[newRow][newCol].couldPass==False:
            return False
        return True

    #Returns the best solution starting from the four directions,takes reference 
    #to https://www.cs.cmu.edu/~112/notes/notes-recursion-part2.html#mazeSolving
    def solvePath(self,start,end):
        resultUp=self.pathFind(start,end,list(),set(),'Up')
        resultRight=self.pathFind(start,end,list(),set(),'Right')
        resultDown=self.pathFind(start,end,list(),set(),'Down')
        resultLeft=self.pathFind(start,end,list(),set(),'Left')
        toBeCompared=[resultUp,resultRight,resultDown,resultLeft]
        if resultUp==None and resultRight==None and resultLeft==None and resultDown==None:
            return None
        for i in range(3):
            if toBeCompared[i]!=None:
                best=toBeCompared[0]
                bestLen=len(toBeCompared[0])
        for result in toBeCompared:
            if result!=None and len(result)<bestLen:
                best=result
                bestLen=len(result)
        return best

    #Returns a list of tuple path starting from point start to end, with starting
    #direction included
    def pathFind(self,start,end,path,visited,startingDirect):
        if start in visited:
            return None
        rows,cols=len(self.map),len(self.map[0])
        targetRow,targetCol=end
        visited.add((start))
        path.append(start)
        if start==end:
            return path
        else:
            if startingDirect=='Up':
                for direction in [(-1,0),(0,1),(1,0),(0,-1)]:
                    if self.validMove(start,direction):
                        row,col=start
                        drow,dcol=direction
                        newRow,newCol=row+drow,col+dcol
                        result=self.pathFind((newRow,newCol),end,path,visited,startingDirect)
                        if result!=None:
                            return result
            if startingDirect=='Right':
                for direction in [(0,1),(-1,0),(0,-1),(1,0)]:
                    if self.validMove(start,direction):
                        row,col=start
                        drow,dcol=direction
                        newRow,newCol=row+drow,col+dcol
                        result=self.pathFind((newRow,newCol),end,path,visited,startingDirect)
                        if result!=None:
                            return result
            if startingDirect=='Down':
                for direction in [(-1,0),(0,-1),(1,0),(0,1)]:
                    if self.validMove(start,direction):
                        row,col=start
                        drow,dcol=direction
                        newRow,newCol=row+drow,col+dcol
                        result=self.pathFind((newRow,newCol),end,path,visited,startingDirect)
                        if result!=None:
                            return result
            if startingDirect=='Left':
                for direction in [(0,-1),(-1,0),(0,1),(1,0)]:
                    if self.validMove(start,direction):
                        row,col=start
                        drow,dcol=direction
                        newRow,newCol=row+drow,col+dcol
                        result=self.pathFind((newRow,newCol),end,path,visited,startingDirect)
                        if result!=None:
                            return result
        visited.remove(start)
        path.pop()
        return None

#Test case for path solving, where the enemy class is not yet properly defined
def testSolvePath():
    print('Testing solvePath...',end='')
    map=[[Path(),Path(),Path(),Path(),Path(),Origin(),Path(),Path(),Wall()],
         [Path(),Wall(),Path(),HighLand(),Wall(),Path(),Wall(),Path(),Wall()],
         [Path(),Path(),Path(),Path(),Path(),Destination(),Path(),Path(),Path()],
         [Wall(),Path(),HighLand(),Path(),Wall(),Path(),Fence(),HighLand(),Path()],
         [Destination(),NPath(),Path(),Path(),HighLand(),Path(),HighLand(),HighLand(),Origin()],
         [Wall(),Wall(),Wall(),Wall(),Wall(),Wall(),Wall(),Wall(),Wall()]]
    demo=Level(map,['Originium Slug'])
    print(demo.solvePath((0,5),(4,0)))
    print(demo.solvePath((4,8),(4,0)))
    print('Passed')

testSolvePath()    
    