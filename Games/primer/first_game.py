import pygame
from pygame.locals import *


# Define our player object and call super to give it all the properties and methods of pygame.sprite.Sprite
# The surface we draw on the screen is now a property of 'player'
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.Surface((75, 25))
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect()

    def update(self, pressed_keys):
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -5)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 5)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)

#initialize pygame
pygame.init()

#create the screen object
screen = pygame.display.set_mode((800, 600))

#instantiate the player
player = Player()

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

    pressed_keys = pygame.key.get_pressed()

    player.update(pressed_keys)

    # blit surface onto surface (our screen)
    screen.blit(player.surf, (400, 300))
    pygame.display.flip()

#Change from ashy pally








