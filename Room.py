# -*- coding: utf-8 -*-

from UniVars import *
from graphics import *
from Level import *
import random

class Room (Level):
	def __init__(self, number, color):
		self._color = color
		self._number = number
		self._exits = random.sample(xrange(1,4), random.randrange(1,4))
		self.create()

	def create(self):
		self._lvl = Level(self._exits,self._color)

	def getLvl(self):
		return self._lvl

	def clear(self):
		pass