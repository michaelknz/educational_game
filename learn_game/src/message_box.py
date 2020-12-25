import pygame
from button import button

class message_box:
    def __init__(self,screen):
        self.screen=screen
        self.surf=pygame.Surface((320,320)).convert()
        self.surf.set_colorkey((255,255,255))
        self.path='res/UI_1.png'
        self.load_bg()
        self.congr_but=button("res/buttons.png")
        self.congr_but.add_button((190,49),(190,45,380,95),"Уровень пройден!")
        self.congr_but.add_button((190,45),(0,50,190,95),"Уровень пройден!")
        self.ok_but=button("res/buttons.png")
        self.ok_but.add_button((190,49),(190,45,380,95),"OK")
        self.ok_but.add_button((190,45),(0,50,190,95),"OK")
        self.font=pygame.font.SysFont('Corbel',100)


    def load_bg(self):
        size=(16,16)
        sheet=pygame.image.load(self.path).convert()
        mid=pygame.Surface(size).convert()
        ri=pygame.Surface(size).convert()
        le=pygame.Surface(size).convert()
        up=pygame.Surface(size).convert()
        down=pygame.Surface(size).convert()
        luc=pygame.Surface(size).convert()
        ruc=pygame.Surface(size).convert()
        rdc=pygame.Surface(size).convert()
        ldc=pygame.Surface(size).convert()
        ldc.set_colorkey((0,0,0))
        mid.blit(sheet,(0,0),(252,378,268,394))
        ri.blit(sheet,(0,0),(270,378,286,394))
        le.blit(sheet,(0,0),(234,378,250,394))
        up.blit(sheet,(0,0),(252,360,268,376))
        down.blit(sheet,(0,0),(252,396,268,412))
        luc.blit(sheet,(0,0),(288,360,304,376))
        ruc.blit(sheet,(0,0),(306,360,322,376))
        rdc.blit(sheet,(0,0),(306,378,322,394))
        ldc.blit(sheet,(0,0),(288,378,304,394))
        for y in range(20):
            for x in range(20):
                if(x==0 and y==0):
                    self.surf.blit(luc,(0,0))
                elif(x==19 and y==19):
                    self.surf.blit(rdc,(x*size[0],y*size[1]))
                elif(x==0 and y==19):
                    self.surf.blit(ldc,(x*size[0],y*size[1]))
                elif(x==19 and y==0):
                    self.surf.blit(ruc,(x*size[0],y*size[1]))
                elif(x==0):
                    self.surf.blit(le,(x*size[0],y*size[1]))
                elif(y==0):
                    self.surf.blit(up,(x*size[0],y*size[1]))
                elif(x==19):
                    self.surf.blit(ri,(x*size[0],y*size[1]))
                elif(y==19):
                    self.surf.blit(down,(x*size[0],y*size[1]))
                else:
                    self.surf.blit(mid,(x*size[0],y*size[1]))

    def draw_cong(self):
        image = pygame.image.load('res/congratulations.png')
        colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
        self.screen.blit(self.surf,(self.screen.get_width()*3//8-self.surf.get_width()//2,self.screen.get_height()//2-self.surf.get_height()//2))
        self.screen.blit(image,(self.screen.get_width()*2//8+50,self.screen.get_height()*2//8+60))
        self.congr_but.draw_button(self.screen,0,(self.screen.get_width()*3//8,self.screen.get_height()*5//8))
        
    def draw_error(self):
        self.screen.blit(self.surf,(self.screen.get_width()*3//8-self.surf.get_width()//2,self.screen.get_height()//2-self.surf.get_height()//2))
        image=pygame.image.load('res/Error.png')
        image=pygame.transform.scale(image,(75,75))
        colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
        self.screen.blit(image,(self.screen.get_width()*3//8-30,self.screen.get_height()//2-150))
        self.ok_but.draw_button(self.screen,0,(self.screen.get_width()*3//8,self.screen.get_height()*5//8))
        f=pygame.font.SysFont('Corbel',30)
        t=f.render("Somthing went wrong",True,(255,255,255))
        self.screen.blit(t,(self.screen.get_width()*3//8-t.get_width()//2,self.screen.get_height()//2-60))


    def update_cong(self,is_clicked,pos,ln):
        self.draw_cong()
        if(is_clicked and self.congr_but.check_pos_in_button(pos)):
            self.congr_but.draw_button(self.screen,1,(self.screen.get_width()*3//8,self.screen.get_height()*5//8))
            return 0
        else:
            self.congr_but.draw_button(self.screen,0,(self.screen.get_width()*3//8,self.screen.get_height()*5//8))
            return ln

    def update_error(self,is_clicked,pos):
        self.draw_error()
        if(is_clicked and self.ok_but.check_pos_in_button(pos)):
            self.ok_but.draw_button(self.screen,1,(self.screen.get_width()*3//8,self.screen.get_height()*5//8))
            return False
        else:
            self.ok_but.draw_button(self.screen,0,(self.screen.get_width()*3//8,self.screen.get_height()*5//8))
            return True
