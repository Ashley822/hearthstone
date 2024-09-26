# cards.py

class Card:
    """Base class for all cards."""
    def __init__(self, name, mana_cost, description):
        self.name = name
        self.mana_cost = mana_cost
        self.description = description

    def play(self):
        """Placeholder for playing a card."""
        pass

    def __str__(self):
        return f"{self.name} (Mana: {self.mana_cost}) - {self.description}"


class Minion(Card):
    """Defines a minion card with attack, health, and optional abilities."""
    def __init__(self, name, mana_cost, attack, health, description, abilities=None):
        super().__init__(name, mana_cost, description)
        self.attack = attack
        self.health = health
        self.can_attack = False
        self.abilities = abilities if abilities else []

    def has_ability(self, ability):
        return ability in self.abilities

    def play(self):
        """Summons a minion to the board."""
        print(f"{self.name} is summoned with {self.attack} attack and {self.health} health.")
        if 'Charge' in self.abilities:
            self.can_attack = True
        else:
            self.can_attack = False

    def attack_minion(self, target):
        print(f"{self.name} attacks {target.name}")
        target.health -= self.attack
        self.health -= target.attack

    def attack_player(self, target_player):
        print(f"{self.name} attacks {target_player.name} for {self.attack} damage!")
        target_player.health -= self.attack


class Spell(Card):
    """Defines a spell card that can apply effects."""
    def __init__(self, name, mana_cost, description, effect):
        super().__init__(name, mana_cost, description)
        self.effect = effect

    def play(self, target):
        self.effect(target)
