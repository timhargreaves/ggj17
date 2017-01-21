import pygame

class Boat:
    # Shared
    boatImage = pygame.image.load('assets/boat.png')
    imageWidth = 50
    imageHeight = 100

    # Unique
    def __init__(self):
        self.posX = 100
        self.posY = 100
        self.deltaX = 0
        self.deltaY = 0
        self.rot = 0
        self.rotDelta = 0

    def draw(self,gameDisplay):

        gameDisplay.blit(pygame.transform.rotate(self.boatImage,self.rot), (self.posX,self.posY))

    def move(self,event,screenMaxX,screenMaxY):
        # Input Handling
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.rotDelta = -5
            elif event.key == pygame.K_RIGHT:
                self.rotDelta = 5
            elif event.key == pygame.K_UP:
                self.deltaY = -5
            elif event.key == pygame.K_DOWN:
                self.deltaY = 5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                self.deltaX = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                self.deltaY = 0

        # Collision Detection - Window borders
        if self.deltaX < 0 and self.posX + self.deltaX > 0:
            self.posX += self.deltaX
        if self.deltaY < 0 and self.posY + self.deltaY > 0:
            self.posY += self.deltaY
        if self.deltaX > 0 and self.posX + self.imageWidth + self.deltaX < screenMaxX:
            self.posX += self.deltaX
        if self.deltaY > 0 and self.posY + self.imageHeight + self.deltaY < screenMaxY:
            self.posY += self.deltaY

        # Rotation
        if self.rotDelta != 0:
            self.rot += self.rotDelta
