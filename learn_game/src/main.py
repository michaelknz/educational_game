import pygame
from start_screen import start_screen
from inform_game import inform_game
from math_game import math_game
from memo import memo_game

SCREEN_WIDTH=1600
SCREEN_HEIGHT=800

pygame.init()

screen=pygame.display.set_mode([SCREEN_WIDTH,SCREEN_HEIGHT])
clock = pygame.time.Clock()
start_scr=start_screen(screen,"res/start_bg.jpg")
inform_scr=inform_game(screen,"res/start_bg.jpg")
math_scr=math_game(screen,"res/math_bg.jpg")
memo_scr=memo_game(screen)
running=True
is_clicked=False
mouse_pos=[-1,-1]
cur_mode=0
next_mode=0
keys=[]
for i in range(258):
    keys.append([False,0,'',0,False])
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
            if(event.key<256):
                keys[event.key][0]=True
                keys[event.key][2]=event.unicode
                keys[event.key][3]=pygame.time.get_ticks()
            elif(event.key==pygame.K_RIGHT):
                keys[256][0]=True
                keys[256][2]=''
                keys[256][3]=pygame.time.get_ticks()
            elif(event.key==pygame.K_LEFT):
                keys[257][0]=True
                keys[257][2]=''
                keys[257][3]=pygame.time.get_ticks()
        if event.type == pygame.KEYUP:
            if(event.key<256):
                keys[event.key][0]=False
                keys[event.key][1]=0
                keys[event.key][4]=False
            elif(event.key==pygame.K_RIGHT):
                keys[256][0]=False
                keys[256][1]=0
                keys[256][4]=False
            elif(event.key==pygame.K_LEFT):
                keys[257][0]=False
                keys[257][1]=0
                keys[257][4]=False


    screen.fill((127,127,127))
    if(cur_mode==0):
        next_mode = start_scr.update(is_clicked,mouse_pos)
    elif(cur_mode==1):
        next_mode = inform_scr.update(is_clicked,mouse_pos,keys)
    elif(cur_mode==2):
        next_mode = math_scr.update(is_clicked,mouse_pos)
        cur_mode=next_mode
    elif(cur_mode==3):
        next_mode=memo_scr.update(is_clicked,mouse_pos)
        cur_mode=next_mode
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
