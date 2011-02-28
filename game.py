#!/usr/bin/env python

class Game(object):    
    def __init__(self):
        pass
        
    def play(self):
        pass
    
    

class GameState(object):
    """Store the game state visible publicly. Eg. timers, points etc."""
    
    def __init__(self):
        pass
        
    def __repr__(self):
        return "GameState()"
        

class Player(object):
    def __init__(self, name):
        self.name = name
    
    def __unicode__(self):
        return self.name
        
    def __str__(self):
        return self.name
        
    def __repr__(self):
        return 'Player(' + repr(self.name) + ')'
        
    def play(self, game_state):
        return None
    

class HumanPlayer(Player):
    
    def __init__(self, name, input_stream, output_stream, prompts=True):
        Player.__init__(self, name)
        self.input = input_stream
        self.output = output_stream
        self.prompts = prompts
        
        
    def __repr__(self):
        return 'HumanPlayer(' + repr(self.name) + ')'
        
    def play(self, state):
        if self.prompts:
            self.output.write("Game State: %s\n%s> " % (state, self))
            self.output.flush()
            
        for line in self.input: # TODO: Fix needed. Lines are not read in one by one...
            if line != "":
                value, suit = line.split(' ', 2)
                return Card(value, suit)
            else:
                if self.prompts:
                    self.output.write("%s> " % self)
        
    

class CourtPiece(object):
    def __init__(self, players):
        self.players = players
        self.game_state = GameState()
        
    def play(self):
        for player in self.players:
            print "Player (%s) played %s" % (player, player.play(self.game_state))
