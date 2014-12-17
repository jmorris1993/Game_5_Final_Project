# -*- coding: utf-8 -*-
"""
Created on Fri Dec 05 14:29:54 2014

@author: jmorris
"""

from UniVars import *
from Thing import *

#
# Characters represent persons and animals and things that move
# about possibly proactively
#
class Character (Thing):
    def __init__ (self,name,desc):
        Thing.__init__(self,name,desc)
        log("Character.__init__ for "+str(self))
        rect = Rectangle(Point(1,1),
                         Point(TILE_SIZE-1,TILE_SIZE-1))
        rect.setFill("red")
        rect.setOutline("red")
        self._sprite = rect


    # A character has a move() method that you should implement
    # to enable movement

    def c_move (self,dx,dy):
        tempx = self._x
        tempy = self._y
        tempx += dx
        tempy += dy
        if self._screen.tile(tempx,tempy) == 1 or self._screen.tile(tempx,tempy) == 0:
            self._sprite.move(dx*24,dy*24)
            self._x = tempx
            self._y = tempy 
        if self._screen.tile(tempx,tempy) == 'null':
            print 'Can\'t move here'

    def is_character (self):
        return True

    def is_walkable (self):
        return False