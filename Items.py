# -*- coding: utf-8 -*-
"""
Created on Fri Dec 05 14:46:08 2014

@author: jmorris
"""

from Thing import *

class Items (Thing):
    def __init__ (self,name,desc):
        Thing.__init__(self,name,desc)
        log("Character.__init__ for "+str(self))
        pic = 'money.gif'
        self._sprite = Image(Point(TILE_SIZE/2,TILE_SIZE/2),pic)
        self._origin = self._sprite.getAnchor()
        self._cx = int(self._origin.getX())*2+1
        self._cy = int(self._origin.getY())*2+1

    # A character has a move() method that you should implement
    # to enable movement

    def is_Item (self):
        return True

    def is_walkable (self):
        return True
    
