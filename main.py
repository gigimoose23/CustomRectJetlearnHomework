import pgzero  
import pgzrun
import pygame
currentRects = []
rectColor = ""


def drawRect(colour, size, pos):
    global currentRects
    global rectColor
    rectColor = colour
    newRect = Rect(pos[0], pos[1], size[0], size[1])
    
    currentRects.append(newRect)
    return newRect

def destroyRect(toDestroy):
    if not toDestroy in currentRects:
        raise Exception("Cannot destroy rectangle that has not been drawn yet")
    else:
        currentRects.remove(toDestroy)

def draw():
    global rectColor
    for rect in currentRects:
        
        screen.draw.filled_rect(rect, rectColor)
        rectColor = ""       

class CustomRect():
    def __init__(self, colour, size, pos):
        self.rectangle_pos = pos
        self.rectangle_colour = colour
        self.rectangle_size = size
        self.realRect = ""

    def draw(self):
        rectDrawed = drawRect(colour=self.rectangle_colour, size=self.rectangle_size, pos=self.rectangle_pos)
        self.draw = rectDrawed
        self.realRect = rectDrawed
        

    def destroy(self):
        self.destroy = destroyRect(self.realRect)


rectOne = CustomRect("red", (90,90), (500,50))
rectTwo = CustomRect("white", (90,90), (70,50))

rectTwo.draw()

rectOne.destroy()
pgzrun.go()