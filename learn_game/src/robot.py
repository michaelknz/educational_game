import pygame
import player

class robot(player.player):
    def move_right(self):
        self.movings.append(['r',self.del_col])
    def move_down(self):
        self.movings.append(['d',self.del_col])
    def move_left(self):
        self.movings.append(['l',self.del_col])
    def move_up(self):
        self.movings.append(['u',self.del_col])
