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
        self.time_delay=25
        self.first_time_delay=200
        self.caret_pos_in_text=0
        self.scaret_pos_on_screen=[start_pos[0]+self.font.render(' ',True,(0,0,0)).get_width()*6,start_pos[1]]
        self.caret_pos_on_screen=self.scaret_pos_on_screen.copy()
        self.special=set()
        self.classes=set()
        self.method=set()
        self.vars=set()
        self.divisors=set([' ','(',')','.',':'])
        self.colors={'special':(255,150,250),'digits':(0,255,0),'normal':(255,255,255),'divisors':(150,250,255),'str_num':(100,100,100),'method':(255,200,150),'class':(150,255,200),'vars':(255,255,0)}
        self.is_block=False
        self.is_in_set=True

    def draw_bg(self):
        bg=pygame.Surface((self.size[0],self.size[1]))
        bg.fill(self.bg_color)
        self.screen.blit(bg,self.start_pos)

    def clean_editor(self):
        self.code=''
        self.caret_pos_in_text=0
        self.caret_pos_on_screen=self.scaret_pos_on_screen.copy()

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
                elif(s in self.classes):
                    color=self.colors['class']
                elif(s in self.method):
                    color=self.colors['method']
                elif(s in self.vars):
                    color=self.colors['vars']
                else:
                    if(s!=''):
                        self.is_in_set=False
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
            self.screen.blit(self.update_caret(),(self.caret_pos_on_screen[0],self.caret_pos_on_screen[1]))
        else:
            color=0
            if(s.isdigit()):
                color=self.colors['digits']
            elif(s in self.special):
                color=self.colors['special']
            elif(s in self.classes):
                color=self.colors['class']
            elif(s in self.method):
                color=self.colors['method']
            elif(s in self.vars):
                color=self.colors['vars']
            else:
                if(s!=''):
                    self.is_in_set=False
                color=self.colors['normal']
            t=self.font.render(s,True,color)
            self.screen.blit(t,(x,y))

    def update_code(self,keys):
        if(self.is_block):
            return
        for i in range(len(keys)):
            if(keys[i][0]==True and keys[i][1]<=0):
                if(i==8 and len(self.code)!=0 and self.caret_pos_in_text>0):
                    self.code=self.code[:self.caret_pos_in_text-1:]+self.code[self.caret_pos_in_text::]
                    self.caret_pos_in_text-=1
                elif(i==8):
                    pass
                elif(i==13):
                    self.code=self.code[:self.caret_pos_in_text:]+'\n'+self.code[self.caret_pos_in_text::]
                    self.caret_pos_in_text+=1
                elif(i==9):
                    self.code=self.code[:self.caret_pos_in_text:]+'    '+self.code[self.caret_pos_in_text::]
                    self.caret_pos_in_text+=4
                elif(i==256):
                    if(self.caret_pos_in_text<len(self.code)):
                        self.caret_pos_in_text+=1
                elif(i==257):
                    if(self.caret_pos_in_text>0):
                        self.caret_pos_in_text-=1
                elif(i==258):
                    self.vertical_caret_movement('up')
                elif(i==259):
                    self.vertical_caret_movement('down')
                else:
                    q=len(self.code)
                    self.code=self.code[:self.caret_pos_in_text:]+keys[i][2]+self.code[self.caret_pos_in_text::]
                    if(q!=len(self.code)):
                        self.caret_pos_in_text+=1
                if(keys[i][4]==False):
                    keys[i][1]=self.first_time_delay
                    keys[i][4]=True
                else:
                    keys[i][1]=self.time_delay
                keys[i][3]=pygame.time.get_ticks()
            elif(keys[i][0]==True):
                tmp=pygame.time.get_ticks()
                keys[i][1]-=abs(keys[i][3]-tmp)
                keys[i][3]=tmp

        a=self.find_caret_pos(self.caret_pos_in_text-1)
        if(self.caret_pos_in_text<len(self.code) and self.code[self.caret_pos_in_text]!='\n'):
            a[0]-=self.font.render(self.code[self.caret_pos_in_text],True,(0,0,0)).get_width()//2
        self.caret_pos_on_screen=[self.scaret_pos_on_screen[0]+a[0],self.scaret_pos_on_screen[1]+a[1]]

    def draw_text(self,keys,is_finished):
        if(not is_finished):
            self.update_code(keys)
        self.is_in_set=True
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

    def set_lighting(self,s=set(),c=set(),m=set(),v=set()):
        self.special=s.copy()
        self.classes=c.copy()
        self.method=m.copy()
        self.vars=v.copy()
        
    def draw_ed(self,keys,is_finished):
        self.draw_bg()
        self.draw_text(keys,is_finished)

    def find_caret_pos(self,x):
        xi=0
        y=0
        i=x
        while(i>=0 and len(self.code)>0):
            if(self.code[i]=='\n'):
                if(y==0):
                    xi=self.font.render(self.code[i+1:x+1:],True,(0,0,0)).get_width()
                y+=self.font.render('1',True,(0,0,0)).get_height()*(1.3)
            i-=1
        if(y==0):
            xi=self.font.render(self.code[i+1:x+1:],True,(0,0,0)).get_width()
        return [xi,y]

    def vertical_caret_movement(self,s):
        ind=self.caret_pos_in_text
        col=0
        if(s=='up'):
            if(self.caret_pos_in_text==0):
                return
            if(ind>len(self.code)-1):
                ind-=1
            while(ind<len(self.code)-1 and self.code[ind]!='\n'):
                ind+=1
                col+=1
            ind=self.caret_pos_in_text
            if(ind>len(self.code)-1 or self.code[ind]=='\n'):
                ind-=1
            while(ind>0 and self.code[ind]!='\n'):
                ind-=1
            ind1=ind-1
            for i in range(col):
                ind-=1
                if(ind<=0):
                    self.caret_pos_in_text=0
                    return
                elif(self.code[ind]=='\n'):
                    self.caret_pos_in_text=ind1
                    return
            if(col==0):
                self.caret_pos_in_text=ind-1
            else:
                self.caret_pos_in_text=ind
        else:
            if(ind>len(self.code)-1):
                return
            if(self.code[ind]=='\n'):
                ind-=1
            while(ind>0 and self.code[ind]!='\n'):
                ind-=1
                col+=1
            if(self.code[self.caret_pos_in_text]=='\n'):
                col+=1
            ind=self.caret_pos_in_text
            while(ind<len(self.code)-1 and self.code[ind]!='\n'):
                ind+=1
            ind1=ind+1
            for i in range(col):
                ind+=1
                if(ind>=len(self.code)-1):
                    self.caret_pos_in_text=ind-1
                    return
                elif(self.code[ind]=='\n' or ind==len(self.code)-1):
                    self.caret_pos_in_text=ind
                    return
            if(col==0):
                self.caret_pos_in_text=ind+1
            else:
                self.caret_pos_in_text=ind

    def block(self):
        self.is_block=True

    def unblock(self):
        self.is_block=False