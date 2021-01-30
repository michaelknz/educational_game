import pygame
from robot import robot
from inf_l_base import inf_l_base

class inf_l_6(inf_l_base):
    def build_map(self):
        self.map=['G','G','G','G','G','G','G','G',
                  'DL','H','H','H','D-L','G','G','G',
                  'G','G','G','G','V','G','G','G',
                  'G','G','G','G','V','G','G','G',
                  'G','G','G','G','V','G','G','G',
                  'G','G','G','G','V','G','G','G',
                  'G','G','G','G','V','G','G','G',
                  'G','G','G','G','U-R','H','H','DR']
        self.start_pos=[0,1]
        self.fin_pos=[7,7]
        self.level_num=6

    def syntax_lighting(self):
        s=set(['for','in','range'])
        c=set(['robot'])
        m=set(['move_right','move_left','move_up','move_down'])
        v=set(['i'])
        self.editor.set_lighting(s,c,m,v)
        self.edb.set_Cname(list(c)[0])

    def set_hero(self):
        self.hero=robot(self.screen,'res/robot.png',self.start_pos.copy(),self.tile_size)
        self.hero.set_poses(self.start_pos,self.fin_pos)
        self.hero.set_map(self.map,self.map_size)

    def to_start(self):
        self.is_finished=False
        self.is_error=False
        self.hero.to_start()

    def set_start(self):
        out=[]
        text="This level is similar to past, but\nhas more difficult path."
        out.append(text)
        text="The list of comands:\nrobot.move_right()-move robot\nright on one cell\nrobot.move_left()-move robot\nleft on one cell\nrobot.move_up()-move robot\nup on one cell"
        out.append(text)
        text="robot.move_down()-move robot\ndown on one cell"
        out.append(text)
        self.message.set_start_text(out)
