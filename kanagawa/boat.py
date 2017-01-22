import pygame
import userevents
import math

class Boat:
    # Shared
    imageAsset = pygame.image.load('assets/boat.png')
    imageWidth = 50
    imageHeight = 100

    maxSpeed = 4.5

    # Unique
    def __init__(self):
        self.posX = 400
        self.posY = 200
        self.velocity = 0
        self.deltaX = 0
        self.deltaY = 0
        self.rot = 0
        self.deltaRot = 0

    def draw(self,gameDisplay):
        gameDisplay.blit(pygame.transform.rotate(self.imageAsset,self.rot), (self.posX,self.posY))

    def getForwardVector(self):
        radAngle = math.radians(self.rot)
        sin = math.sin(radAngle)
        cos = math.cos(radAngle)

        # Vector.Up
        referenceVector = pygame.math.Vector2(0, 1)
        return pygame.math.Vector2(referenceVector.x * cos - referenceVector.y * sin, referenceVector.x * cos + referenceVector.y * cos)



    def move(self,events,deltaTime,screenMaxX,screenMaxY):
        # Input Handling
        shouldMoveForward = False
        for event in events:
            if event.type == userevents.ROTCWEVENT:
                self.deltaRot += 0.25
            if event.type == userevents.ROTCOUNTERCWEVENT:
                self.deltaRot += -0.25
            if event.type == userevents.MOVEFORWARDEVENT:
                shouldMoveForward = True

        acceleration = 10
        dragFactor = 5
        # Fudgy "feel" tuning
#        if self.velocity < 1:
#            dragFactor *= 0.6
#        elif self.velocity < 3:
#            dragFactor *= 0.4
#        print(str(dragFactor))

        # Translation
        if shouldMoveForward:
            self.velocity += acceleration * deltaTime / 1000

        if self.velocity > 0:
            self.velocity -= dragFactor * deltaTime / 1000
        else:
            self.velocity = 0

        self.velocity = min(self.velocity, self.maxSpeed)

        forwardVector = self.getForwardVector()
        deltaVector = forwardVector * self.velocity
        self.deltaX = deltaVector.x
        self.deltaY = deltaVector.y

        print(str(self.velocity))

        # Collision Detection - Window borders
        if self.deltaX < 0 and self.posX + self.deltaX > 0:
            self.posX += self.deltaX
        if self.deltaY < 0 and self.posY + self.deltaY > 0:
            self.posY -= self.deltaY
        if self.deltaX > 0 and self.posX + self.imageWidth + self.deltaX < screenMaxX:
            self.posX += self.deltaX
        if self.deltaY > 0 and self.posY + self.imageHeight + self.deltaY < screenMaxY:
            self.posY -= self.deltaY

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
