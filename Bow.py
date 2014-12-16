# -*- coding: utf-8 -*-
"""
Created on Fri Dec 05 15:07:12 2014

@author: jmorris
"""

from UniVars import *

class Bow (Equipment):
    def __init__ (self,name,desc,attack,attackRange):
        Equipment.__init__(self,name,desc)
        log("Character.__init__ for "+str(self))
        #self._sprite = Image(Point(TILE_SIZE/2,TILE_SIZE/2),pic)
        self._attack = attack
        self._attackRange = attackRange


    # A character has a move() method that you should implement
    # to enable movement  

    def is_Bow (self):
        return True

    def is_walkable (self):
        return True
    
    def getAttack (self):
        return self._attack
    
    def getAttackRange (self):
        return self._attackRange