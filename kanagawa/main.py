import pygame
import boat


# System Vars and Setup
pygame.init()

display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Main Window')

clock = pygame.time.Clock()

# Asset Vars and Setup
backgroundImage = pygame.image.load('assets/background.png')
boatImage = pygame.image.load('assets/boat.png')

def background(x,y):
    gameDisplay.blit(backgroundImage, (x,y))



global thisBoat
thisBoat = boat.Boat()
#global boaty
boat.posX = (display_width * 0.5)
boat.posY = (display_height * 0.5)

# Main Game Loop
def game_loop():
    gameExit = False

    while not gameExit:
        # End State
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True

            print(event)

        thisBoat.move(event,display_width,display_height)

        # Draw Static Elements
        background(0,0)

        # Draw Dynamic Elements
        thisBoat.draw(gameDisplay)

        # System Update
        pygame.display.update()
        clock.tick(60)

# System Start Game Loop
game_loop()

# System Quit
pygame.quit()
quit()