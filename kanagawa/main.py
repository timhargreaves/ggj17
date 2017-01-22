import pygame
import boat
import fish
import net
import inputhandler
import userevents


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



playerBoat = boat.Boat()


fish = fish.Fish()

leftNet = net.Net(-100,-100)
rightNet = net.Net(-100,-100)


global inputHandler
inputHandler = inputhandler.InputHandler()

# Main Game Loop
def game_loop():
    global playerBoat, fish, leftNet, rightNet
    global inputHandler

    gameExit = False
    while not gameExit:
        events = pygame.event.get(pygame.QUIT)
        # End State
        for event in events:
            if event.type == pygame.QUIT:
                gameExit = True

#            print(event)
        inputHandler.handleInput(pygame.event.get((pygame.KEYDOWN,pygame.KEYUP)))

        fish.update()

        boatMovementEvents = (userevents.ROTCOUNTERCWEVENT, userevents.ROTCWEVENT, userevents.MOVEFORWARDEVENT)
        playerBoat.move(pygame.event.get(boatMovementEvents),display_width,display_height)

        events = pygame.event.get((userevents.SPAWNLEFTNETEVENT, userevents.SPAWNRIGHTNETEVENT))
        for event in events:
            #print(event)
            if event.type == userevents.SPAWNLEFTNETEVENT:
                print("Creating leftNet at: " + str(playerBoat.posX) + ", " + str(playerBoat.posY))
                leftNet = net.Net(playerBoat.posX, playerBoat.posY)

        if leftNet is not None:
            leftNet.update()

        # Draw Static Elements
        background(0,0)

        # Draw Dynamic Elements
        playerBoat.draw(gameDisplay)
        fish.draw(gameDisplay)
        leftNet.draw(gameDisplay)

        # System Update
        pygame.display.update()
        clock.tick(60)

# System Start Game Loop
game_loop()

# System Quit
pygame.quit()
quit()
