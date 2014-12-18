# -*- coding: utf-8 -*-
"""
Created on Fri Dec 05 14:46:08 2014

@author: jmorris
"""

from UniVars import *
from Thing import *

class Items (Thing):
    def __init__ (self,name,desc):
        Thing.__init__(self,name,desc)
        log("Character.__init__ for "+str(self))
    # A character has a move() method that you should implement
    # to enable movement

    def is_item (self):
        return True

    def is_walkable (self):
        return True
    
