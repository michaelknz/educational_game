import pygame

class player:
    def __init__(self,screen,path,pos,step):
        self.screen=screen
        self.path=path
        self.move_side=[]
        self.get_wimages()
        self.pos=[pos[0]*step[0],pos[1]*step[1]]
        self.pos_in_quads=pos
        self.step=step
        self.del_col=75
        self.movings=[]
        self.animP=0.1
        self.animIndex=0
        self.cur_del=0
        self.still=self.image_at((0,0,96,128),(96,128))
        self.surf=self.still
        self.is_exec=True
        self.is_flip=False

    def image_at(self, rectangle, size):
        self.sheet = pygame.image.load(self.path).convert()
        rect = pygame.Rect(rectangle)
        image = pygame.Surface(size).convert()
        image.blit(self.sheet, (0, 0), rect)
        image.set_colorkey((0,0,0))
        return image

    def get_wimages(self):
        for i in range(1,8):
            self.move_side.append(self.image_at((i*96,128*4,(i+1)*96,128*5),(96,128)))

    def Clear_movings(self):
        self.movings.clear()

    def right(self,x):
        if(self.is_exec):
            for i in range(x):
                self.movings.append(['r',self.del_col])

    def left(self,x):
        if(self.is_exec):
            for i in range(x):
                self.movings.append(['l',self.del_col])

    def down(self,x):
        if(self.is_exec):
            for i in range(x):
                self.movings.append(['d',self.del_col])

    def up(self,x):
        if(self.is_exec):
            for i in range(x):
                self.movings.append(['u',self.del_col])

    def animation(self):
        self.animIndex+=self.animP
        if(self.animIndex>7.0):
            self.animIndex-=7.0
        self.surf=self.move_side[int(self.animIndex)]

    def to_start(self):
        self.pos_in_quads=self.start_pos.copy()
        self.pos=[self.start_pos[0]*self.step[0],self.start_pos[1]*self.step[1]]

    def set_poses(self,start,fin):
        self.start_pos=start.copy()
        self.fin_pos=fin.copy()

    def update(self,is_finished,map,tile_col):
        if(is_finished):
            self.screen.blit(self.surf,(self.pos[0],self.pos[1]-self.surf.get_height()//2))
            return 1
        if(len(self.movings)!=0):
            if(self.movings[0][1]==0):
                self.cur_del=0
                if(self.movings[0][0]== 'r'):
                    self.pos_in_quads[0]+=1
                elif(self.movings[0][0]== 'l'):
                    self.pos_in_quads[0]-=1
                elif(self.movings[0][0]== 'd'):
                    self.pos_in_quads[1]+=1
                elif(self.movings[0][0]== 'u'):
                    self.pos_in_quads[1]-=1
                self.movings.pop(0)
                if(self.check(map,tile_col)):
                    self.Clear_movings()
                self.animIndex=0
                self.surf=self.still
                if(len(self.movings)==0):
                    if(self.pos_in_quads[0]==self.fin_pos[0] and self.pos_in_quads[1]==self.fin_pos[1]):
                        return 1
                    else:
                        self.pos_in_quads=self.start_pos.copy()
                        self.pos=[self.start_pos[0]*self.step[0],self.start_pos[1]*self.step[1]]
                    self.is_exec=True
                    self.is_flip=False
                    return 0 
            if(self.cur_del==0):
                if(self.movings[0][0]== 'r' or self.movings[0][0]== 'l'):
                    self.cur_del=self.step[0]/self.movings[0][1]
                else:
                    self.cur_del=self.step[1]/self.movings[0][1]
            if(self.movings[0][0]== 'r'):
                self.pos[0]+=self.cur_del
                self.is_flip=False
            elif(self.movings[0][0]== 'l'):
                self.pos[0]-=self.cur_del
                self.is_flip=True
            elif(self.movings[0][0]== 'd'):
                self.pos[1]+=self.cur_del
            elif(self.movings[0][0]== 'u'):
                self.pos[1]-=self.cur_del
            self.animation()
            self.movings[0][1]-=1

        else:
            self.is_exec=True
        self.screen.blit(pygame.transform.flip(self.surf,self.is_flip,False),(self.pos[0],self.pos[1]-self.surf.get_height()//2))
        return 0

    def check(self,map,map_size):
        if(map[self.pos_in_quads[1]*map_size[0]+self.pos_in_quads[0]]=='G' or self.pos_in_quads[1]<0 or self.pos_in_quads[1]>=map_size[1] or self.pos_in_quads[0]<0 or self.pos_in_quads[0]>=map_size[0]):
            return True
        else:
            return False