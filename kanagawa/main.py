import pygame

# System Vars and Setup
pygame.init()

display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Main Window')

clock = pygame.time.Clock()

crashed = False

# Asset Vars and Setup
backgroundImage = pygame.image.load('assets/background.png')
boatImage = pygame.image.load('assets/boat.png')

def background(x,y):
    gameDisplay.blit(backgroundImage, (x,y))

def boat(x,y):
    gameDisplay.blit(boatImage, (x,y))

boatx = (display_width * 0.5)
boaty = (display_height * 0.5)
boatx_delta = 0
boaty_delta = 0

# Main Game Loop
while not crashed:
    # End State
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

        print(event)

    # Input Handling
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            boatx_delta = -5
        elif event.key == pygame.K_RIGHT:
            boatx_delta = 5
        elif event.key == pygame.K_UP:
            boaty_delta = -5
        elif event.key == pygame.K_DOWN:
            boaty_delta = 5
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
            boatx_delta = 0
        elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
            boaty_delta = 0

    # Update Elements

    boatx += boatx_delta
    boaty += boaty_delta

    # Draw Static Elements
    background(0,0)

    # Draw Dynamic Elements
    boat(boatx,boaty)

    # System Update
    pygame.display.update()
    clock.tick(60)


# System Quit
pygame.quit()
quit()
