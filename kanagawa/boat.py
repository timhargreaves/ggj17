import pygame
import userevents
import math

class Boat:
    # Shared
    boatImage = pygame.image.load('assets/boat.png')
    imageWidth = 50
    imageHeight = 100

    # Unique
    def __init__(self):
        self.posX = 400
        self.posY = 200
        self.deltaX = 0
        self.deltaY = 0
        self.rot = 0
        self.deltaRot = 0

    def draw(self,gameDisplay):
        gameDisplay.blit(pygame.transform.rotate(self.boatImage,self.rot), (self.posX,self.posY))

    def moveForward(self):
        radAngle = math.radians(self.rot)
        sin = math.sin(radAngle)
        cos = math.cos(radAngle)

        referenceVector = pygame.math.Vector2(0, -1)
        forwardVector = pygame.math.Vector2(referenceVector.x * cos - referenceVector.y * sin, referenceVector.x * cos + referenceVector.y * cos)
        self.deltaX = forwardVector.x
        self.deltaY = forwardVector.y

        print("x: " + str(self.posX) + " y: " + str(self.posY))
        print("dx: " + str(forwardVector.x) + " dy: " + str(forwardVector.y))


    def move(self,events,screenMaxX,screenMaxY):
        # Input Handling
        shouldMoveForward = False
        for event in events:
            if event.type == userevents.ROTCWEVENT:
                self.deltaRot += 0.25
            if event.type == userevents.ROTCOUNTERCWEVENT:
                self.deltaRot += -0.25
            if event.type == userevents.MOVEFORWARDEVENT:
                shouldMoveForward = True
        # Collision Detection - Window borders
        if self.deltaX < 0 and self.posX + self.deltaX > 0:
            self.posX -= self.deltaX
        if self.deltaY < 0 and self.posY + self.deltaY > 0:
            self.posY += self.deltaY
        if self.deltaX > 0 and self.posX + self.imageWidth + self.deltaX < screenMaxX:
            self.posX -= self.deltaX
        if self.deltaY > 0 and self.posY + self.imageHeight + self.deltaY < screenMaxY:
            self.posY += self.deltaY

        falloff = 0.9
        self.deltaX *= falloff
        self.deltaY *= falloff

        # Rotation
        rotFalloff = 0.9
        self.deltaRot *= rotFalloff
        if self.deltaRot < 0.01 and self.deltaRot > -0.01:
            self.deltaRot = 0
        if self.deltaRot != 0:
            self.rot += self.deltaRot
            if self.rot > 360:
                self.rot -= 360
            if self.rot < 0:
                self.rot += 360
#            print(self.rot)
        if shouldMoveForward:
            self.moveForward()
