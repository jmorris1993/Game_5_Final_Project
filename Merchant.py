# -*- coding: utf-8 -*-
"""
Created on Tue Dec 09 14:56:26 2014

@author: jmorris
"""

from UniVars import *
from Character import *

class Merchant (Character):
    def __init__ (self,name):
        Character.__init__(self,name,"Yours truly",screen)
        log("Player.__init__ for "+str(self))
        #self._sprite = Image(Point(TILE_SIZE/2,TILE_SIZE/2),pic)
        self._origin = self._sprite.getAnchor()
        self._cx = int(self._origin.getX())*2+1
        self._cy = int(self._origin.getY())*2+1
        self._things = things

    def is_merchant (self):
        return True

    def move (self,dx,dy):
        print(self._cx, self._cy)
        tempx = self._cx
        tempy = self._cy
        tempx += dx
        tempy += dy
        print (tempx,tempy)
        print(self._screen.tile(tempx,tempy))
        if self._screen.tile(tempx,tempy) == 1 or self._screen.tile(tempx,tempy) == 0:
            for j in range(len(self._things)):
                self._things[j]._sprite.move(-dx*24,-dy*24)
            for i in range(len(self._screen._things)):
                self._screen._things[i].move(-dx*24,-dy*24)
            self._cx = tempx
            self._cy = tempy
        else:
            print("That's a tree!")