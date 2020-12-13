import pygame
from button import button

class editor_bar:
    def __init__(self,screen,hero,editor,start_pos):
        self.screen=screen
        self.hero=hero
        self.start_pos=start_pos
        self.editor=editor
        self.size=(abs(screen.get_width()-start_pos[0]),abs(screen.get_height()-start_pos[1]))
        self.run=button("res/button_blue.png")
        self.run.add_button((49,48),(339,95,388,143),'run',(255,255,255))
        self.run.add_button((49,45),(290,95,340,140),'run',(255,255,255))
        self.run.draw_button(screen,0,(start_pos[0]+(screen.get_width()-start_pos[0])//2,start_pos[1]+(screen.get_height()-start_pos[1])//2))
        self.bg_color=(25,25,75)

    def draw_bg(self):
        bg=pygame.Surface((self.size[0],self.size[1]))
        bg.fill(self.bg_color)
        self.screen.blit(bg,self.start_pos)

    def draw_button(self,is_clicked,pos):
        if(is_clicked and self.run.check_pos_in_button(pos)):
            self.run.draw_button(self.screen,1,self.run.pos)
        else:
            self.run.draw_button(self.screen,0,self.run.pos)

    def execute(self,is_clicked,pos):
        if(is_clicked and self.run.check_pos_in_button(pos) and self.hero.is_exec):
            h=self.hero
            exec(self.editor.code)
            h.is_exec=False
            self.hero=h
        return self.hero

    def update(self,is_clicked,pos):
        self.draw_bg()
        self.draw_button(is_clicked,pos)
        self.execute(is_clicked,pos)
        return self.hero