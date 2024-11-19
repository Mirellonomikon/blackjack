from Card import *


class Hand:
    """A class representing a hand in a game of Blackjack.
    Attributes:
        cards (list): A list containing Card objects in the hand
        aces (int): Count of aces in the hand
        value (int): Current total value of cards in the hand
    Methods:
        add_card(card): Adds a card to the hand and updates the total value
        ace_adjust(): Adjusts ace values (11->1) when hand would bust
        is_bust(): Checks if hand value exceeds 21
        is_blackjack(): Checks if hand is a natural blackjack
        get_value(): Returns current value of hand after ace adjustment
    """

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
            self.ace_adjust()

    def ace_adjust(self):
        while self.aces and not self.value <= 21:
            self.aces -= 1
            self.value -= 10

    def is_bust(self):
        return self.get_value() > 21
    
    def is_blackjack(self):
        return len(self.cards) == 2 and self.get_value() == 21
    
    def get_value(self):
        self.ace_adjust()
        return self.value
    