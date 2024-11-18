values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10,
          'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}


class Card:
    """A class representing a playing card.
    Attributes:
        suit (str): The suit of the card (Hearts, Diamonds, Clubs, Spades)
        rank (str): The rank of the card (2-10, Jack, Queen, King, Ace)  
        value (int): The numerical value of the card in Blackjack
    """

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + " of " + self.suit
