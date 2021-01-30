import pygame
from robot import robot
from inf_l_base import inf_l_base

class inf_l_5(inf_l_base):
    def build_map(self):
        self.map=['G','G','G','G','G','G','G','G',
                  'DL','H','H','H','H','H','H','DR',
                  'G','G','G','G','G','G','G','G',
                  'G','G','G','G','G','G','G','G',
                  'G','G','G','G','G','G','G','G',
                  'G','G','G','G','G','G','G','G',
                  'G','G','G','G','G','G','G','G',
                  'G','G','G','G','G','G','G','G']
        self.start_pos=[0,1]
        self.fin_pos=[7,1]
        self.level_num=5

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
        text="On this level you will learn\nhow to use another\nprogamming tool - loops."
        out.append(text)
        text="You can use them when you need\nto execute a bunch of\nsimilar operations."
        out.append(text)
        text="It has very simple syntax:\nfor i in range(num of executions):\n#code that you need to be\n#executed many times"
        out.append(text)
        text="The list of comands:\nrobot.move_right()-move robot\nright on one cell\nrobot.move_left()-move robot\nleft on one cell\nrobot.move_up()-move robot\nup on one cell"
        out.append(text)
        text="robot.move_down()-move robot\ndown on one cell"
        out.append(text)
        self.message.set_start_text(out)
