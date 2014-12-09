# -*- coding: utf-8 -*-
"""
Created on Fri Dec 05 14:48:02 2014

@author: jmorris
"""

from Items import *

class Potion (Items):
    def __init__ (self,name,desc):
        Items.__init__(self,name,desc)
        log("Character.__init__ for "+str(self))
        pic = 'potion.gif'
        self._sprite = Image(Point(TILE_SIZE/2,TILE_SIZE/2),pic)
        self._window = window
        self._origin = self._sprite.getAnchor()
        self._cx = int(self._origin.getX())*2+1
        self._cy = int(self._origin.getY())*2+1
        print self._cx
        print self._cy
        self._things = things

    # A character has a move() method that you should implement
    # to enable movement
 

    def is_potion (self):
        return True

    def is_walkable (self):
        return True