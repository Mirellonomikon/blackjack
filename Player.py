from Hand import *
from Deck import *

class Player:
    """A class representing a player in a blackjack game.
    The Player class manages the player's chips, hands, bets and actions during gameplay.
    Attributes:
        chips (int): The amount of chips the player currently has
        hands (list): List of Hand objects representing the player's current hands
        current_hand (int): Index of the currently active hand
        bets (list): List of bet amounts corresponding to each hand
    Methods:
        get_current_hand(): Returns the currently active Hand object
        next_hand(): Moves to the next hand if available
        win_chips(amount, hand_index): Adds won chips to player's total
        bet_chips(amount): Places a bet for the current hand
        double_down(): Doubles the bet and adds one card to current hand
        split_hand(): Splits a pair into two separate hands
        hit(deck): Takes another card from the deck
        stand(): Ends the turn for current hand
    """

    def __init__(self, chips):
        self.chips = chips
        self.hands = [Hand()]
        self.current_hand = 0
        self.bets = [0]

    def get_current_hand(self):
        return self.hands[self.current_hand]
    
    def next_hand(self):
        if self.current_hand < len(self.hands) - 1:
            self.current_hand += 1
            return True
        return False

    def win_chips(self, amount, hand_index=0):
        self.chips += amount
        print(f"You win {amount} chips on hand {hand_index + 1}.")

    def bet_chips(self, amount): 
        if self.chips < amount:
            print("You don't have enough chips to bet that amount.")
            return False
        else:
            self.chips -= amount
            self.bets[self.current_hand] = amount
            print(f"You bet {amount} chips on hand {self.current_hand + 1}.")
            return True

    def double_down(self):
        if len(self.hands[self.current_hand].cards) != 2:
            print("You can only double down on your first two cards.")
            return False
        if self.chips < self.bets[self.current_hand]:
            print("You don't have enough chips to double down.")
            return False
        self.chips -= self.bets[self.current_hand]
        self.bets[self.current_hand] *= 2

        # Add one more card and end the turn for this hand
        self.hands[self.current_hand].add_card(Deck.deal_one())
        print(f"Doubled down on hand {self.current_hand + 1}. New bet: {self.bets[self.current_hand]}")
        return True
    
    def split_hand(self):
        if len(self.hands[self.current_hand].cards) != 2 or self.hands[self.current_hand].cards[0].rank != self.hands[self.current_hand].cards[1].rank:
            print("You can only split with two cards of the same rank.")
            return False
        if self.chips < self.bets[self.current_hand]:
            print("You don't have enough chips to split.")
            return False
        
        new_hand = Hand()
        new_hand.add_card(self.hands[self.current_hand].cards.pop())
        self.hands.append(new_hand)

        self.chips -= self.bets[self.current_hand]
        self.bets.append(self.bets[self.current_hand])

        # Add one more card for each hand
        self.hands[self.current_hand].add_card(Deck.deal_one())
        self.hands[-1].add_card(Deck.deal_one())

        print(f"Hand split. You now have {len(self.hands)} hands.")
        print("Current bets: " + ", ".join(str(bet) for bet in self.bets))
        return True

    def hit(self, deck):
        card = deck.deal_one()
        self.get_current_hand().add_card(card)
        print(f"You drew {card}")

    def stand(self):
        print(f"You stand on hand {self.current_hand + 1}")
        