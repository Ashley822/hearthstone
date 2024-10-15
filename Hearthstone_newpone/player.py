from deck import Deck
from hand import Hand

class Player:
    def __init__(self, name, deck):
        self.name = name
        self.deck = Deck(deck)
        self.hand = Hand()
        self.battlefield = []
        self.mana_crystals = 1
        self.max_mana = 1
        self.health = 30
        self.fatigue_damage = 1

    def draw_starting_hand(self):
        for _ in range(3):
            self.hand.add_card(self.deck.draw_card())

    def draw_card(self):
        card = self.deck.draw_card()
        if card:
            self.hand.add_card(card)
            print(f"{self.name} draws {card.name}")
        else:
            self.take_fatigue_damage()

    def take_fatigue_damage(self):
        print(f"{self.name} suffers {self.fatigue_damage} fatigue damage!")
        self.health -= self.fatigue_damage
        self.fatigue_damage += 1

    def start_turn(self):
        self.mana_crystals = min(self.max_mana, 10)
        self.max_mana += 1
        print(f"{self.name}'s turn begins with {self.mana_crystals} mana crystals.")
        for minion in self.battlefield:
            minion.can_attack = True
