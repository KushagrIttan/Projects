import pygame

#initialize the pygame
pygame.init()

#create a screen
screen = pygame.display.set_mode( (800,600) )

#title and icon
pygame.display.set_caption("Space invaders")
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)
#game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
#rgb
    screen.fill((0 ,0 ,0 ))
    pygame.display.update()