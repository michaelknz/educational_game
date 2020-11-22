import pygame

class button(object):
    def __init__(self,image_path):
        self.images=[]
        self.png=pygame.image.load(image_path)
        self.font = pygame.font.SysFont('Corbel',25)
        self.texts=[]

    def image_at(self,image_size,image_pos,colorkey=None):
        rect = pygame.Rect(image_pos)
        image = pygame.Surface(image_size).convert()
        image.blit(self.png, (0, 0), rect)
        if colorkey is not None:
            if colorkey == -1:
                colorkey = image.get_at((0,0))
            image.set_colorkey(colorkey, pygame.RLEACCEL)

        return image

    def draw_button(self,screen,i,pos):
        screen.blit(self.images[i],(pos[0]-self.images[i].get_width()//2,pos[1]-self.images[i].get_height()//2))
        t=self.font.render(self.texts[i],True,(50,50,50))
        screen.blit(t,(pos[0]-t.get_width()//2,pos[1]-t.get_height()//2))

    def add_button(self,image_size,image_pos,text):
        self.images.append(self.image_at(image_size,image_pos,(0,0,0)))
        self.texts.append(text)
