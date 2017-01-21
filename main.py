import pygame

pygame.init()

gameDisplay = pygame.display.set_mode((800,600))
pygame.display.set_caption('Main Window')

clock = pygame.time.Clock()

crashed = False
backgroundImage = pygame.image.load('assets/background.png')

def background(x,y):
    gameDisplay.blit(backgroundImage, (x,y))

x = 0
y = 0

while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

        print(event)

    background(x,y)

    pygame.display.update()
    clock.tick(60)


pygame.quit()
quit()
