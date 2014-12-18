# -*- coding: utf-8 -*-

from UniVars import *
from graphics import *
from Level import *
from Money import *
from Sword import *
from Scorpion import *
from Potion import *
import random

class Room (Level):
	def __init__(self, number, color,q):
		self._color = color
		self._number = number
		self._exits = random.sample(xrange(1,4), random.randrange(1,4))
		self.create()
		self._q = q

	def create(self):
		self._lvl = Level(self._exits,self._color)

	def getLvl(self):
		return self._lvl

	def buildObj(self,scr):
		for i in range(random.randrange(1,10)):
			Money("Money","Can be used to buy things from merchant.",random.choice([5,10,50])).materialize(scr,random.randint(
            	LEVEL_WIDTH/2-VIEWPORT_WIDTH/2+1,LEVEL_WIDTH/2+VIEWPORT_WIDTH/2-1),random.randint(LEVEL_HEIGHT/2-VIEWPORT_HEIGHT/2+3,LEVEL_HEIGHT/2+VIEWPORT_HEIGHT/2)-1)
		for i in range(random.randrange(1,3)):
			Potion("Potion", "Can be used to heal Player.",10).materialize(scr,random.randint(
				LEVEL_WIDTH/2-VIEWPORT_WIDTH/2+1,LEVEL_WIDTH/2+VIEWPORT_WIDTH/2-1),random.randint(LEVEL_HEIGHT/2-VIEWPORT_HEIGHT/2+3,LEVEL_HEIGHT/2+VIEWPORT_HEIGHT/2)-1)
		for i in range(random.randrange(1,3)):
			Scorpion("Pinky","A Scorpion").register(self._q,40).materialize(scr,30,30)
		Sword("Wooden Sword", "Weakest Sword in the game", 10).materialize(scr,35,37)