import pygame
import userevents
import random

class Fish:
    # Shared
    imageAsset = pygame.image.load('assets/fish.png')
    imageWidth = 50
    imageHeight = 50
    timeToLive = 5000
    alive = False

    # Unique
    def __init__(self):
        self.posX = 650
        self.posY = 500
        self.alive = True
        #self.deltaX = 0
        #self.deltaY = 0
        #self.rot = 0
        #self.deltaRot = 0

    def draw(self,gameDisplay):
        if self.alive:
            gameDisplay.blit(self.imageAsset, (self.posX,self.posY))

    def update(self):
        #if self.timeToLive > 0:
        self.timeToLive -=60
        if self.timeToLive < 0:
            self.alive = False
        if self.timeToLive < -5000:
            self.timeToLive = 5000
            self.posX = random.randint(0,800)
            self.posY = random.randint(0,600)
            self.alive = True
