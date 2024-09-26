# deck.py
import random

class Deck:
    """Class representing a deck of cards."""
    def __init__(self, cards):
        self.cards = cards

    def shuffle(self):
        """Shuffles the deck of cards."""
        random.shuffle(self.cards)

    def draw_card(self):
        """Draws a card from the deck."""
        if len(self.cards) > 0:
            return self.cards.pop(0)
        else:
            return None
