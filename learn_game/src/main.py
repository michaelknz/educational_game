import pygame
from start_screen import start_screen
from inform_game import inform_game

SCREEN_WIDTH=1600
SCREEN_HEIGHT=800

pygame.init()

screen=pygame.display.set_mode([SCREEN_WIDTH,SCREEN_HEIGHT])
clock = pygame.time.Clock()
start_scr=start_screen(screen,"res/start_bg.jpg")
inform_scr=inform_game(screen,"res/start_bg.jpg")

running=True
is_clicked=False
mouse_pos=[-1,-1]
cur_mode=0
next_mode=0
keys=[]
for i in range(255):
    keys.append([False,False])
while(running):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            is_clicked=True
            mouse_pos=[event.pos[0],event.pos[1]]
        if event.type == pygame.MOUSEBUTTONUP:
            mouse_pos=[-1,-1]
            is_clicked=False
            cur_mode=next_mode
        if event.type == pygame.KEYDOWN:
            keys[event.key][0]=True
        if event.type == pygame.KEYUP:
            keys[event.key][0]=False
            keys[event.key][1]=False


    screen.fill((127,127,127))
    if(cur_mode==0):
        next_mode = start_scr.update(is_clicked,mouse_pos)
    elif(cur_mode==1):
        next_mode = inform_scr.update(is_clicked,mouse_pos,keys)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
