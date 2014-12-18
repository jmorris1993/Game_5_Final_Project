# -*- coding: utf-8 -*-
"""
Created on Tue Dec 09 14:58:27 2014

@author: jmorris
"""

from UniVars import *
from Character import *
import random

class Boss (Character):
    def __init__ (self,name,desc):
        Character.__init__(self,name,desc)
        log("Boss.__init__ for "+str(self))
        pic = 't_android_red.gif'
        self._sprite = Image(Point(TILE_SIZE/2,TILE_SIZE/2),GAURD)
        self._direction = random.randrange(4)
        self._health = 1000
        self._attack = 5

    def is_boss (self):
        return True
    
    def register (self,q,freq):
        self._freq = freq
        q.enqueue(freq,self)
        return self
    
    def attack (self):
        self._attack = random.randrange(5)
        if self._attack < 2:
            self._attack = 8
        return self._attack

    
    def super_attack (self):
        self._superAttack = random.randrange(10)
        
        self.register(q,self._freq)
        
    
    def event (self,q):
        self._direction = random.randrange(4)
        if self._direction == 0:
            self.c_move(2,0)
        elif self._direction == 1:
            self.c_move(-2,0)
        elif self._direction == 2:
            self.c_move(0,2)
        elif self._direction == 3:
            self.c_move(0,-2)
        self.register(q,self._freq)
    
    def die(self):
        self._sprite.undraw()
        self._x = None
        self._y = None
        
        
        
        
        
        
        