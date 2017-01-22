import pygame
import userevents
import random

class Net(pygame.sprite.Sprite):

    def __init__(self, spawnx, spawny,spawnUnitDirectionVector, event):
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)

        # Geometry and Physics
        distance = 100
        offsetAngle = 90
        if event.type == userevents.SPAWNRIGHTNETEVENT:
            offsetAngle *= -1

        up = pygame.math.Vector2(0, 1)
        angle = spawnUnitDirectionVector.angle_to(up)
        sideVector = up.rotate(angle + offsetAngle)
        resultant = pygame.math.Vector2(spawnx, spawny) + (sideVector * distance)

        self.posX = resultant.x
        self.posY = resultant.y

        # Graphics
        self.image = pygame.image.load('assets/net.png')
        self.rect = self.image.get_rect()

        # Collision
        self.mask = pygame.mask.from_surface(self.image)

        # State
        self.timeToLive = 1500
        self.alive = True

        # Future
        #self.deltaX = 0
        #self.deltaY = 0
        #self.rot = 0
        #self.deltaRot = 0

    def draw(self,gameDisplay):
        if self.alive:
            gameDisplay.blit(self.image, (self.posX,self.posY))

    def update(self,deltaTime):
        if self.timeToLive > 0:
            self.timeToLive -= deltaTime
        if self.timeToLive < 0:
            self.alive = False
