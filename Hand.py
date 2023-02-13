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
        self.cards.append(card)
        if card.rank == 'Ace':
            self.aces += 1

    def ace_adjust(self):
        while self.aces and not self.value <= 21:
            self.aces -= 1
            self.value -= 10
