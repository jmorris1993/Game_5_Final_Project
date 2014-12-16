# -*- coding: utf-8 -*-
"""
Created on Fri Dec 05 14:49:55 2014

@author: jmorris
"""

from UniVars import *
from Items import *

class Money (Items):
    def __init__ (self,name,desc,value):
        Items.__init__(self,name,desc)
        log("Character.__init__ for "+str(self))
        if value == 1:
            self._sprite = Image(Point(TILE_SIZE/2,TILE_SIZE/2),MONEY)
        elif value == 5:
            self._sprite = Image(Point(TILE_SIZE/2,TILE_SIZE/2),MONEY5)
        elif value == 50:
            self._sprite = Image(Point(TILE_SIZE/2,TILE_SIZE/2),MONEY50)
        self._value = value

    # A character has a move() method that you should implement
    # to enable movement

    def is_money (self):
        return True

    def is_walkable (self):
        return True
    
    def get_value (self):
        return self._value

    def add_value (self, player):
        player._money += self.get_value()
        if player._money > 9999:
            player._money = 9999
            warning = Text(Point(697,36),"MAX!")
            warning.setStyle('bold')
            rect2 = Rectangle(Point(670,24),Point(720,48))
            rect2.setFill("white")
            rect2.setOutline("white")
            rect2.draw(player._window)
            warning.setTextColor('red2')
            warning.draw(player._window)
        self._sprite.undraw()
        player.current_money.setText("Rupees: " + str(player._money))