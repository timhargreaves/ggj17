import pygame

class Boat:
    # Shared
    boatImage = pygame.image.load('assets/boat.png')
    imageWidth = 50
    imageHeight = 100

    # Unique
    def __init__(self):
        self.posX = 0
        self.posY = 0
        self.deltaX = 0
        self.deltaY = 0
    def draw(self,gameDisplay):
        gameDisplay.blit(self.boatImage, (self.posX,self.posY))
    def move(self,event,screenMaxX,screenMaxY):
        # Input Handling
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.deltaX = -5
            elif event.key == pygame.K_RIGHT:
                self.deltaX = 5
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
        if self.deltaX < 0 and boatx + self.deltaX < 0:
            boatx += self.deltaX
        if self.deltaY < 0 and boaty + self.deltaY < 0:
            boaty += self.deltaY
        if self.deltaX > 0 and boatx + boatWidth + self.deltaX < screenMaxX:
            boatx += self.deltaX
        if self.deltaY > 0 and boaty + boatHeight + self.deltaY < screenMaxY:
            boaty += self.deltaY
