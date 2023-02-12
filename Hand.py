from Card import *


class Hand:

    def __init__(self):
        self.cards = []
        self.aces = 0
        self.value = 0

    def __str__(self):
        result = ', '.join(str(card) for card in self.cards)
        return result

    def add_card(self, card):
        self.value += card.value
