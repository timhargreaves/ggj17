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
        self.rect.x = self.posX
        self.rect.y = self.posY

        # Collision
        #self.mask = pygame.mask.from_surface(self.image)

        # State
        self.timeToLive = 15000 #tmp
        self.alive = True
        self.cooldDown = 500


    def respawn(self):
        self.timeToLive = 15000
        self.coolDown = 500
        self.posX = random.randint(0,800)
        self.posY = random.randint(0,600)
        self.rect.x = self.posX
        self.rect.y = self.posY
        self.alive = True

    def draw(self,gameDisplay):
        if self.alive:
            gameDisplay.blit(self.image, self.rect)
            pygame.draw.rect(gameDisplay, (128, 128, 128), self.rect, 3)
        pygame.draw.rect(gameDisplay, (33, 33, 33), self.rect, 3)
        #print("drawing fishrect at: " + str(self.rect))


    def update(self):
        #if self.timeToLive > 0:
        if self.alive:
            self.timeToLive -=60
            if self.timeToLive < 0:
                self.alive = False
        else:
            self.cooldDown -= 60
            if self.cooldDown < 0:
                self.respawn()



        # Update mask after all movement
        #self.rect = self.image.get_rect()
        #print("rect: " + str(self.rect.topleft) + ", " + str(self.rect.topright))

        #self.mask = pygame.mask.from_surface(self.image)
