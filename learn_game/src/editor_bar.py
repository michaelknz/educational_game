import pygame
from button import button

class editor_bar:
    def __init__(self,screen,hero,editor,start_pos):
        self.screen=screen
        self.hero=hero
        self.start_pos=start_pos
        self.class_name=''
        self.editor=editor
        self.size=(abs(screen.get_width()-start_pos[0]),abs(screen.get_height()-start_pos[1]))
        self.run=button("res/button_blue.png")
        self.run.add_button((49,48),(339,95,388,143),'run',(255,255,255))
        self.run.add_button((49,45),(290,95,340,140),'run',(255,255,255))
        self.run.draw_button(screen,0,(start_pos[0]+(screen.get_width()-start_pos[0])//2,start_pos[1]+(screen.get_height()-start_pos[1])//2))
        self.ret=button("res/button_blue.png")
        self.ret.add_button((49,48),(339,95,388,143),'',(255,255,255))
        self.ret.add_button((49,45),(290,95,340,140),'',(255,255,255))
        self.ret.set_picture('res/icons.png',(4*51-5,51+5,5*51-5,2*51+5),(40,40))
        self.ret.draw_button(screen,0,(start_pos[0]+(screen.get_width()-start_pos[0])//2+self.run.images[0].get_width()+50,start_pos[1]+(screen.get_height()-start_pos[1])//2))
        self.qw=button("res/button_blue.png")
        self.qw.add_button((49,48),(339,95,388,143),'',(255,255,255))
        self.qw.add_button((49,45),(290,95,340,140),'',(255,255,255))
        self.qw.set_picture('res/icons.png',(204,110,244,150),(40,40))
        self.qw.draw_button(screen,0,(start_pos[0]+(screen.get_width()-start_pos[0])//2-self.run.images[0].get_width()-50,start_pos[1]+(screen.get_height()-start_pos[1])//2))
        self.bg_color=(25,25,75)
        self.is_block=False

    def draw_bg(self):
        bg=pygame.Surface((self.size[0],self.size[1]))
        bg.fill(self.bg_color)
        self.screen.blit(bg,self.start_pos)

    def draw_button(self,is_clicked,pos):
        if(is_clicked and self.qw.check_pos_in_button(pos)):
            self.qw.draw_button(self.screen,1,self.qw.pos)
        else:
            self.qw.draw_button(self.screen,0,self.qw.pos)
        if(is_clicked and self.ret.check_pos_in_button(pos)):
            self.ret.draw_button(self.screen,1,self.ret.pos)
        else:
            self.ret.draw_button(self.screen,0,self.ret.pos)
        if(is_clicked and self.run.check_pos_in_button(pos)):
            self.run.draw_button(self.screen,1,self.run.pos)
        else:
            self.run.draw_button(self.screen,0,self.run.pos)

    def execute(self,is_clicked,pos, is_norm):
        bout=False
        flag=0
        if(is_clicked and self.ret.check_pos_in_button(pos) and self.hero.is_exec and (not self.is_block)):
            flag=1
        if(is_clicked and self.qw.check_pos_in_button(pos) and self.hero.is_exec and (not self.is_block)):
            flag=2
        if(is_clicked and self.run.check_pos_in_button(pos) and self.hero.is_exec and (not self.is_block)):
            locals().update({self.class_name:self.hero})
            if(not is_norm):
                locals()[self.class_name].Clear_movings()
                bout=True
                self.hero=locals()[self.class_name]
                return (self.hero,bout,flag)
            for i in range(self.hero.num):
                if(self.hero.num>1):
                    self.hero.cur_num=i
                try:
                    exec(self.editor.code)
                except:
                    locals()[self.class_name].Clear_movings()
                    bout=True
            locals()[self.class_name].is_exec=False
            self.hero=locals()[self.class_name]
        return (self.hero,bout,flag)

    def block(self):
        self.is_block=True

    def unblock(self):
        self.is_block=False

    def update(self,is_clicked,pos,is_norm=True):
        self.draw_bg()
        self.draw_button(is_clicked,pos)
        return self.execute(is_clicked,pos,is_norm)

    def set_Cname(self,text):
        self.class_name=text