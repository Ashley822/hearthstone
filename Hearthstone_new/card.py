# card.py

class Card:
    def __init__(self, name, mana_cost, description):
        self.name = name
        self.mana_cost = mana_cost
        self.description = description

    def play(self):
        pass

    def __str__(self):
        return f"{self.name} (Mana: {self.mana_cost}) - {self.description}"

class Minion(Card):
    def __init__(self, name, mana_cost, attack, health, abilities=None):
        super().__init__(name, mana_cost, "Minion")
        self.attack = attack
        self.health = health
        self.abilities = abilities if abilities is not None else []
        self.can_attack = False

    def attack_minion(self, target):
        print(f"{self.name} attacks {target.name}")
        target.health -= self.attack
        self.health -= target.attack
        print(f"{self.name} health is now {self.health}")
        print(f"{target.name} health is now {target.health}")

    def attack_player(self, target_player):
        print(f"{self.name} attacks {target_player.name} for {self.attack} damage!")
        target_player.health -= self.attack
        print(f"{target_player.name}'s health is now {target_player.health}")

    def __str__(self):
        return f"{self.name} (Mana: {self.mana_cost}) - Attack: {self.attack}, Health: {self.health}, Abilities: {self.abilities}"

class Spell(Card):
    def __init__(self, name, mana_cost, description, effect):
        super().__init__(name, mana_cost, description)
        self.effect = effect

    def play(self, target):
        self.effect(target)

# Define Spell effects
def fireball_effect(target):
    target.health -= 6
    print(f"{target.name} takes 6 damage! Health is now {target.health}.")

def polymorph_effect(target):
    target.name = "Sheep"
    target.attack = 1
    target.health = 1
    print(f"{target.name} has been transformed into a Sheep! Attack: {target.attack}, Health: {target.health}")
