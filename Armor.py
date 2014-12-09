# -*- coding: utf-8 -*-
"""
Created on Fri Dec 05 15:07:55 2014

@author: jmorris
"""

class Armor (Equipment):
    def __init__ (self,name,desc,defense):
        Equipment.__init__(self,name,desc)
        log("Character.__init__ for "+str(self))
        pic = 'money.gif'
        self._sprite = Image(Point(TILE_SIZE/2,TILE_SIZE/2),pic)
        self._origin = self._sprite.getAnchor()
        self._cx = int(self._origin.getX())*2+1
        self._cy = int(self._origin.getY())*2+1
        self._defense = defense

    # A character has a move() method that you should implement
    # to enable movement

    def is_Armor (self):
        return True

    def is_walkable (self):
        return True
    
    def get_defense (self):
        return self._defense