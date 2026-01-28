import pygame
import random

#general setup
pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720 
display_surface = pygame.display.set_mode ((WINDOW_WIDTH,WINDOW_HEIGHT)) #creating window
pygame.display.set_caption("akai")
running = True
screen_rect = display_surface.get_rect()

#surface
my_surface = pygame.Surface((100,200))

x= 100
player_surf = pygame.image.load('images/player.png').convert_alpha() #making the player surface and importing image
starrysbackgroud = pygame.image.load('images/star.png')


surface_rect = my_surface.get_rect(center=screen_rect.center)
star_position = [(random.randint(0, WINDOW_WIDTH), random.randint(0, WINDOW_HEIGHT)) for i in range(20)]


while running:
    #event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #draw the game
    #fill the window with a red color
    
    display_surface.fill("black")
    x += 0.1
    for pos in star_position:
        display_surface.blit(starrysbackgroud, pos)
    display_surface.blit(player_surf, surface_rect)


        
    pygame.display.flip()
pygame.quit()
