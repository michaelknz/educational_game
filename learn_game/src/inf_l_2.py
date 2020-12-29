import pygame
from inf_l_base import inf_l_base
from player import player

class inf_l_2(inf_l_base):
    def build_map(self):
        self.map=['G','G','G','G','G','G','G','G',
                  'DL','D-L','G','DL','H','D-L','G','G',
                  'G','V','G','G','G','V','G','G',
                  'G','V','G','G','G','V','G','G',
                  'G','V','R-D','H','H','L-U','G','G',
                  'G','V','V','G','G','G','G','G',
                  'G','V','V','G','G','G','G','G',
                  'G','U-R','L-U','G','G','G','G','G',]
        self.start_pos=[0,1]
        self.fin_pos=[3,1]
        self.level_num=2

    def syntax_lighting(self):
        s=set()
        c=set(['boy'])
        m=set(['right','left','down','up'])
        self.editor.set_lighting(s,c,m)
        self.edb.set_Cname(list(c)[0])

    def set_hero(self):
        self.hero=player(self.screen,'res/hero.png',self.start_pos.copy(),self.tile_size)
        self.hero.set_poses(self.start_pos,self.fin_pos)

    def to_start(self):
        self.is_finished=False
        self.is_error=False
        self.hero.to_start()

    def set_start(self):
        out=[]
        text="Congratulations!\nYou passed first level!\nNow you need to go\nthrough more difficult path."
        out.append(text)
        text="The list of commands\n is not changed."
        out.append(text)
        text="boy.right(N)-move right on N cells\nboy.left(N)-move left on N cells\nboy.up(N)-move up on N cells\nboy.down(N)-move down on\nN cells"
        out.append(text)
        self.message.set_start_text(out)


