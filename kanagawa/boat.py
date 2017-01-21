import pygame
import userevents

class Boat:
    # Shared
    boatImage = pygame.image.load('assets/boat.png')
    imageWidth = 50
    imageHeight = 100

    # Unique
    def __init__(self):
        self.posX = 100
        self.posY = 100
        self.deltaX = 0
        self.deltaY = 0
        self.rot = 0
        self.deltaRot = 0

    def draw(self,gameDisplay):
        gameDisplay.blit(pygame.transform.rotate(self.boatImage,self.rot), (self.posX,self.posY))

    def move(self,events,screenMaxX,screenMaxY):
        # Input Handling
        for event in events:
            if event == userevents.ROTCOUNTERCWEVENT:
                self.deltaRot += -0.75
            if event == userevents.ROTCWEVENT:
                self.deltaRot += 0.75
            if event == userevents.MOVEFORWARDEVENT:
                doNothing = 1
        # Collision Detection - Window borders
        if self.deltaX < 0 and self.posX + self.deltaX > 0:
            self.posX += self.deltaX
        if self.deltaY < 0 and self.posY + self.deltaY > 0:
            self.posY += self.deltaY
        if self.deltaX > 0 and self.posX + self.imageWidth + self.deltaX < screenMaxX:
            self.posX += self.deltaX
        if self.deltaY > 0 and self.posY + self.imageHeight + self.deltaY < screenMaxY:
            self.posY += self.deltaY

        # Rotation
        falloff = 0.9
        self.deltaRot *= falloff
        if self.deltaRot < 0.01 and self.deltaRot > -0.01:
            self.deltaRot = 0
        if self.deltaRot != 0:
            self.rot += self.deltaRot
            print(self.rot)
