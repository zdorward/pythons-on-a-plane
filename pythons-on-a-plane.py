# FIXME: Fancy Header Here Later

import pygame
from sys import exit
from pygame.locals import *
pygame.init()
pygame.display.set_caption('Pythons on a Plane')
# Create vars for screen size and width/height of screen
size = 980, 660
width, height = size

# Initialize pygame and set a screen variable
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    pygame.display.update()
    clock.tick(60)

