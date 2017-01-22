import pygame
import userevents
import random

class Wave(pygame.sprite.Sprite):

    def __init__(self):
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)

        # Geometry and Physics
        self.posX = 0
        self.posY = 801
        self.velocity = 0
        self.acceleration = 10

        # Graphics
        self.image = pygame.image.load('assets/wave.png')
        self.rect = self.image.get_rect()
        self.rect.x = self.posX
        self.rect.y = self.posY

        # Collision
        #self.mask = pygame.mask.from_surface(self.image)

        # State
        self.alive = False
        self.countDown = 1000

    def draw(self,gameDisplay):
        gameDisplay.blit(self.image, self.rect)

    def update(self,events,deltaTime,screenMaxX,screenMaxY):
        if countDown > 0:
            countDown -= 60
        else:
            self.velocity += self.acceleration * deltaTime / 1000

        self.rect.move_ip(0, self.posY)
