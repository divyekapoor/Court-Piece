#!/usr/bin/env python

class Game(object):
	
	def __init__(self):
		pass
		
	def play(self):
		pass
		

class Player(object):
	
	def __init__(self, name, cards):
		self.name = name
		self.cards = cards
	
	def __unicode__(self):
		return self.name
		
	def __str__(self):
		return self.name
		
	def __repr__(self):
		return 'Player(' + repr(self.name) + ', ' + repr(self.cards) + ')'
	
	@property
	def name(self):
		return self._name
		
	@name.setter
	def name(self, value):
		if isinstance(value, basestring):
			self._name = value
		else:
			raise ValueError("%r is not a suitable ")
			
	@name.deleter
	def name(self):
		del self._name
		

class CourtPiece(object):
	
	def __init__(self):
