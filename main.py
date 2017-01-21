import pygame

pygame.init()

display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Main Window')

clock = pygame.time.Clock()

crashed = False
backgroundImage = pygame.image.load('assets/background.png')
boatImage = pygame.image.load('assets/boat.png')

def background(x,y):
    gameDisplay.blit(backgroundImage, (x,y))

def boat(x,y):
    gameDisplay.blit(boatImage, (x,y))

boatx = (display_width * 0.5)
boaty = (display_height * 0.5)


while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

        print(event)

    background(0,0)

    boat(boatx,boaty)

    pygame.display.update()
    clock.tick(60)


pygame.quit()
quit()
