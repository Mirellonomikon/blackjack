from Deck import *
from Hand import *

class Dealer:
    """
    A class representing a dealer in a blackjack game.
    Attributes:
        hand (Hand): The dealer's current hand of cards
        show_cards (bool): Flag indicating whether all dealer's cards should be visible
    Methods:
        hit(deck): Takes one card from the deck and adds it to dealer's hand
        can_hit(): Checks if dealer must hit (hand value < 17)
        show_hand(): Displays dealer's cards if show_cards is True
        reset_hand(): Resets dealer's hand to a new empty hand
        __str__(): Returns string representation of dealer's hand, hiding cards if necessary
    """
    
    def __init__(self):
        self.hand = Hand()
        self.show_cards = False

    def hit(self, deck):
        self.hand.add_card(deck.deal_one())

    def can_hit(self):
        return self.hand.get_value() < 17
    
    def show_hand(self):
        if self.show_cards:
            print(self.hand)

    def reset_hand(self):
        self.hand = Hand()
        self.show_one_card = True

    def __str__(self):
        if not self.show_cards:
            return f"Dealer's Hand: {self.hand.cards[0]}, <card hidden>"
        else:
            return f"Dealer's Hand: {self.hand}"
        