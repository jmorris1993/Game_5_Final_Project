# -*- coding: utf-8 -*-

from UniVars import *
from graphics import *
from Room import *
import random



class Floor(Room):
	def __init__(self, color):
		self._color = color


	def clear(self):
		pass
