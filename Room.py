# -*- coding: utf-8 -*-

from UniVars import *
from graphics import *
from Level import *
import random

class Room (Level):
	def __init__(self, number, floor):
		self._floor = floor
		self._color = floor._color
		self._number = number
		self._exits = random.sample(xrange(1,4), random.randrange(1,4))
		print self._exits
		self.create(self._exits)

	def create(self, exits):
		self._lvl = Level(exits,self._color)

	def clear(self):
		pass