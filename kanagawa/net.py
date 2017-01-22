import pygame
import userevents
import random

class Net(pygame.sprite.Sprite):

    def getSpawnPosition(self, spawnx, spawny,spawnUnitDirectionVector, event):
        distance = 100
        offsetAngle = 90
        if event != None and event.type == userevents.SPAWNRIGHTNETEVENT:
            offsetAngle *= -1

        up = pygame.math.Vector2(0, 1)
        angle = spawnUnitDirectionVector.angle_to(up)
        sideVector = up.rotate(angle + offsetAngle)
        return pygame.math.Vector2(spawnx, spawny) + (sideVector * distance)



    def __init__(self, spawnx, spawny,spawnUnitDirectionVector, event):
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)


        # Graphics
        self.image = pygame.image.load('assets/net.png')
        self.rect = self.image.get_rect()

        # Collision
        if event != None:
            resultant = self.getSpawnPosition(spawnx, spawny,spawnUnitDirectionVector, event)
            # Geometry and Physics
            self.posX = resultant.x
            self.posY = resultant.y
        # State (part of if)
            self.timeToLive = 1500
            self.alive = True
        else:
            self.posX = -100
            self.posY = -100
            self.timeToLive = -1
            self.alive = False

        self.rect.x = self.posX
        self.rect.y = self.posY
        #self.mask = pygame.mask.from_surface(self.image)



        # Future
        #self.deltaX = 0
        #self.deltaY = 0
        #self.rot = 0
        #self.deltaRot = 0

    def respawn(self, spawnx, spawny,spawnUnitDirectionVector, event):
        if self.timeToLive <= 0:
            self.timeToLive = 1500
            resultant = self.getSpawnPosition(spawnx, spawny,spawnUnitDirectionVector, event)
            self.posX = resultant.x
            self.posY = resultant.y
            print("new pos: " + str(resultant))
            self.rect.x = self.posX
            self.rect.y = self.posY
            self.alive = True

    def draw(self,gameDisplay):
        if self.alive:
            gameDisplay.blit(self.image, (self.posX,self.posY))
        pygame.draw.rect(gameDisplay, (255, 33, 33), self.rect, 3)


    def update(self,deltaTime):
        if self.alive:
            if self.timeToLive > 0:
                self.timeToLive -= deltaTime
            if self.timeToLive < 0:
                self.alive = False
        # Update mask after all movement
        #self.mask = pygame.mask.from_surface(self.image)
