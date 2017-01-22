import pygame
import userevents

class InputHandler:
    # Shared
    countercwRot = False
    cwRot = False
    spawnLeftNet = False
    spawnRightNet = False

    # Unique
    def __init__(self):
        x = 0

    def handleInput(self,events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.countercwRot = True
                elif event.key == pygame.K_RIGHT:
                    self.cwRot = True
                elif event.key == pygame.K_a:
                    self.spawnLeftNet = True
                elif event.key == pygame.K_d:
                    self.spawnRightNet = True

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    self.countercwRot = False
                elif event.key == pygame.K_RIGHT:
                    self.cwRot = False

        if self.countercwRot:
            userEvent = pygame.event.Event(userevents.ROTCOUNTERCWEVENT)
            pygame.event.post(userEvent)
        if self.cwRot:
            userEvent = pygame.event.Event(userevents.ROTCWEVENT)
            pygame.event.post(userEvent)
        if self.countercwRot and self.cwRot:
            userEvent = pygame.event.Event(userevents.MOVEFORWARDEVENT)
            pygame.event.post(userEvent)

        if self.spawnLeftNet:
            userEvent = pygame.event.Event(userevents.SPAWNLEFTNETEVENT)
            pygame.event.post(userEvent)
            self.spawnLeftNet = False
        if self.spawnRightNet:
            userEvent = pygame.event.Event(userevents.SPAWNRIGHTNETEVENT)
            pygame.event.post(userEvent)
            self.spawnRightNet = False
