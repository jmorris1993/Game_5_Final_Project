# -*- coding: utf-8 -*-
"""
Created on Fri Dec 05 14:35:14 2014

@author: jmorris
"""

from Character import *

#
# The Player character
#
class Player (Character):
    def __init__ (self,name,window,screen,cx,cy,things):
        Character.__init__(self,name,"Yours truly",screen)
        log("Player.__init__ for "+str(self))
        pic = 't_android_red.gif'
        self._sprite = Image(Point(TILE_SIZE/2,TILE_SIZE/2),pic)
        self._window = window
        self._origin = self._sprite.getAnchor()
        self._cx = int(self._origin.getX())*2+1
        self._cy = int(self._origin.getY())*2+1
        print self._cx
        print self._cy
        self._things = things

    def is_player (self):
        return True

    # The move() method of the Player is called when you 
    # press movement keys. 
    # It is different enough from movement by the other
    # characters that you'll probably need to overwrite it.
    # In particular, when the Player move, the screen scrolls,
    # something that does not happen for other characters

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