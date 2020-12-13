import pygame

class code_writer:
    def __init__(self,screen,start_pos):
        self.screen=screen
        self.start_pos=start_pos
        self.bg_color=(20,20,20)
        self.font = pygame.font.SysFont('Corbel',20)
        self.size=(abs(screen.get_width()-start_pos[0]),abs(screen.get_height()-start_pos[1]))
        self.caret=self.image_at("res/UI_1.png",(58,197,66,215),(8,18))
        self.code=""
        self.del_alpha=5
        self.cur_alpha=255
        self.special=set()
        self.divisors=set([' ','(',')'])
        self.colors={'special':(255,150,250),'digits':(0,255,0),'normal':(255,255,255),'divisors':(150,250,255),'str_num':(100,100,100)}

    def draw_bg(self):
        bg=pygame.Surface((self.size[0],self.size[1]))
        bg.fill(self.bg_color)
        self.screen.blit(bg,self.start_pos)

    def set_alpha(self,sur,cur):
        w, h = sur.get_size()
        for x in range(w):
            for y in range(h):
                a = sur.get_at((x, y))
                if(a[0]>0):
                    sur.set_at((x, y), pygame.Color(a[0], a[1], a[2], max(0,cur)))
        return sur

    def update_caret(self):
        self.cur_alpha-=self.del_alpha
        if(self.cur_alpha<=0 and self.del_alpha>0 or self.cur_alpha>=255 and self.del_alpha<0):
            self.del_alpha*=-1
        return self.set_alpha(self.caret,self.cur_alpha)

    def image_at(self, image_path, pos, size):
        png=pygame.image.load(image_path)
        rect = pygame.Rect(pos)
        image = pygame.Surface(size).convert_alpha()
        image.blit(png, (0, 0), rect)
        image.set_colorkey((0,0,0))
        return image

    def draw_line(self,line,pos):
        x=pos[0]+self.font.render(' ',True,(0,0,0)).get_width()*6
        y=pos[1]
        s=''
        b=False
        for i in line:
            if(i in self.divisors):
                color=0
                if(s.isdigit()):
                    color=self.colors['digits']
                elif(s in self.special):
                    color=self.colors['special']
                else:
                    color=self.colors['normal']
                t=self.font.render(s,True,color)
                self.screen.blit(t,(x,y))
                x+=t.get_width()
                t1=self.font.render(i,True,self.colors['divisors'])
                self.screen.blit(t1,(x,y))
                x+=t1.get_width()
                s=''
                b=True
            else:
                s+=i
        if(s=='EOF'):
            self.screen.blit(self.update_caret(),(x-self.font.render(' ',True,(0,0,0)).get_width(),y))
        else:
            color=0
            if(s.isdigit()):
                color=self.colors['digits']
            elif(s in self.special):
                color=self.colors['special']
            else:
                color=self.colors['normal']
            t=self.font.render(s,True,color)
            self.screen.blit(t,(x,y))

    def update_code(self,keys):
        for i in range(len(keys)):
            if(keys[i][0]==True and keys[i][1]==False):
                if(i==8):
                    self.code=self.code[:-1:]
                elif(i==13):
                    self.code+='\n'
                elif(i==9):
                    self.code+='    '
                else:
                    self.code+=keys[i][2]
                keys[i][1]=True

    def draw_text(self,keys):
        self.update_code(keys)
        x=self.start_pos[0]
        y=self.start_pos[1]
        j=1
        s=self.code+' EOF'
        mas=s.split('\n')
        if(len(s)==0):
            mas=[]
        for i in range(len(mas)):
            self.draw_line(mas[i],(x,y))
            x=self.start_pos[0]
            t=self.font.render(str(j),True,self.colors['str_num'])
            self.screen.blit(t,(x,y))
            j+=1
            y+=self.font.render('1',True,(0,0,0)).get_height()*(1.3)

    def set_lighting(self,s=set()):
        self.special=s.copy()


    def draw_ed(self,keys):
        self.draw_bg()
        self.draw_text(keys)
