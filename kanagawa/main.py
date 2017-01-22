import pygame
import boat
import fish
import net
import wave
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
spawnedFish = fish.Fish()
leftNet = net.Net(playerBoat.posX, playerBoat.posY, playerBoat.getForwardUnitVector(), None)
rightNet = net.Net(playerBoat.posX, playerBoat.posY, playerBoat.getForwardUnitVector(), None)
mainwave = wave.Wave('assets/wave.png')
wavefollow = wave.Wave('assets/wavefollow.png')
wavefollow.velocity = -30
wavefollow.acceleration = -20
wavefollow.countDown = 1
wavefollow.image
score = 0

inputHandler = inputhandler.InputHandler()

fishGroupSingle = pygame.sprite.GroupSingle(spawnedFish)

# Main Game Loop
def game_loop():
    global playerBoat, spawnedFish, leftNet, rightNet, mainwave, wavefollow
    global score
    global inputHandler
    global fishGroupSingle

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
        spawnedFish.update()

        #if leftNet != None:
    #        print("fish: " + str(spawnedFish.mask.overlap_area(leftNet.mask, (0,0))))


        # Boat
        boatMovementEvents = (userevents.ROTCOUNTERCWEVENT, userevents.ROTCWEVENT, userevents.MOVEFORWARDEVENT)
        playerBoat.update(pygame.event.get(boatMovementEvents),deltaTime,display_width,display_height)

        # Nets
        events = pygame.event.get((userevents.SPAWNLEFTNETEVENT, userevents.SPAWNRIGHTNETEVENT))
        for event in events:
            if event.type == userevents.SPAWNLEFTNETEVENT:
                leftNet.respawn(playerBoat.posX, playerBoat.posY, playerBoat.getForwardUnitVector(), event)
            if event.type == userevents.SPAWNRIGHTNETEVENT:
                rightNet.respawn(playerBoat.posX, playerBoat.posY, playerBoat.getForwardUnitVector(), event)

        fishHitList = list()

        leftNet.update(deltaTime)
        fishHitList += pygame.sprite.spritecollide(leftNet,fishGroupSingle,True,pygame.sprite.collide_rect)

        rightNet.update(deltaTime)
        fishHitList += pygame.sprite.spritecollide(rightNet,fishGroupSingle,True,pygame.sprite.collide_rect)

        for fishHit in fishHitList:
            print("adding score")
            score += 1
            spawnedFish.respawn()
            fishGroupSingle.add(spawnedFish)
            #print("sprite:" + str(spawnedFish.rect))

        mainwave.update(deltaTime, display_width, display_height)
        if mainwave.rect.y < 5:
            wavefollow.update(deltaTime, display_width, display_height)
        #print("loop")
        #print("score: " + str(score))

        # Draw Static Elements
        background(0,0)

        # Draw Dynamic Elements
        spawnedFish.draw(gameDisplay)
        playerBoat.draw(gameDisplay)

        leftNet.draw(gameDisplay)
        rightNet.draw(gameDisplay)

        mainwave.draw(gameDisplay)
        wavefollow.draw(gameDisplay)

        # System Update
        pygame.display.update()
        clock.tick(60)

# System Start Game Loop
game_loop()

# System Quit
pygame.quit()
quit()
