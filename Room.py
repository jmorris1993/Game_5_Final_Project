# -*- coding: utf-8 -*-

from UniVars import *
from graphics import *
from Level import *
import random

class Room (Level):
	def __init__(self, number, floor):
		self._floor = floor
		self._number = number
		self._lvl = Level()
		self._exits = random.choice([1,2,3,4])
