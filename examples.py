#!/usr/bin/env python

from card import Card
from game import CourtPiece, HumanPlayer
import sys


def print_deck():
    print "A deck of cards: "
    for suit in Card.suits:
        print suit + ": ",
        for value in range(1,13):
            print unicode(Card(value, suit)),
        print

def play_one_round():
    # Create a game of Court Piece with 4 players
    # Note: The input-output file handles are currently stdin and stdout
    #   They can be easily changed to be socket handles
    court_piece = CourtPiece([
        HumanPlayer('Bharat', sys.stdin, sys.stdout), 
        HumanPlayer('Swagat', sys.stdin, sys.stdout),
        HumanPlayer('Rohit', sys.stdin, sys.stdout),
        HumanPlayer('Divye', sys.stdin, sys.stdout),
        ])
        
    court_piece.play()
    
            
if __name__ == "__main__":
    print_deck()
    play_one_round()
    

