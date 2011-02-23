#!/usr/bin/env python

from card import Card

def print_deck():
	print "A deck of cards: "
	for suit in Card.suits:
		print suit + ": ",
		for value in range(1,13):
			print unicode(Card(value, suit)),
		print
		
if __name__ == "__main__":
	print_deck()
	

