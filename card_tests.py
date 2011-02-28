#!/usr/bin/env python

import unittest
import itertools
import random
from random import Random

from card import Card

class CardTests(unittest.TestCase):
    def setUp(self):
        self.random = Random()
        self.value = self.random.randint(1,13)
        self.suit = self.random.choice(Card.suits)
        
    def test_static_suits(self):
        self.assertTrue("spades" in Card.suits)
        self.assertTrue("clubs" in Card.suits)
        self.assertTrue("hearts" in Card.suits)
        self.assertTrue("diamonds" in Card.suits)
        self.assertTrue(len(Card.suits) == 4)
        
    def test_init_valid(self):
        card = Card(self.value, self.suit)
        self.assertEqual(card.suit, self.suit)
        self.assertEqual(card.index, self.value)
        
    def test_repr(self):
        card = Card(self.value, self.suit)
        repr_card = eval(repr(card))
        self.assertEqual(repr_card, card)
        
        
    def test_init_invalid(self):
        invalid_suits = [self.suit, None, "spade", "diamond", "club", "heart", "abracadabra"]
        invalid_values = [self.value, None, 0, Card.KING_INDEX + 1, random.randint(-100, -1), random.randint(15,100)]
        
        # Test the cross product of all the invalid suits and invalid values
        for invalid_suit, invalid_value in itertools.product(invalid_suits, invalid_values):
            if not (invalid_suit == self.suit and invalid_value == self.value):
                self.assertRaises(ValueError, Card, invalid_value, invalid_suit)


    def test_face_card(self):
        face_card = Card(self.random.randint(Card.JACK_INDEX,Card.KING_INDEX), self.random.choice(Card.suits))
        self.assertTrue(face_card.is_face())
        self.assertEqual(face_card.value, ["J", "Q", "K"][face_card.index - Card.JACK_INDEX])
        
        
    def test_normal_card(self):
        normal_card = Card(self.random.randint(1,9), self.random.choice(Card.suits))
        self.assertFalse(normal_card.is_face())
        self.assertEqual(normal_card.value, str(normal_card.index))
        
        
    def test_str(self):
        normal_card = Card(7, "spades")
        face_card = Card(12, "clubs")
        self.assertEqual(str(normal_card), "7 of spades")
        self.assertEqual(str(face_card), "Q of clubs")
        
    def test_unicode(self):
        normal_card = Card(8, "hearts")
        face_card = Card(11, "diamonds")
        
        self.assertEqual(unicode(normal_card), u'8\u2665')
        self.assertEqual(unicode(face_card), u'J\u2666')
        
    def test_value_setter(self):
        normal_card = Card(6, "hearts")
        self.assertEqual(normal_card.value, '6')
        self.assertEqual(normal_card.index, 6)
        normal_card.value = 10
        self.assertEqual(normal_card.value, '10')
        self.assertEqual(normal_card.index, 10)
        normal_card.value = 'J'
        self.assertEqual(normal_card.value, 'J')
        self.assertEqual(normal_card.index, Card.JACK_INDEX)
        normal_card.value = '4'
        self.assertEqual(normal_card.value, '4')
        self.assertEqual(normal_card.index, 4)
    
    def test_value_setter_invalid(self):
        invalid_values = ['Kings', 'Jack', 'Queen', '0', -1, 0, 14, random.randint(15,100), random.randint(-100, -1)]
        for value in invalid_values:
            card = Card(3, "diamonds")
            try:
                card.value = value
                self.assert_(False)
            except ValueError as e:
                self.assert_(isinstance(e, ValueError))

    def test_eq(self):
        card1 = Card('6', 'hearts')
        card2 = Card('J', 'hearts')
        self.assertNotEqual(card1, card2)
        self.assertEqual(card1, card1)
        self.assertEqual(card1, Card(6, 'hearts'))
        
    def test_lt(self):
        card1 = Card('2', 'hearts')
        card2 = Card(2, 'spades')
        cards = [None, card2]
        for card in cards:
            try:
                card1 < card
                self.assert_(False) # This line should never be reached
            except ValueError as e:
                self.assert_(isinstance(e, ValueError))
                
        for suit in Card.suits:
            self.assert_(Card(2, suit) < Card(3, suit))
            self.assert_(Card('J', suit) < Card('Q', suit))
            self.assert_(Card('Q', suit) < Card('K', suit))
            self.assert_(Card('J', suit) < Card('K', suit))
        
            
    def tearDown(self):
        self.value = None
        self.suit = None
        self.random = None
        

if __name__ == "__main__":
    unittest.main()
