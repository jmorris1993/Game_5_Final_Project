# -*- coding: utf-8 -*-
"""
Created on Fri Dec 05 14:41:56 2014

@author: jmorris
"""
import random
from UniVars import *

#############################################################
# 
# The description of the world and the screen which displays
# the world
#
# A level contains the background stuff that you can't really
# interact with. The tiles are decorative, and do not come
# with a corresponding object in the world. (Though you can
# change that if you want.)
#
# Right now, a level is described using the following encoding
#
# 0 empty   (light green rectangle)
# 1 grass   (green rectangle)
# 2 tree    (sienna rectangle)
#
# you'll probably want to make nicer sprites at some point.


#
# This implements a random level right now. 
# You'll probably want to replace this with something that 
# implements a specific map -- perhaps of Olin?
#
class Level (object):
    def __init__ (self):
        size = LEVEL_WIDTH * LEVEL_HEIGHT
        map = [0] * size
        for i in range(100):
            map[random.randrange(size)] = 1
        for i in range(50):
            map[random.randrange(size)] = 2
        disp_x = LEVEL_WIDTH - VIEWPORT_WIDTH
        disp_y = LEVEL_HEIGHT - VIEWPORT_HEIGHT
        for i in range(VIEWPORT_HEIGHT):
            print i
            if i == 0 or i == VIEWPORT_HEIGHT-1:
                for j in range(VIEWPORT_WIDTH):
                    map[i * LEVEL_WIDTH + disp_x / 2 + 1 + j + (disp_y + 1) / 2 * LEVEL_HEIGHT] = 3
            else:
                map[i * LEVEL_WIDTH + disp_x / 2 + 1 + (disp_y + 1) / 2 * LEVEL_HEIGHT] = 3
                map[i * LEVEL_WIDTH + VIEWPORT_WIDTH + disp_x / 2 + (disp_y + 1) / 2 * LEVEL_HEIGHT] = 3
        self._map = map

    def _pos (self,x,y):
        return x + (y*LEVEL_WIDTH);

    # return the tile at a given tile position in the level
    def tile (self,x,y):
        return self._map[self._pos(x,y)]