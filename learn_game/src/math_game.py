import pygame
from button import button

class math_game:
    def __init__(self,screen,path):
        self.screen=screen
        self.bg=pygame.image.load(path)
        self.bg=pygame.transform.scale(self.bg,(self.screen.get_width(),self.screen.get_height()))
        self.return_but=button("res/button_blue.png")
        self.return_but.add_button((49,48),(339,95,388,143),'',(255,255,255))
        self.return_but.add_button((49,45),(290,95,340,140),'',(255,255,255))
        self.return_but.set_picture('res/icons.png',(4*51-5,51+5,5*51-5,2*51+5),(40,40))
        self.return_but.draw_button(self.screen,0,(self.screen.get_width()-100,self.screen.get_height()-100))
        self.ans_1_but=button("res/button_blue.png")
        self.ans_2_but=button("res/button_blue.png")
        self.ans_3_but=button("res/button_blue.png")
        self.ans_4_but=button("res/button_blue.png")
        self.ans_1_but.add_button((190,49),(0,0,190,49),'',(255,255,255))
        self.ans_1_but.add_button((190,45),(0,50,190,95),'',(255,255,255))
        self.ans_2_but.add_button((190,49),(0,0,190,49),'',(255,255,255))
        self.ans_2_but.add_button((190,45),(0,50,190,95),'',(255,255,255))
        self.ans_3_but.add_button((190,49),(0,0,190,49),'',(255,255,255))
        self.ans_3_but.add_button((190,45),(0,50,190,95),'',(255,255,255))
        self.ans_4_but.add_button((190,49),(0,0,190,49),'',(255,255,255))
        self.ans_4_but.add_button((190,45),(0,50,190,95),'',(255,255,255))
        x=self.screen.get_width()//2
        y=self.screen.get_height()//2+180
        self.ans_1_but.draw_button(self.screen,0,(x-100,y-30))
        self.ans_2_but.draw_button(self.screen,0,(x+100,y-30))
        self.ans_3_but.draw_button(self.screen,0,(x-100,y+30))
        self.ans_4_but.draw_button(self.screen,0,(x+100,y+30))

    def draw_bg(self):
        self.screen.blit(self.bg,(0,0))

    def draw_buttons(self,is_clicked,pos):
        out=0
        if(is_clicked and self.ans_1_but.check_pos_in_button(pos)):
            self.ans_1_but.draw_button(self.screen,1,self.ans_1_but.pos)
            out=1
        else:
            self.ans_1_but.draw_button(self.screen,0,self.ans_1_but.pos)
        if(is_clicked and self.ans_2_but.check_pos_in_button(pos)):
            self.ans_2_but.draw_button(self.screen,1,self.ans_2_but.pos)
            out=2
        else:
            self.ans_2_but.draw_button(self.screen,0,self.ans_2_but.pos)
        if(is_clicked and self.ans_3_but.check_pos_in_button(pos)):
            self.ans_3_but.draw_button(self.screen,1,self.ans_3_but.pos)
            out=3
        else:
            self.ans_3_but.draw_button(self.screen,0,self.ans_3_but.pos)
        if(is_clicked and self.ans_4_but.check_pos_in_button(pos)):
            self.ans_4_but.draw_button(self.screen,1,self.ans_4_but.pos)
            out=4
        else:
            self.ans_4_but.draw_button(self.screen,0,self.ans_4_but.pos)
        return out

    def update(self,is_clicked,pos):
        self.draw_bg()
        if(is_clicked and self.return_but.check_pos_in_button(pos)):
            self.return_but.draw_button(self.screen,1,self.return_but.pos)
            return 0
        else:
            self.return_but.draw_button(self.screen,0,self.return_but.pos)
        self.draw_buttons(is_clicked,pos)
        return 2