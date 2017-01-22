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
# Background
backgroundImage = pygame.image.load('assets/background.png')
def background(x,y):
    gameDisplay.blit(backgroundImage, (x,y))

# Globals
playerBoat = boat.Boat()
fish = fish.Fish()
leftNet = None
rightNet = None

inputHandler = inputhandler.InputHandler()

# Main Game Loop
def game_loop():
    global playerBoat, fish, leftNet, rightNet
    global inputHandler

    gameExit = False
    while not gameExit:
        deltaTime = clock.get_time()

        # End State
        events = pygame.event.get(pygame.QUIT)
        for event in events:
            if event.type == pygame.QUIT:
                gameExit = True

        inputHandler.handleInput(pygame.event.get((pygame.KEYDOWN,pygame.KEYUP)))

        # Fish
        fish.update()

        # Boat
        boatMovementEvents = (userevents.ROTCOUNTERCWEVENT, userevents.ROTCWEVENT, userevents.MOVEFORWARDEVENT)
        playerBoat.update(pygame.event.get(boatMovementEvents),deltaTime,display_width,display_height)

        # Nets
        events = pygame.event.get((userevents.SPAWNLEFTNETEVENT, userevents.SPAWNRIGHTNETEVENT))
        for event in events:
            if event.type == userevents.SPAWNLEFTNETEVENT:
                leftNet = net.Net(playerBoat.posX, playerBoat.posY, playerBoat.getForwardUnitVector(), event)
            if event.type == userevents.SPAWNRIGHTNETEVENT:
                rightNet = net.Net(playerBoat.posX, playerBoat.posY, playerBoat.getForwardUnitVector(), event)
        if leftNet is not None:
            leftNet.update(deltaTime)
        if rightNet is not None:
            rightNet.update(deltaTime)

        # Draw Static Elements
        background(0,0)

        # Draw Dynamic Elements
        fish.draw(gameDisplay)
        playerBoat.draw(gameDisplay)
        if leftNet is not None:
            leftNet.draw(gameDisplay)
        if rightNet is not None:
            rightNet.draw(gameDisplay)

        # System Update
        pygame.display.update()
        clock.tick(60)

# System Start Game Loop
game_loop()

# System Quit
pygame.quit()
quit()
