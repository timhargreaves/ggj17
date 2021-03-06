import pygame
import userevents
import random

class Wave(pygame.sprite.Sprite):

    def __init__(self,imageAsset):
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)

        # Geometry and Physics
        self.posX = 0
        self.posY = 601
        self.velocity = 0
        self.acceleration = -10 # Inverted Y axis

        # Graphics
        self.image = pygame.image.load(imageAsset)
        self.rect = self.image.get_rect()
        self.rect.x = self.posX
        self.rect.y = self.posY

        # Collision
        #self.mask = pygame.mask.from_surface(self.image)

        # State
        self.alive = False
        self.countDown = 30000

        # Audio
        self.sound = pygame.mixer.Sound('assets/wave.wav')
        self.soundPlaying = False
        self.soundCooldown = 5000

    def draw(self,gameDisplay):
        gameDisplay.blit(self.image, self.rect)

    def update(self,deltaTime,screenMaxX,screenMaxY):
        if self.countDown > 0:
            self.countDown -= deltaTime
            if self.countDown < 10000:
                userEvent = pygame.event.Event(userevents.BGMTWOEVENT)
                pygame.event.post(userEvent)
        else:
            self.velocity += self.acceleration * deltaTime / 1000
            self.acceleration *= 1.005

        self.rect.x = self.posX
        self.rect.y = self.posY + self.velocity
        self.rect.y = max(self.rect.y, 0)
        if not self.soundPlaying and self.countDown <= 0 and self.countDown >= -15000:
            self.sound.play()
            self.soundPlaying = True
            self.soundCooldDown = 5000
        else:
            self.soundCooldown -= deltaTime
        if self.soundCooldown <= 0:
            self.soundPlaying = False
