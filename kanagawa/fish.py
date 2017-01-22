import pygame
import userevents
import random

class Fish(pygame.sprite.Sprite):

    def __init__(self):
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)

        # Geometry and Physics
        self.posX = random.randint(0,800)
        self.posY = random.randint(0,600)

        # Graphics
        self.image = pygame.image.load('assets/fish.png')
        self.rect = self.image.get_rect()
        self.rect.move_ip(self.posX, self.posY)

        # Collision
        #self.mask = pygame.mask.from_surface(self.image)

        # State
        self.timeToLive = 15000 #tmp
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
            self.timeToLive = 15000
            self.posX = random.randint(0,800)
            self.posY = random.randint(0,600)
            self.rect.move_ip(self.posX,self.posY)
            self.alive = True
        # Update mask after all movement
        #self.rect = self.image.get_rect()
        print("rect: " + str(self.rect.topleft) + ", " + str(self.rect.topright))

        #self.mask = pygame.mask.from_surface(self.image)
