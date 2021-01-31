import pygame
from button import button
from message_box import message_box
import random


class math_game:
    def __init__(self, screen, path):
        self.screen = screen
        self.bg = pygame.image.load(path)
        self.bg = pygame.transform.scale(self.bg, (self.screen.get_width(), self.screen.get_height()))
        self.return_but = button("res/button_blue.png")
        self.return_but.add_button((49, 48), (339, 95, 388, 143), '', (255, 255, 255))
        self.return_but.add_button((49, 45), (290, 95, 340, 140), '', (255, 255, 255))
        self.return_but.set_picture('res/icons.png', (4 * 51 - 5, 51 + 5, 5 * 51 - 5, 2 * 51 + 5), (40, 40))
        self.return_but.draw_button(self.screen, 0, (self.screen.get_width() - 100, self.screen.get_height() - 100))
        self.ans_1_but = button("res/button_blue.png")
        self.ans_2_but = button("res/button_blue.png")
        self.ans_3_but = button("res/button_blue.png")
        self.ans_4_but = button("res/button_blue.png")
        self.ans_1_but.add_button((190, 49), (0, 0, 190, 49), '', (255, 255, 255))
        self.ans_1_but.add_button((190, 45), (0, 50, 190, 95), '', (255, 255, 255))
        self.ans_2_but.add_button((190, 49), (0, 0, 190, 49), '', (255, 255, 255))
        self.ans_2_but.add_button((190, 45), (0, 50, 190, 95), '', (255, 255, 255))
        self.ans_3_but.add_button((190, 49), (0, 0, 190, 49), '', (255, 255, 255))
        self.ans_3_but.add_button((190, 45), (0, 50, 190, 95), '', (255, 255, 255))
        self.ans_4_but.add_button((190, 49), (0, 0, 190, 49), '', (255, 255, 255))
        self.ans_4_but.add_button((190, 45), (0, 50, 190, 95), '', (255, 255, 255))
        x = self.screen.get_width() // 2
        y = self.screen.get_height() // 2 + 180
        self.ans_1_but.draw_button(self.screen, 0, (x - 100, y - 30))
        self.ans_2_but.draw_button(self.screen, 0, (x + 100, y - 30))
        self.ans_3_but.draw_button(self.screen, 0, (x - 100, y + 30))
        self.ans_4_but.draw_button(self.screen, 0, (x + 100, y + 30))
        self.cur_exp = ""
        self.cur_diff = 0
        self.cur_score = -1
        self.cur_time = 10
        self.del_time = self.cur_time
        self.cur_ticks = pygame.time.get_ticks()
        self.cur_right = -1
        self.variants = []
        self.but = 0
        self.is_right = False
        self.fin_scr = message_box(self.screen)
        self.is_over = False
        self.is_first = True
        self.is_f_f = True
        self.out = -1
        self.new_level(True)

    def draw_bg(self):
        self.screen.blit(self.bg, (0, 0))

    def draw_bg_for_exp(self, size1):
        size = (16, 16)
        self.path = 'res/UI_1.png'
        self.surf = pygame.Surface((size1[0] * size[0], size1[1] * size[1])).convert()
        self.surf.set_colorkey((255, 255, 255))
        sheet = pygame.image.load(self.path).convert()
        mid = pygame.Surface(size).convert()
        ri = pygame.Surface(size).convert()
        le = pygame.Surface(size).convert()
        up = pygame.Surface(size).convert()
        down = pygame.Surface(size).convert()
        luc = pygame.Surface(size).convert()
        ruc = pygame.Surface(size).convert()
        rdc = pygame.Surface(size).convert()
        ldc = pygame.Surface(size).convert()
        ldc.set_colorkey((0, 0, 0))
        mid.blit(sheet, (0, 0), (252, 378, 268, 394))
        ri.blit(sheet, (0, 0), (270, 378, 286, 394))
        le.blit(sheet, (0, 0), (234, 378, 250, 394))
        up.blit(sheet, (0, 0), (252, 360, 268, 376))
        down.blit(sheet, (0, 0), (252, 396, 268, 412))
        luc.blit(sheet, (0, 0), (288, 360, 304, 376))
        ruc.blit(sheet, (0, 0), (306, 360, 322, 376))
        rdc.blit(sheet, (0, 0), (306, 378, 322, 394))
        ldc.blit(sheet, (0, 0), (288, 378, 304, 394))
        for y in range(size1[1]):
            for x in range(size1[0]):
                if (x == 0 and y == 0):
                    self.surf.blit(luc, (0, 0))
                elif (x == size1[0] - 1 and y == size1[1] - 1):
                    self.surf.blit(rdc, (x * size[0], y * size[1]))
                elif (x == 0 and y == size1[1] - 1):
                    self.surf.blit(ldc, (x * size[0], y * size[1]))
                elif (x == size1[0] - 1 and y == 0):
                    self.surf.blit(ruc, (x * size[0], y * size[1]))
                elif (x == 0):
                    self.surf.blit(le, (x * size[0], y * size[1]))
                elif (y == 0):
                    self.surf.blit(up, (x * size[0], y * size[1]))
                elif (x == size1[0] - 1):
                    self.surf.blit(ri, (x * size[0], y * size[1]))
                elif (y == size1[1] - 1):
                    self.surf.blit(down, (x * size[0], y * size[1]))
                else:
                    self.surf.blit(mid, (x * size[0], y * size[1]))

    def draw_buttons(self, is_clicked, pos):
        out = 0
        if (is_clicked and self.ans_1_but.check_pos_in_button(pos)):
            self.ans_1_but.draw_button(self.screen, 1, self.ans_1_but.pos)
            out = 1
        else:
            self.ans_1_but.draw_button(self.screen, 0, self.ans_1_but.pos)
        if (is_clicked and self.ans_2_but.check_pos_in_button(pos)):
            self.ans_2_but.draw_button(self.screen, 1, self.ans_2_but.pos)
            out = 2
        else:
            self.ans_2_but.draw_button(self.screen, 0, self.ans_2_but.pos)
        if (is_clicked and self.ans_3_but.check_pos_in_button(pos)):
            self.ans_3_but.draw_button(self.screen, 1, self.ans_3_but.pos)
            out = 3
        else:
            self.ans_3_but.draw_button(self.screen, 0, self.ans_3_but.pos)
        if (is_clicked and self.ans_4_but.check_pos_in_button(pos)):
            self.ans_4_but.draw_button(self.screen, 1, self.ans_4_but.pos)
            out = 4
        else:
            self.ans_4_but.draw_button(self.screen, 0, self.ans_4_but.pos)
        return out

    def generate_exp(self, diff):
        out = ""
        operat = ['+', '-', '*', '/']
        a = random.random() * (11 + 10 * diff) + 1
        b = random.random() * (11 + 10 * diff) + 1
        a = round(a, diff)
        b = round(b, diff)
        if (float(int(a)) == a):
            a = int(a)
        if (float(int(b)) == b):
            b = int(b)
        op = operat[random.randint(0, 3)]
        out = str(a) + op + str(b)
        for i in range(diff):
            op = operat[random.randint(0, 3)]
            c = random.random() * (11 + 10 * diff) + 1
            c = round(c, diff)
            if (float(int(c)) == c):
                c = int(c)
            out += op + str(c)
        return out

    def new_level(self, is_right):
        if (is_right and self.cur_score % 5 == 0 and self.cur_score != 0):
            self.cur_diff += 1
            self.cur_time += 5
        if (is_right and not self.is_over):
            self.del_time = self.cur_time
            self.cur_score += 1
            self.cur_exp = self.generate_exp(self.cur_diff)
            ans = ['r', '1', '2', '3']
            self.variants.clear()
            for i in range(4):
                tmp = random.randint(0, len(ans) - 1)
                if (ans[tmp] == 'r'):
                    self.cur_right = i + 1
                    x = eval(self.cur_exp)
                    x = round(x, 3)
                    if (float(int(x)) == x):
                        x = int(x)
                    self.variants.append(x)
                elif (ans[tmp] == '1'):
                    x = eval(self.cur_exp)
                    x += 1.5
                    x = round(x, 3)
                    if (float(int(x)) == x):
                        x = int(x)
                    self.variants.append(x)
                elif (ans[tmp] == '2'):
                    x = eval(self.cur_exp)
                    x -= 0.5
                    x = round(x, 3)
                    if (float(int(x)) == x):
                        x = int(x)
                    self.variants.append(x)
                else:
                    x = eval(self.cur_exp)
                    x -= 1.5
                    x = round(x, 3)
                    if (float(int(x)) == x):
                        x = int(x)
                    self.variants.append(x)
                ans.pop(tmp)
        f = pygame.font.SysFont('Corbel', 20)
        t = f.render(self.cur_exp, True, (255, 255, 255))
        self.screen.blit(t, (
        self.screen.get_width() // 2 - t.get_width() // 2, self.screen.get_height() // 2 - t.get_height() // 2 - 100))
        self.ans_1_but.set_text(str(self.variants[0]), (255, 255, 255))
        self.ans_2_but.set_text(str(self.variants[1]), (255, 255, 255))
        self.ans_3_but.set_text(str(self.variants[2]), (255, 255, 255))
        self.ans_4_but.set_text(str(self.variants[3]), (255, 255, 255))
        f = pygame.font.SysFont('Corbel', 70)
        s = f.render(str(self.cur_score), True, (100, 255, 100))
        self.screen.blit(s, (self.screen.get_width() - 100, 20))
        if (not self.is_over):
            q = pygame.time.get_ticks()
            self.del_time -= ((q - self.cur_ticks) / 1000)
            self.cur_ticks = q
            if (self.del_time <= 0):
                self.is_over = True
        s = f.render(str(int(self.del_time)), True, (100, 255, 100))
        self.screen.blit(s, (self.screen.get_width() // 2, 20))

    def to_start(self):
        self.cur_exp = ""
        self.cur_diff = 0
        self.cur_score = -1
        self.cur_time = 10
        self.del_time = self.cur_time
        self.cur_ticks = pygame.time.get_ticks()
        self.cur_right = -1
        self.variants = []
        self.but = 0
        self.is_right = False
        self.is_over = False
        self.is_first = False
        self.is_f_f = True
        self.new_level(True)
        self.out = -1

    def update(self, is_clicked, pos):
        if (self.is_first):
            self.to_start()
        self.draw_bg()
        self.draw_bg_for_exp((50, 20))
        self.screen.blit(self.surf, (self.screen.get_width() // 2 - self.surf.get_width() // 2,
                                     self.screen.get_height() // 2 - self.surf.get_height() // 2 - 100))
        self.new_level(self.is_right)
        self.is_right = False
        if (is_clicked and self.return_but.check_pos_in_button(pos) and not self.is_over):
            self.return_but.draw_button(self.screen, 1, self.return_but.pos)
            self.is_first=True
            return 0
        else:
            self.return_but.draw_button(self.screen, 0, self.return_but.pos)
        if (self.but == self.cur_right and is_clicked == False):
            self.is_right = True
            self.but = 0
        elif (self.but != 0 and self.but != self.cur_right and is_clicked == False):
            self.is_over = True
        self.but = self.draw_buttons(is_clicked, pos)
        if (self.is_over):
            if (self.out != 0):
                self.out = self.fin_scr.draw_fin(self.is_f_f, is_clicked, pos, self.cur_score)
            else:
                self.fin_scr.draw_fin(self.is_f_f, is_clicked, pos, self.cur_score)
            self.is_f_f = False
            if (self.out == 0 and not is_clicked):
                self.is_first = True
                return self.out
        return 2
