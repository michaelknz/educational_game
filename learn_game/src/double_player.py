import pygame
from player import player

class double_player:
    def __init__(self,screen,path1,path2,start_poses,tile_size):
        self.Player1=player(screen,path1,start_poses[0],tile_size)
        self.Player2=player(screen,path2,start_poses[1],tile_size)
        self.is_exec=True
        self.num=2
        self.cur_num=0
        self.map=0
        self.map_size=0

    def set_poses(self,start_poses,fin_poses):
        self.Player1.set_poses(start_poses[0],fin_poses[0])
        self.Player2.set_poses(start_poses[1],fin_poses[1])

    def set_map(self,map,map_size):
        self.Player1.set_map(map,map_size)
        self.Player2.set_map(map,map_size)
        self.map=map
        self.map_size=map_size

    def to_start(self):
        self.Player1.to_start()
        self.Player2.to_start()

    def Clear_movings(self):
        self.Player1.Clear_movings()
        self.Player2.Clear_movings()

    def right(self,x):
        if(self.cur_num==0):
            self.Player1.right(x)
        else:
            self.Player2.right(x)

    def left(self,x):
        if(self.cur_num==0):
            self.Player1.left(x)
        else:
            self.Player2.left(x)

    def up(self,x):
        if(self.cur_num==0):
            self.Player1.up(x)
        else:
            self.Player2.up(x)

    def down(self,x):
        if(self.cur_num==0):
            self.Player1.down(x)
        else:
            self.Player2.down(x)

    def is_down_free(self):
        if(self.cur_num==0):
            u=self.Player1.pos_in_quads.copy()
            for i in range(len(self.Player1.movings)):
                if self.Player1.movings[i][0]=='l':
                    u[0]-=1
                elif self.Player1.movings[i][0]=='r':
                    u[0]+=1
                elif self.Player1.movings[i][0]=='d':
                    u[1]+=1
                else:
                    u[1]-=1
            if(u[1]+1<self.map_size[1] and self.map[(u[1]+1)*self.map_size[0]+u[0]]!='G'):
                return True
            else:
                return False
        else:
            u=self.Player2.pos_in_quads.copy()
            for i in range(len(self.Player2.movings)):
                if self.Player2.movings[i][0]=='l':
                    u[0]-=1
                elif self.Player2.movings[i][0]=='r':
                    u[0]+=1
                elif self.Player2.movings[i][0]=='d':
                    u[1]+=1
                else:
                    u[1]-=1
            if(u[1]+1<self.map_size[1] and self.map[(u[1]+1)*self.map_size[0]+u[0]]!='G'):
                return True
            else:
                return False

    def is_up_free(self):
        if(self.cur_num==0):
            u=self.Player1.pos_in_quads.copy()
            for i in range(len(self.Player1.movings)):
                if self.Player1.movings[i][0]=='l':
                    u[0]-=1
                elif self.Player1.movings[i][0]=='r':
                    u[0]+=1
                elif self.Player1.movings[i][0]=='d':
                    u[1]+=1
                else:
                    u[1]-=1
            if(u[1]-1>=0 and self.map[(u[1]-1)*self.map_size[0]+u[0]]!='G'):
                return True
            else:
                return False
        else:
            u=self.Player2.pos_in_quads.copy()
            for i in range(len(self.Player2.movings)):
                if self.Player2.movings[i][0]=='l':
                    u[0]-=1
                elif self.Player2.movings[i][0]=='r':
                    u[0]+=1
                elif self.Player2.movings[i][0]=='d':
                    u[1]+=1
                else:
                    u[1]-=1
            if(u[1]-1>=0 and self.map[(u[1]-1)*self.map_size[0]+u[0]]!='G'):
                return True
            else:
                return False

    def is_right_free(self):
        if(self.cur_num==0):
            u=self.Player1.pos_in_quads.copy()
            for i in range(len(self.Player1.movings)):
                if self.Player1.movings[i][0]=='l':
                    u[0]-=1
                elif self.Player1.movings[i][0]=='r':
                    u[0]+=1
                elif self.Player1.movings[i][0]=='d':
                    u[1]+=1
                else:
                    u[1]-=1
            if(u[0]+1<self.map_size[0] and self.map[u[1]*self.map_size[0]+u[0]+1]!='G'):
                return True
            else:
                return False
        else:
            u=self.Player2.pos_in_quads.copy()
            for i in range(len(self.Player2.movings)):
                if self.Player2.movings[i][0]=='l':
                    u[0]-=1
                elif self.Player2.movings[i][0]=='r':
                    u[0]+=1
                elif self.Player2.movings[i][0]=='d':
                    u[1]+=1
                else:
                    u[1]-=1
            if(u[0]+1<self.map_size[0] and self.map[u[1]*self.map_size[0]+u[0]+1]!='G'):
                return True
            else:
                return False

    def is_left_free(self):
        if(self.cur_num==0):
            u=self.Player1.pos_in_quads.copy()
            for i in range(len(self.Player1.movings)):
                if self.Player1.movings[i][0]=='l':
                    u[0]-=1
                elif self.Player1.movings[i][0]=='r':
                    u[0]+=1
                elif self.Player1.movings[i][0]=='d':
                    u[1]+=1
                else:
                    u[1]-=1
            if(u[0]-1>=0 and self.map[u[1]*self.map_size[0]+u[0]-1]!='G'):
                return True
            else:
                return False
        else:
            u=self.Player2.pos_in_quads.copy()
            for i in range(len(self.Player2.movings)):
                if self.Player2.movings[i][0]=='l':
                    u[0]-=1
                elif self.Player2.movings[i][0]=='r':
                    u[0]+=1
                elif self.Player2.movings[i][0]=='d':
                    u[1]+=1
                else:
                    u[1]-=1
            if(u[0]-1>=0 and self.map[u[1]*self.map_size[0]+u[0]-1]!='G'):
                return True
            else:
                return False

    def update(self,is_finished):
        self.Player1.is_exec=self.is_exec
        self.Player2.is_exec=self.is_exec
        a=self.Player1.update(is_finished)
        b=self.Player2.update(is_finished)
        if(len(self.Player1.movings)==0 and a==0):
            self.Player2.Clear_movings()
            self.Player2.to_start()
            self.Player2.animIndex=0
            self.Player2.surf=self.Player2.still
            self.is_exec=True
        if(len(self.Player2.movings)==0 and b==0):
            self.Player1.Clear_movings()
            self.Player1.to_start()
            self.Player1.animIndex=0
            self.Player1.surf=self.Player1.still
            self.is_exec=True
        if(a==1 and b==1):
            return 1
        else:
            return 0
