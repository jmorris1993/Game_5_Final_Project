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
        self._health = 5

    def is_boss (self):
        return True
    
    def attack (self,q):
        self._attack = random.randrange(4)
        if self._attack == 0:
            #Do an attack
        
        self.register(q,self._freq)
    
    def super_attack (self,q):
        self._superAttack = random.randrange(10)
        if self._superAttack == 0:
            #Do a super attack
        
        self.register(q,self._freq)
        
    
    def event (self,q):
        self._direction = random.randrange(4)
        if self._direction == 0:
            self.c_move(1,0)
        elif self._direction == 1:
            self.c_move(-1,0)
        elif self._direction == 2:
            self.c_move(0,1)
        elif self._direction == 3:
            self.c_move(0,-1)
        self.register(q,self._freq)
    
    def die(self):
        self._sprite.undraw()
        self._x = None
        self._y = None
        
        
        
        
        
        
        