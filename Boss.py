# -*- coding: utf-8 -*-
"""
Created on Tue Dec 09 14:58:27 2014

@author: jmorris
"""

from UniVars import *
from Character import *

class Boss (Character):
    def __init__ (self,name,window,screen,cx,cy,things):
        Character.__init__(self,name,"Yours truly",screen)
        log("Player.__init__ for "+str(self))
        pic = 't_android_red.gif'
        self._sprite = Image(Point(TILE_SIZE/2,TILE_SIZE/2),GAURD)
        self._window = window
        self._things = things

    def is_Boss (self):
        return True
    
    def attack (self):
        pass
    
    def super_attack (self):
        pass