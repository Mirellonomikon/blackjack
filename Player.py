from Hand import *


class Player:

    def __init__(self, chips):
        self.chips = chips
        self.hand = Hand()

    def win_chips(self, amount):
        self.chips += amount

    def bet_chips(self):
        pass
