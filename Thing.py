# -*- coding: utf-8 -*-
"""
Created on Fri Dec 05 14:26:18 2014

@author: jmorris
"""

from UniVars import *
from graphics import *
import time

def log (message):
    print time.strftime("[%H:%M:%S]",time.localtime()),message

#
# The root object
#
class Root (object):
    # default predicates

    # is this object a Thing?
    def is_thing (self):
        return False

    # is this object a Character?
    def is_character (self):
        return False

    # is this object the Player?
    def is_player (self):
        return False

    # can this object be walked over during movement?
    def is_walkable (self):
        return False

    def is_open_door(self):
        return False

    def is_closed_door(self):
        return False
    
    def is_merchant (self):
        return False
    
    def is_rat (self):
        return False
    
    def is_boss (self):
        return False
    
    def is_items (self):
        return False
    
    def is_potion (self):
        return False
    
    def is_money (self):
        return False

    def is_scorpion(self):
        return False
    
    def is_equipment (self):
        return False
    
    def is_sword (self):
        return False
    
    def is_bow (self):
        return False
    
    def is_armor (self):
        return False
    
    def is_OlinStatue (self):
        return False

# A thing is something that can be interacted with and by default
# is not moveable or walkable over
#
#   Thing(name,description)
#
# A thing defines a default sprite in field _sprite
# To create a new kind of thing, subclass Thing and 
# assign it a specific sprite (see the OlinStatue below).
# 
class Thing (Root):
    def __init__ (self,name,desc):
        self._name = name
        self._description = desc
        self._sprite = Text(Point(TILE_SIZE/2,TILE_SIZE/2),"?")
        log("Thing.__init__ for "+str(self))

    def __str__ (self):
        return "<"+self.name()+">"

    # return the sprite for display purposes
    def sprite (self):
        return self._sprite

    # return the name
    def name (self):
        return self._name

    # return the position of the thing in the level array
    def position (self):
        return (self._x,self._y)
        
    # return the description
    def description (self):
        return self._description

    # creating a thing does not put it in play -- you have to 
    # call materialize, passing in the screen and the position
    # where you want it to appear
    def materialize (self,screen,x,y):
        screen.add(self,x,y)
        self._screen = screen
        self._x = x
        self._y = y
        self._screen._things.append(self)
        return self

    def is_thing (self):
        return True

    def is_walkable (self):
        return False

    def move (self,dx,dy):
        self._sprite.move(dx,dy)

    def get_x(self):
        return self._x

    def get_y(self):
        return self._y


