import pygame
import userevents
import random

class Net:
    # Shared
    imageAsset = pygame.image.load('assets/net.png')
    imageWidth = 75
    imageHeight = 75
    timeToLive = 1500
    alive = False

    # Unique
    def __init__(self, spawnx, spawny,spawnUnitDirectionVector, event):
        offsetAngle = 90
        if event.type == userevents.SPAWNRIGHTNETEVENT:
            offsetAngle *= -1

        distance = 100
        up = pygame.math.Vector2(0, 1)
        angle = spawnUnitDirectionVector.angle_to(up)
        sideVector = up.rotate(angle + offsetAngle)
        resultant = pygame.math.Vector2(spawnx, spawny) + (sideVector * distance)

        self.posX = resultant.x
        self.posY = resultant.y

        self.alive = True
        #self.deltaX = 0
        #self.deltaY = 0
        #self.rot = 0
        #self.deltaRot = 0

    def draw(self,gameDisplay):
        if self.alive:
            gameDisplay.blit(self.imageAsset, (self.posX,self.posY))

    def update(self,deltaTime):
        if self.timeToLive > 0:
            self.timeToLive -= deltaTime
        if self.timeToLive < 0:
            self.alive = False
