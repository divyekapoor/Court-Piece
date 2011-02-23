#!/usr/bin/env python

import sys
import os


class Card(object):
    suits = ["spade", "clubs", "hearts", "diamonds"]
    face = ["J", "Q", "K"]
    pretty_suits = [u"\u2660", u"\u2663", u"\u2665", u"\u2666"]
    
    def __init__(self, value, suit):
        """Constructor for Cards"""
        # use property assignments to initialize
        self.value = value
        self.suit = suit
        
        
    def int_value(self):
        """Returns an integer representation of the card value. Range: 1-13."""
        return self._value
        
    @property
    def value(self):
        """Getter for the expected string representation of the card value"""
        return (self.is_face() and face[self.value - 10]) or str(self.value)
        
    @value.setter
    def value(self,value_):
        """Setter for the card value"""
        if value_ <= 0 or value_ > 13:
            raise ValueError("The value %d is out of bounds for a deck of cards." % value_)
        self._value = value_
        
        
    @property
    def suit(self):
        """Getter for the expected string representation of the card suit"""
        return Card.suits[self._suit]
        
    @suit.setter
    def suit(self, suit_):
        """Setter for the card suit"""
        if suit_ not in Card.suits:
            throw ValueError("Invalid Suit supplied. Suit must be one of %r" % Card.suits)
        self._suit = Card.suits.index(suit_)
        
    def __str__(self):
        return "%s of %s" % (self.value, self.suit)
        
    def __unicode__(self):
        return "%s
        
    def is_face(self):
        return self.value >= 10
        
