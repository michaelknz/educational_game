import copy
import pygame
from inf_l_base import inf_l_base
from double_player import double_player

class inf_l_4(inf_l_base):
    def build_map(self):
        self.map=['G','G','G','G','G','G','G','G',
                  'DL','H','H','D-L','G','G','G','G',
                  'G','G','G','V','G','G','G','G',
                  'G','G','G','V','G','G','G','G',
                  'DL','H','H','X','H','H','H','DR',
                  'G','G','G','V','G','G','G','G',
                  'G','G','G','V','G','G','G','G',
                  'G','G','G','U-R','H','H','H','DR']
        self.start_pos=[[0,1],[7,4]]
        self.fin_pos=[[7,7],[0,4]]
        self.level_num=4

    def syntax_lighting(self):
        s=set(['if','else'])
        c=set(['group'])
        m=set(['right','left','down','up','is_up_free','is_down_free','is_right_free','is_left_free'])
        self.editor.set_lighting(s,c,m)
        self.edb.set_Cname(list(c)[0])

    def set_hero(self):
        self.hero=double_player(self.screen,'res/hero.png','res/second_hero.png',copy.deepcopy(self.start_pos),self.tile_size)
        self.hero.set_poses(copy.deepcopy(self.start_pos),copy.deepcopy(self.fin_pos))
        self.hero.set_map(self.map,self.map_size)

    def to_start(self):
        self.is_finished=False
        self.is_error=False
        self.hero.to_start()

    def set_start(self):
        out=[]
        text='Now you need to solve more\ndifficult problem with operators\n"if-else".'
        out.append(text)
        text='The list of instructions is not\nchanged.\ngroup.right(N)-move right on N\ncells\ngroup.left(N)-move left on N cells\ngroup.up(N)-move up on N cells'
        out.append(text)
        text='group.down(N)-move down on\nN cells\ngroup.is_right_free()-returns true\nif hero can go right.\ngroup.is_left_free()-returns true\nif hero can go left.'
        out.append(text)
        text='group.is_up_free()-returns true\nif hero can go up.\ngroup.is_down_free()-returns true\nif hero can go down.'
        out.append(text)
        self.message.set_start_text(out)