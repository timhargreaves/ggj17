import pygame
import userevents

class Fish:
    # Shared
    imageAsset = pygame.image.load('assets/fish.png')
    imageWidth = 50
    imageHeight = 50

    # Unique
    def __init__(self):
        self.posX = 650
        self.posY = 500
        #self.deltaX = 0
        #self.deltaY = 0
        #self.rot = 0
        #self.deltaRot = 0

    def draw(self,gameDisplay):
        gameDisplay.blit(self.imageAsset, (self.posX,self.posY))

    #def update(self):
        # do something
