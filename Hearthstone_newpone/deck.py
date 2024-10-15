import random
from card import all_minions, all_spells

class Deck:
    def __init__(self, cards=None):
        if cards is None:
            cards = random.sample(all_minions + all_spells, 10)  # Create a deck with random cards
        self.cards = cards

    def shuffle(self):
        random.shuffle(self.cards)

    def draw_card(self):
        if len(self.cards) > 0:
            return self.cards.pop(0)
        else:
            return None

    def display_deck(self):
        print("Deck:")
        for card in self.cards:
            print(card)
