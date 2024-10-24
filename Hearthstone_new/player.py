from hand import Hand
from card import Minion, Spell


class Player:
    def ensure_battlefield(self):
        # Ensures that battlefield is always an empty list or populated
        if self.battlefield is None:
            self.battlefield = []
    
    def __init__(self, name, deck):
        self.name = name
        self.deck = deck  # A deck of cards (a list)
        self.hand = Hand()  # Player's hand
        self.battlefield = []  # Minions on the battlefield
        self.mana_crystals = 1  # Starting with 1 mana crystal
        self.max_mana = 1  # Max mana crystals
        self.health = 30  # Starting health
        self.fatigue_damage = 1  # Fatigue damage if the player runs out of cards

    def draw_starting_hand(self):
        # Draw 3 cards from the deck to the hand at the start of the game
        for _ in range(3):
            self.draw_card()

    def draw_card(self):
        # Draw a card from the deck if possible
        if len(self.deck) > 0:
            card = self.deck.pop(0)
            self.hand.add_card(card)
            print(f"{self.name} draws {card.name}.")
        else:
            # Handle fatigue (no cards left to draw)
            self.health -= self.fatigue_damage
            self.fatigue_damage += 1
            print(f"{self.name} takes {self.fatigue_damage - 1} fatigue damage. Health is now {self.health}.")

    def attack_with_minion(self, minion_index, target_player=None, target_minion=None):
        # Ensure current player's battlefield is valid
        self.ensure_battlefield()

        if minion_index < len(self.battlefield):
            minion = self.battlefield[minion_index]
            if minion.can_attack:
                if target_minion:
                    # Ensure target_player and target_minion are valid
                    if target_player is not None:
                        target_player.ensure_battlefield()  # Ensure the target player has a valid battlefield
                        print(f"{minion.name} attacks {target_minion.name}")
                        minion.attack_minion(target_minion)

                        # Check if the target minion dies
                        if target_minion.health <= 0:
                            print(f"{target_minion.name} has died.")
                            target_player.battlefield.remove(target_minion)

                        # Check if the attacking minion dies
                        if minion.health <= 0:
                            print(f"{minion.name} has died.")
                            self.battlefield.remove(minion)
                    else:
                        print("Error: target_player is None.")
                else:
                    print(f"{minion.name} attacks {target_player.name}")
                    minion.attack_player(target_player)
                    minion.can_attack = False
            else:
                print(f"{minion.name} cannot attack this turn (summoning sickness).")
        else:
            print("Invalid minion index!")
    
    def start_turn(self):
        self.mana_crystals = min(self.max_mana, 10)
        self.max_mana += 1
        print(f"{self.name}'s turn begins with {self.mana_crystals} mana crystals.")
        for minion in self.battlefield:
            minion.can_attack = True

