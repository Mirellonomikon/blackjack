import random

from Card import *

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')


class Deck:

    def __init__(self):
        self.all_cards = []

        # We use 4 decks of cards
        for i in range(4):
            for suit in suits:
                for rank in ranks:
                    self.all_cards.append(Card(suit, rank))

    def __str__(self):
        return "Current deck: " + "\n".join(str(card) for card in self.all_cards)

    def shuffle(self):
        random.shuffle(self.all_cards)

    def deal_one(self):
        return self.all_cards.pop(0)

    def deal_cards(self, n):
        cards = []
        for i in range(1, n + 1):
            cards.append(self.all_cards.pop(0))
        return cards
