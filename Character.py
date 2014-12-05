# -*- coding: utf-8 -*-
"""
Created on Fri Dec 05 14:29:54 2014

@author: jmorris
"""

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

    def move (self,dx,dy):
        self._sprite.move(dx,dy)   

    def is_character (self):
        return True

    def is_walkable (self):
        return False