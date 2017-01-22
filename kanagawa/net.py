import pygame
import userevents
import random

class Net:
    # Shared
    imageAsset = pygame.image.load('assets/net.png')
    imageWidth = 75
    imageHeight = 75
    timeToLive = 1000
    alive = False

    # Unique
    def __init__(self, spawnx, spawny,spawnUnitDirectionVector):
        normalVector = pygame.math.Vector2(-spawnUnitDirectionVector.y, spawnUnitDirectionVector.x)
        normalVector += pygame.math.Vector2(spawnx - 50, spawny)
        self.posX = normalVector.x
        #normalVector *= 1.5

        #print(str(self.posX))
        self.posY = normalVector.y
        print("Created leftNet at: " + str(normalVector.x) + ", " + str(normalVector.y))

        self.alive = True
        #self.deltaX = 0
        #self.deltaY = 0
        #self.rot = 0
        #self.deltaRot = 0

    def draw(self,gameDisplay):
        if self.alive:
            gameDisplay.blit(self.imageAsset, (self.posX,self.posY))

    def update(self):
        self.alive = True
        #if self.timeToLive > 0:
#        self.timeToLive -=60
#        if self.timeToLive < 0:
#            self.alive = False
