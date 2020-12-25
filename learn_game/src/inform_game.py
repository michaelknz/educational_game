import pygame
from button import button
from inf_l_1 import inf_l_1

class inform_game(object):
    def __init__(self,screen,image_path):
        self.screen=screen
        self.bg=pygame.image.load(image_path)
        self.bg=pygame.transform.scale(self.bg,(self.screen.get_width(),self.screen.get_height()))
        self.buttons=[]
        self.levels=[]
        self.init_buttons()
        self.init_levels()
        self.cur_level=0
        self.next_level=0

    def init_buttons(self):
        for i in range(1):
            self.buttons.append(button("res/button_blue.png"))
            self.buttons[i].add_button((49,48),(339,95,388,143),str(i+1),(255,255,255))
            self.buttons[i].add_button((49,45),(290,95,340,140),str(i+1),(255,255,255))
        self.return_button=button("res/button_blue.png")
        self.return_button.add_button((49,48),(339,95,388,143),'',(255,255,255))
        self.return_button.add_button((49,45),(290,95,340,140),'',(255,255,255))
        self.return_button.set_picture('res/icons.png',(4*51-5,51+5,5*51-5,2*51+5),(40,40))

    def levels_to_start(self):
        for i in range(len(self.levels)):
            self.levels[i].to_start()

    def init_levels(self):
        self.levels.append(inf_l_1(self.screen,(150,100)))

    def draw_bg(self):
        self.screen.blit(self.bg,(0,0))

    def draw_buttons(self,is_clicked,pos):
        for i in range(len(self.buttons)):
            if(is_clicked and self.buttons[i].check_pos_in_button(pos)):
                self.next_level=i+1
                self.buttons[i].draw_button(self.screen,1,(100+i*25,100))
            else:
                self.buttons[i].draw_button(self.screen,0,(100+i*25,100))
        if(is_clicked and self.return_button.check_pos_in_button(pos)):
            self.next_level=-1
            self.return_button.draw_button(self.screen,1,(self.screen.get_width()-100,self.screen.get_height()-100))
        else:
            self.return_button.draw_button(self.screen,0,(self.screen.get_width()-100,self.screen.get_height()-100))

    def update(self,is_clicked,pos,keys):
        if(is_clicked==False):
            self.cur_level=self.next_level
        if(self.cur_level==0):
            self.draw_bg()
            self.draw_buttons(is_clicked,pos)
            self.levels_to_start()
        elif(self.next_level!=-1):
            self.next_level = self.levels[self.cur_level-1].update(keys,is_clicked,pos)
        if(self.next_level==-1):
            self.next_level=0
            self.cur_level=0
            return 0

        return 1
