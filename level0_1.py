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
    level=Level(map,[])
    level.redraw(app,canvas)
    Exus= Exusiai()
    Exus.redraw(app,canvas)

