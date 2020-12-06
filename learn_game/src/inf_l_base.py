import pygame
from code_writer import code_writer

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
        self.build_map()
        self.editor=code_writer(self.screen,(screen.get_width()*3//4,0))

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
                   'R-D':(5,0),'U-R':(5,1),'L-U':(6,1),'D-L':(6,0)}

    def draw_map(self):
        for i in range(self.map_size[1]):
            for j in range(self.map_size[0]):
                image=self.image_at(self.dict[self.map[i*self.map_size[0]+j]][0],self.dict[self.map[i*self.map_size[0]+j]][1])
                self.screen.blit(image,(j*self.tile_size[0],i*self.tile_size[1]))

    def update(self,keys):
        self.draw_map()
        self.editor.draw_ed(keys)

    def build_map(self):
        pass