import pygame
import userevents
import random

class Fish(pygame.sprite.Sprite):

    def __init__(self):
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)

        # Geometry and Physics
        self.posX = 650
        self.posY = 500

        # Graphics
        self.image = pygame.image.load('assets/fish.png')
        self.rect = self.image.get_rect()

        # Collision
        self.mask = pygame.mask.from_surface(self.image)

        # State
        self.timeToLive = 5000
        self.alive = True



    def draw(self,gameDisplay):
        if self.alive:
            gameDisplay.blit(self.image, (self.posX,self.posY))

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
