import pygame
from inf_l_base import inf_l_base
from player import player

class inf_l_1(inf_l_base):
    def build_map(self):
        self.map=['G','G','G','G','G','G','G','G',
                  'DL','H','H','H','D-L','G','G','G',
                  'G','G','G','G','U-R','H','H','DR',
                  'G','G','G','G','G','G','G','G',
                  'G','G','G','G','G','G','G','G',
                  'G','G','G','G','G','G','G','G',
                  'G','G','G','G','G','G','G','G',
                  'G','G','G','G','G','G','G','G',]
        self.start_pos=[0,1]
        self.fin_pos=[7,2]
        self.level_num=1

    def syntax_lighting(self):
        s=set()
        c=set(['boy'])
        m=set(['right','left','down','up'])
        self.editor.set_lighting(s,c,m)

    def set_hero(self):
        self.hero=player(self.screen,'res/hero.png',self.start_pos.copy(),self.tile_size)
        self.hero.set_poses(self.start_pos,self.fin_pos)
        self.editor.code='boy.right(4)\nboy.down(1)\nboy.right(3)'

    def to_start(self):
        self.is_finished=False
        self.is_error=False
        self.hero.to_start()