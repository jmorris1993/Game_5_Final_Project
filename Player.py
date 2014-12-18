# -*- coding: utf-8 -*-
"""
Created on Fri Dec 05 14:35:14 2014

@author: jmorris
"""

from UniVars import *
from Character import *
from graphics import *

#
# The Player character
#
class Player (Character):
    def __init__ (self,name,window):
        Character.__init__(self,name,"Yours truly")
        log("Player.__init__ for "+str(self))
        self._sprite = Image(Point(TILE_SIZE/2,TILE_SIZE/2),PLAYER)
        self._window = window
        self._money = 0
        self._attack = 1
        self._defense = 1
        self.current_money=Text(Point(697,12),"Rupees: " + str(self._money))
        self.current_money.draw(self._window)
        self.current_attack=Text(Point(200,12),"Attack: " + str(self._attack))
        self.current_attack.draw(self._window)
        self.current_defense=Text(Point(300,12),"Defense: " + str(self._defense))
        self.current_defense.draw(self._window)
        self._health = 12
        self._maxHealth = self._health
        self.healthStat = Text(Point(80,40),str(self._health)+'/'+str(self._maxHealth))
        self.healthStat.setStyle('bold')
        self.healthStat.draw(window)
        self.health()
        


    def is_player (self):
        return True

    # The move() method of the Player is called when you 
    # press movement keys. 
    # It is different enough from movement by the other
    # characters that you'll probably need to overwrite it.
    # In particular, when the Player move, the screen scrolls,
    # something that does not happen for other characters

    def p_move (self,dx,dy):
        tempx = self._x
        tempy = self._y
        tempx += dx
        tempy += dy
        obj = None
        print(tempx,tempy)
        if self._screen.tile(tempx,tempy) == 1 or self._screen.tile(tempx,tempy) == 0 or self._screen.tile(tempx,tempy) == 4 or self._screen.tile(tempx,tempy) == 5 or self._screen.tile(tempx,tempy) == 6 or self._screen.tile(tempx,tempy) == 7:
            for i in range(len(self._screen._things)):
                if self._screen._things[i]._x == tempx and self._screen._things[i]._y == tempy:
                    if self._screen._things[i].is_scorpion():
                        scorp = self._screen._things[i]
                        self.battle(scorp)
                    if self._screen._things[i].is_money():
                        obj = self._screen._things[i].add_value(self)
                    
                    if self._screen._things[i].is_sword():
                        obj = self._screen._things[i].add_attack(self)
                    if self._screen._things[i].is_armor():
                        obj = self._screen._things[i].add_defense(self)
                    if self._screen._things[i].is_potion():
                        obj = self._screen._things[i].add_value(self)
                        pot = self._screen._things[i]
                        self.heal(pot)
                    
                    
                    if self._screen._things[i].is_open_door():
                        print 'Active'
                        self._screen.clear_scr()
                if self._screen._things[i].is_closed_door():
                    self._screen._things[i].change_door(self._screen,self._window)
                if self._screen._things[i] != self:
                    self._screen._things[i].move(-dx*24,-dy*24)
                    self._x = tempx
                    self._y = tempy
            if obj != None:
                self._screen._things.remove(obj)
        else:
            print("I can't walk on that!")

    def health(self):
        px_per_health = 130/self._maxHealth
        self.healthTile = Rectangle(Point(17,6),Point(17+px_per_health*self._health,25))
        self.healthTile.setFill('red')
        self.healthTile.setOutline('red')
        self.healthTile.draw(self._window)

    def battle(self, enemy):
        self._health = self._health - enemy.attack()
        self.healthTile.undraw()
        self.health()
        self.healthStat.setText(str(self._health)+'/'+str(self._maxHealth))
    
    def heal(self, potion):
        self._health = self._health + potion.get_Value()
        if self._health > 12:
            self._health = 12
        self.healthTile.undraw()
        self.health()
        self.healthStat.setText(str(self._health)+'/'+str(self._maxHealth))
