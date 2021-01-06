import copy
import pygame
from inf_l_base import inf_l_base
from double_player import double_player

class inf_l_3(inf_l_base):
    def build_map(self):
        self.map=['G','G','G','G','G','G','G','G',
                  'DL','H','D-L','G','G','R-D','H','DR',
                  'G','G','V','G','G','V','G','G',
                  'G','G','V','G','G','V','G','G',
                  'G','G','V','G','G','V','G','G',
                  'G','G','V','G','G','V','G','G',
                  'G','G','V','G','G','V','G','G',
                  'DL','H','L-U','G','G','U-R','H','DR']
        self.start_pos=[[0,1],[7,1]]
        self.fin_pos=[[0,7],[7,7]]
        self.level_num=3

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
        text='On this level you will use\nnew operator - if.\nIf you put in this operator\nexpression that is true,\nprogram will run part of code that\nis in body of operator,\notherwise not.'
        out.append(text)
        text='Operator "if" has the following\nform:\nif <expression>:\n#body of operator.'
        out.append(text)
        text='Note that you need to press Tab\nbefore writing every line\nof code that is in operator body.'
        out.append(text)
        text='In this task you can also use\noperator "else". Part of code that\ncontains in the body of this\noperator will be executed only if\nexperession in previouse operator\n"if" is false.'
        out.append(text)
        text='Note that operator "else" can be\nused only after "if" operator.'
        out.append(text)
        text='Operator "else" has the following\nform:\nelse:\n#body of operator.\nHere you also need Tabs before\nlines in operator body.'
        out.append(text)
        text='Now you will need to control two\npeople. And if you write command\nBOTH of people will execute it.'
        out.append(text)
        text='List of comands:\ngroup.right(N)-move right on N\ncells\ngroup.left(N)-move left on N cells\ngroup.up(N)-move up on N cells\ngroup.down(N)-move down on\nN cells'
        out.append(text)
        text='group.is_right_free()-returns true\nif hero can go right.\ngroup.is_left_free()-returns true\nif hero can go left.\ngroup.is_up_free()-returns true\nif hero can go up.'
        out.append(text)
        text='group.is_down_free()-returns true\nif hero can go down.'
        out.append(text)
        self.message.set_start_text(out)
