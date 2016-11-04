import pygame
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((800, 600))

# Variable to keep our main loop running
running = True

# Main loop
while running:
    # loop through the event queues
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            #close program
                if event.key == K_ESCAPE:
                    running = False
        elif event.type == QUIT:
            running = False


