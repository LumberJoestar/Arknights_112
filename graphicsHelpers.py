from operatorsClass import*
from cmu_112_graphics import *

#From https://www.cs.cmu.edu/~112/notes/notes-animations-part4.html#animatedGifs
def loadAnimatedGif(path):
    # load first sprite outside of try/except to raise file-related exceptions
    spritePhotoImages = [ PhotoImage(file=path, format='gif -index 0') ]
    i = 1
    while True:
        try:
            spritePhotoImages.append(PhotoImage(file=path,
                                                format=f'gif -index {i}'))
            i += 1
        except Exception as e:
            return spritePhotoImages

#From one of the homeworks
def almostEqual(d1, d2, epsilon=10**-7):
    # note: use math.isclose() outside 15-112 with Python version 3.5 or later
    return (abs(d2 - d1) < epsilon)

def print2D(L):
    for row in L:
        for col in row:
            print(col,end=' ')
        print()
    

