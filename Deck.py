import random

from Card import *

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')


class Deck:
    """A class representing a deck of playing cards.
    Attributes:
        all_cards (list): A list containing all cards currently in the deck.
    Methods:
        shuffle_deck(): Randomly shuffles all cards in the deck.
        need_shuffle(): Checks if deck needs to be shuffled based on remaining cards.
        deal_one(): Deals a single card from the top of the deck.
        deal_cards(n): Deals n cards from the top of the deck.
    """

    def __init__(self):
        self.all_cards = []

        # We use 4 decks of cards
        for i in range(4):
            for suit in suits:
                for rank in ranks:
                    self.all_cards.append(Card(suit, rank))

    def __str__(self):
        return "Current deck: " + "\n".join(str(card) for card in self.all_cards)

    def shuffle_deck(self):
        random.shuffle(self.all_cards)

    def need_shuffle(self):
        return len(self.all_cards) < 52

    def deal_one(self):
        return self.all_cards.pop(0)

    def deal_cards(self, n):
        cards = self.all_cards[:n]
        self.all_cards = self.all_cards[n:]
        return cards
