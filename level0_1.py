from cmu_112_graphics import *
from levelClass import*
from enemyClass import*
from operatorsClass import*
from snipersCollection import*


def level0_1Mode_redrawAll(app,canvas):
    map=[[Path(),Path(),Path(),Path(),Path(),Origin(),Path(),Path(),Wall()],
         [Path(),Wall(),Path(),HighLand(),Wall(),Path(),Wall(),Path(),Wall()],
         [Path(),Path(),Path(),Path(),Path(),Destination(),Path(),Path(),Path()],
         [Wall(),Path(),HighLand(),Path(),Wall(),Path(),Fence(),HighLand(),Path()],
         [Destination(),NPath(),Path(),Path(),HighLand(),Path(),HighLand(),HighLand(),Origin()],
         [Wall(),Wall(),Wall(),Wall(),Wall(),Wall(),Wall(),Wall(),Wall()]]
    originiumSlug1=OriginiumSlug(1,(0,4),(2,5),1,[(0,0),(2,0),(4,1)])
    
    level=Level(map,['originiumSlug1'])
    level.setOriginDimensions(app,originiumSlug1)

    
    level.redraw(app,canvas)
    

