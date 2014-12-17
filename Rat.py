# -*- coding: utf-8 -*-
"""
Created on Fri Dec 05 14:33:46 2014

@author: jmorris
"""
 
from UniVars import *
from Character import *
import random

# 
# A Rat is an example of a character which defines an event that makes
# the rat move, so that it can be queued into the event queue to enable
# that behavior. (Which is right now unfortunately not implemented.)
#
class Rat (Character):
    def __init__ (self,name,desc,screen):
        Character.__init__(self,name,desc,screen)
        log("Rat.__init__ for "+str(self))
        self._sprite = Image(Point(TILE_SIZE/2,TILE_SIZE/2),KITTY)
        self._direction = random.randrange(4)
        self._attack = 0

    # A helper method to register the Rat with the event queue
    # Call this method with a queue and a time delay before
    # the event is called
    # Note that the method returns the object itself, so we can
    # use method chaining, which is cool (though not as cool as
    # bowties...)

    def register (self,q,freq):
        self._freq = freq
        q.enqueue(freq,self)
        return self

    def is_scorpion(self):
        return True

    def attack(self):
        self._attack = random.randrange(4)
        return self._attack

    # this gets called from event queue when the time is right

    def event (self,q):
        self._direction = random.randrange(4)
        if self._direction == 0:
            self.move(1,0)
        elif self._direction == 1:
            self.move(-1,0)
        elif self._direction == 2:
            self.move(0,1)
        elif self._direction == 3:
            self.move(0,-1)
        self.register(q,self._freq)
        #log("event for "+str(self))
        
        