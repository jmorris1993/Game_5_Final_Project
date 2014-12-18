# -*- coding: utf-8 -*-
"""
Created on Fri Dec 05 14:52:21 2014

@author: jmorris
"""

from UniVars import *
from Equipment import *

class Sword (Equipment):
    def __init__ (self,name,desc,attack):
        Equipment.__init__(self,name,desc)
        log("Character.__init__ for "+str(self))
        self._sprite = Image(Point(TILE_SIZE/2,TILE_SIZE/2),SWORD)
        self._attack = attack

    # A character has a move() method that you should implement
    # to enable movement

    def is_sword (self):
        return True

    def is_walkable (self):
        return True
    
    def get_attack (self):
        return self._attack
    
    def add_attack (self, player):
        player._attack += self.get_attack()
        player.current_attack.setText("Attack: " + str(player._attack))
        self._sprite.undraw()