import sys, pygame
from sys import exit
import pygame.gfxdraw
pygame.init()

black = 112, 10, 139
size = width, height = 1000, 700
screen = pygame.display.set_mode(size)


col = (255, 0, 0)

clr = 255,255,255

temporal = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()


    screen.fill(black)

    temporal = temporal + 1


    for X in range(0,20):
        for Y in range(0+temporal,20+temporal):

            pygame.gfxdraw.pixel(screen, X, Y, clr)

    
    
    pygame.display.flip()

