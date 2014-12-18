# -*- coding: utf-8 -*-

from UniVars import *
from graphics import *
from Room import *
import random



class Floor(Room):
	def __init__(self, color, rooms):
		self._color = color
		self._num_rooms = rooms
		self._room = {}
		self.buildRooms()

	def clear(self):
		pass

	def getRoomNum(self):
		return self._num_rooms

	def getColor(self):
		return self._color

	def getRoom(self, room_num):
		if room_num in self._room:
			return self._room[room_num]

	def buildRooms(self):
		for i in range(self._num_rooms):
			print i
			self._room[i] = Room(i, self._color)
			print self._room[i]._exits 