import pygame
from random 

#general setup
pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720 
display_surface = pygame.display.set_mode ((WINDOW_WIDTH,WINDOW_HEIGHT)) #creating window
pygame.display.set_caption("akai")
running = True
clock = pygame.time.Clock()

#surface
my_surface = pygame.Surface((100,200))

x= 100
player_surf = pygame.image.load('images/player.png').convert_alpha() #making the player surface and importing image
player_rect = player_surf.get_rect(center=(WINDOW_WIDTH / 2, WINDOW_HEIGHT - 100))
player_direction = 1

meteor_surf = pygame.image.load(('images/meteor.png')).convert_alpha()
meteor_rect = meteor_surf.get_rect(center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))

starrysbackgroud = pygame.image.load('images/star.png')
star_position = [(random.randint(0, WINDOW_WIDTH), random.randint(0, WINDOW_HEIGHT)) for i in range(20)]

laser_surf = pygame.image.load("images/laser.png")
laser_rect =laser_surf.get_rect(bottomleft = ( 20, WINDOW_HEIGHT - 20))

while running:
    clock.tick(60)
    #event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    
    display_surface.fill("black")
    for pos in star_position:
        display_surface.blit(starrysbackgroud, pos)

    display_surface.blit(laser_surf, laser_rect)
    display_surface.blit(meteor_surf, meteor_rect)

    
    player_rect.x += 100
    display_surface.blit(player_surf, player_rect)        

    pygame.display.flip()

pygame.quit()
