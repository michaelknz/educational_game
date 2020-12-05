import pygame
from button import button

class start_screen(pygame.sprite.Sprite):
    def __init__(self,screen,image_path):
        pygame.sprite.Sprite.__init__(self)
        self.screen=screen
        self.bg=pygame.image.load(image_path)
        self.bg=pygame.transform.scale(self.bg,(self.screen.get_width(),self.screen.get_height()))
        self.inf_but=button("res/buttons.png")
        self.inf_but.add_button((190,49),(190,45,380,95),"Информатика")
        self.inf_but.add_button((190,45),(0,50,190,95),"Информатика")
        self.font=pygame.font.SysFont('Corbel',100)
        self.title="Обучалка"

    def draw_bg(self):
        self.screen.blit(self.bg,(0,0))

    def draw_title(self,pos):
        t=self.font.render(self.title,True,(255,255,255))
        self.screen.blit(t,(pos[0]-t.get_width()//2,pos[1]-t.get_height()//2))

    def update(self, is_clicked, pos):
        self.draw_bg()
        self.draw_title((self.screen.get_width()//2,self.screen.get_height()//2-250))
        if(is_clicked and self.inf_but.check_pos_in_button(pos)):
            self.inf_but.draw_button(self.screen,1,(self.screen.get_width()//2,self.screen.get_height()//2-75))
            return 1
        else:
            self.inf_but.draw_button(self.screen,0,(self.screen.get_width()//2,self.screen.get_height()//2-75))
            return 0

