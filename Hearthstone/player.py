# player.py

from deck import Deck
from cards import Minion, Spell

class Player:
    """Represents a player in the game, holding a deck, hand, and battlefield."""
    def __init__(self, name, deck):
        self.name = name
        self.deck = Deck(deck)
        self.hand = []
        self.battlefield = []
        self.mana_crystals = 1
        self.max_mana = 1
        self.health = 30
        self.fatigue_damage = 1

    def draw_card(self):
        """Draws a card from the player's deck."""
        card = self.deck.draw_card()
        if card:
            self.hand.append(card)
            print(f"{self.name} draws {card.name}")
        else:
            self.take_fatigue_damage()

    def take_fatigue_damage(self):
        """Handles fatigue damage when no cards are left in the deck."""
        print(f"{self.name} suffers {self.fatigue_damage} fatigue damage!")
        self.health -= self.fatigue_damage
        self.fatigue_damage += 1

    def start_turn(self):
        """Begins the player's turn by replenishing mana and enabling minion attacks."""
        self.mana_crystals = min(self.max_mana, 10)
        self.max_mana += 1
        print(f"{self.name}'s turn begins with {self.mana_crystals} mana crystals.")

        for minion in self.battlefield:
            minion.can_attack = True
