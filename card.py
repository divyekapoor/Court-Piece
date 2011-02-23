#!/usr/bin/env python

import sys
import os


class Card(object):
    # Public exposed array
    suits = ["spades", "clubs", "hearts", "diamonds"]

    # Static Class Constants
    JACK_INDEX = 11
    KING_INDEX = 13
    
    # Internal Class Variables
    _face = ["J", "Q", "K"]
    _pretty_suits = [u"\u2660", u"\u2663", u"\u2665", u"\u2666"]

    
    def __init__(self, value, suit):
        """Constructor for Cards"""
        # use property assignments to initialize
        self.value = value
        self.suit = suit

    @property
    def index(self):
        """Returns an integer representation of the card value. Range: 1-13.
        This is the index of the card in the suit."""
        return self._value
        
    @property
    def value(self):
        """Getter for the expected string representation of the card value"""
        return (self.is_face() and Card._face[self.index - Card.JACK_INDEX]) or str(self._value)
        
    @value.setter
    def value(self,value_):
        """Setter for the card value"""
        if value_ <= 0 or value_ > Card.KING_INDEX:
            raise ValueError("The value %r is out of bounds for a deck of cards." % value_)
        self._value = value_
        
        
    @property
    def suit(self):
        """Getter for the expected string representation of the card suit"""
        return Card.suits[self._suit]
        
    @suit.setter
    def suit(self, suit_):
        """Setter for the card suit"""
        if suit_ not in Card.suits:
            raise ValueError("Invalid Suit supplied. Suit must be one of %r" % Card.suits)
        self._suit = Card.suits.index(suit_)
    
    @property
    def unicode_suit(self):
        """Getter for a unicode representation of the suit"""
        return self._pretty_suits[self._suit]
        
    def __str__(self):
        """Return a string representation of the card"""
        return "%s of %s" % (self.value, self.suit)
        
    def __unicode__(self):
        """Return a unicode string representation of the card. Use pretty symbols for suits"""
        return u"%s %s" % (self.value, self.unicode_suit)
        
    def is_face(self):
        """Is the card a face card?"""
        return self.index >= Card.JACK_INDEX
        
