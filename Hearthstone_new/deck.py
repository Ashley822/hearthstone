# deck.py

import random

class Deck:
    def __init__(self, cards):
        self.cards = cards

    def shuffle(self):
        random.shuffle(self.cards)

    def draw_card(self):
        if len(self.cards) > 0:
            return self.cards.pop(0)
        else:
            return None
