import pygame
from pygame.locals import *

pygame.init()


#screen set

screen_width = 800
screen_height = 800
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Project 1")

#colors
black = [0,0,0]
white = [255,255,255]











#loop
run = True
while run:
    

    screen.fill(white)







    for event in pygame.event.get():
        if event.type == QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == K_ESCAPE:
                run = False
           

    #always use this to update screen
    pygame.display.update()



pygame.quit()