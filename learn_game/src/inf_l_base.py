import pygame
from code_writer import code_writer
from editor_bar import editor_bar
from message_box import message_box

class inf_l_base:
    def __init__(self,screen,tile_size):
        self.screen=screen
        self.tex=pygame.image.load("res/map_tex.png")
        self.tile_tex_size=(64,64)
        self.tile_size=tile_size
        self.dict={}
        self.dict_init()
        self.map_size=(screen.get_width()*3//4//self.tile_size[0],screen.get_height()//self.tile_size[1])
        self.map=[]
        self.start_pos=0
        self.fin_pos=0
        self.level_num=0
        self.build_map()
        self.is_finished=False
        self.is_error=False
        self.is_start=True
        self.hero=0
        self.editor=code_writer(self.screen,(screen.get_width()*3//4,0))
        self.set_hero()
        self.edb=editor_bar(screen,self.hero,self.editor,(screen.get_width()*3//4,screen.get_height()*7//8))
        self.message=message_box(screen)
        self.syntax_lighting()
        self.set_start()

    def image_at(self,i,j,colorkey=None):
        rect = pygame.Rect((i*self.tile_tex_size[0],j*self.tile_tex_size[1],(i+1)*self.tile_tex_size[0],(j+1)*self.tile_tex_size[1]))
        image = pygame.Surface((self.tile_tex_size[0],self.tile_tex_size[1])).convert()
        image.blit(self.tex, (0, 0), rect)
        image=pygame.transform.scale(image,(self.tile_size[0],self.tile_size[1]))
        if colorkey is not None:
            if colorkey == -1:
                colorkey = image.get_at((0,0))
            image.set_colorkey(colorkey, pygame.RLEACCEL)
        return image

    def dict_init(self):
        self.dict={'G':(0,2),'H':(0,1),'V':(0,0),'DL':(8,3),'DR':(9,3),'DU':(8,2),'DD':(9,2),
                   'R-D':(5,0),'U-R':(5,1),'L-U':(6,1),'D-L':(6,0),'X':(9,0)}

    def draw_map(self):
        for i in range(self.map_size[1]):
            for j in range(self.map_size[0]):
                image=self.image_at(self.dict[self.map[i*self.map_size[0]+j]][0],self.dict[self.map[i*self.map_size[0]+j]][1])
                self.screen.blit(image,(j*self.tile_size[0],i*self.tile_size[1]))
                pygame.draw.polygon(self.screen,(255,255,255),[(self.tile_size[0]*j,self.tile_size[1]*i),(self.tile_size[0]*(j+1),self.tile_size[1]*i),(self.tile_size[0]*(j+1),self.tile_size[1]*(i+1)),(self.tile_size[0]*j,self.tile_size[1]*(i+1))],1)

    def update(self,keys,is_clicked,pos):
        self.draw_map()
        self.is_finished=self.hero.update(self.is_finished)
        self.editor.draw_ed(keys,self.is_finished)
        if(self.is_error):
            self.is_error = self.message.update_error(is_clicked,pos)
            self.editor.block()
            self.edb.block()
            self.edb.update(is_clicked,pos)
            return self.level_num
        else:
            self.editor.unblock()
            self.edb.unblock()
        if(self.is_start):
            self.is_start=self.message.update_start(is_clicked,pos)
            self.editor.block()
            self.edb.block()
            self.edb.update(is_clicked,pos)
            return self.level_num
        else:
            self.message.cur_start_p=0
            self.editor.unblock()
            self.edb.unblock()
        if(not self.is_finished):
            flag=0
            self.hero,self.is_error,flag = self.edb.update(is_clicked,pos,self.editor.is_in_set)
            if(flag==1):
                return 0
            elif(flag==2):
                self.is_start=True
        else:
            self.edb.update(is_clicked,pos)
            out=self.message.update_cong(is_clicked,pos,self.level_num)
            if(out==0):
                self.editor.clean_editor()
            return out
        return self.level_num

    def build_map(self):
        pass

    def syntax_lighting(self):
        pass

    def set_hero(self):
        pass

    def to_start(self):
        pass

    def set_start(self):
        pass