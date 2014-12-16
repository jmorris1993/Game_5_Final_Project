# -*- coding: utf-8 -*-
"""
Created on Fri Dec 05 14:33:20 2014

@author: jmorris
"""

from UniVars import *
from Items import *

class OlinStatue (Items):
    def __init__ (self):
        Items.__init__(self,"Olin statue","A statue of F. W. Olin")
        self._sprite = Image(Point(TILE_SIZE/2,TILE_SIZE/2),STATUE)
    
    def is_OlinStatue (self):
        return True