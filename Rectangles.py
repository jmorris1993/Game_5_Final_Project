# -*- coding: utf-8 -*-


from UniVars import *
from graphics import *

class Rectangles (Rectangle):
    def __init__(self, p1, p2, piece,x,y):
        Rectangle.__init__(self,p1,p2)
        self._walkable = piece
        self._x = x
        self._y = y
        self._p1 = p1
        self._p2 = p2

        
    def get_x(self):
        pt = self.getCenter()
        return pt.getX()

    def get_y(self):
        pt = self.getCenter()
        return pt.getY()

    # is this object a Thing?
    def is_thing (self):
        return False

    def is_open_door(self):
        return False

    def is_closed_door(self):
        return False
    # is this object a Character?
    def is_character (self):
        return False

    # is this object the Player?
    def is_player (self):
        return False

    # can this object be walked over during movement?
    def is_walkable (self):
        print self._walkable
        if self._walkable == 1 or self._walkable == 0 or self._walkable == 5:
            return True
        else:
            return False
    
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
    def __init__(self, p, x, y, piece, *pixmap):
        Image.__init__(self, p, *pixmap)
        self._walkable = piece
        self._x = x
        self._y = y
        self._p = p

    def change_door(self,screen,window):
        self._walkable = 5
        print (self._x,self._y)
        door = Images(self._p, self._x, self._y, self._walkable, DOOR_OPEN)
        screen._things.append(door)
        screen._things.remove(self)
        self.undraw()
        door.draw(window)

    # is this object a Thing?
    def is_thing (self):
        return False

    # is this object a Character?
    def is_character (self):
        return False

    # is this object the Player?
    def is_player (self):
        return False

    def is_open_door(self):
        if self._walkable == 5:
            return True
        else:
            return False

    def is_closed_door(self):
        if self._walkable == 4:
            return True
        else:
            return False

    # can this object be walked over during movement?
    def is_walkable (self):
        if self._walkable == 1 or self._walkable == 5:
            return True
        else:
            return False
    
    def is_merchant (self):
        return False
    
    def is_rat (self):
        return False
    
    def is_boss (self):
        return False

    def is_door(self):
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