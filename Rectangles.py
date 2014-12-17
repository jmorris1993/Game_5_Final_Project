# -*- coding: utf-8 -*-


from UniVars import *
from graphics import *

class Rectangles (Rectangle):
    def __init__(self, p1, p2, piece,x,y):
        Rectangle.__init__(self,p1,p2)
        self._walkable = piece
        self._x = x
        self._y = y
        print(x,y)
        
    def get_x(self):
        pt = self.getCenter()
        return pt.getX()

    def get_y(self):
        pt = self.getCenter()
        return pt.getY()

    def change_door(self,screen):
        pass

    # is this object a Thing?
    def is_thing (self):
        return False

    # is this object a Character?
    def is_character (self):
        return False

    # is this object the Player?
    def is_player (self):
        return False

    # can this object be walked over during movement?
    def is_walkable (self):
        return True
    
    def is_merchant (self):
        return False
    
    def is_rat (self):
        return False
    
    def is_boss (self):
        return False
    
    def is_items (self):
        return False
    
    def is_potion (self):
        return False
    
    def is_money (self):
        return False

    def is_scorpion(self):
        return False
    
    def is_equipment (self):
        return False
    
    def is_sword (self):
        return False
    
    def is_bow (self):
        return False
    
    def is_armor (self):
        return False
    
    def is_OlinStatue (self):
        return False

class Images(Image):
    def __init__(self, p, x, y, *pixmap):
        Image.__init__(self, p, *pixmap)
        self._x = x
        self._y = y

    # is this object a Thing?
    def is_thing (self):
        return False

    # is this object a Character?
    def is_character (self):
        return False

    # is this object the Player?
    def is_player (self):
        return False

    # can this object be walked over during movement?
    def is_walkable (self):
        return True
    
    def is_merchant (self):
        return False
    
    def is_rat (self):
        return False
    
    def is_boss (self):
        return False
    
    def is_items (self):
        return False
    
    def is_potion (self):
        return False
    
    def is_money (self):
        return False

    def is_scorpion(self):
        return False
    
    def is_equipment (self):
        return False
    
    def is_sword (self):
        return False
    
    def is_bow (self):
        return False
    
    def is_armor (self):
        return False
    
    def is_OlinStatue (self):
        return False