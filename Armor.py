# -*- coding: utf-8 -*-
"""
Created on Fri Dec 05 15:07:55 2014

@author: jmorris
"""

class Armor (Equipment):
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
        # WRITE ME!
        pass   

    def is_character (self):
        return True

    def is_walkable (self):
        return False