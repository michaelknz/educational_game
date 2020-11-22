import pygame
from start_screen import start_screen

SCREEN_WIDTH=1500
SCREEN_HEIGHT=800

pygame.init()

screen=pygame.display.set_mode([SCREEN_WIDTH,SCREEN_HEIGHT])
clock = pygame.time.Clock()
start_scr=start_screen(screen)

running=True
while(running):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((127,127,127))
    start_scr.update()
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
