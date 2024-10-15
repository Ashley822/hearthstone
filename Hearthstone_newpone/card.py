import random

# Define the base Card class
class Card:
    def __init__(self, name, mana_cost, description):
        self.name = name
        self.mana_cost = mana_cost
        self.description = description

    def play(self):
        pass

    def __str__(self):
        return f"{self.name} (Mana: {self.mana_cost}) - {self.description}"

# Define the Minion class (inherits from Card)
class Minion(Card):
    def __init__(self, name, mana_cost, attack, health, abilities=[]):
        super().__init__(name, mana_cost, f"Attack: {attack}, Health: {health}, Abilities: {abilities}")
        self.attack = attack
        self.health = health
        self.abilities = abilities
        self.can_attack = False  # Minion cannot attack on the same turn it's summoned

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

    def play(self):
        print(f"{self.name} is summoned with {self.attack} attack and {self.health} health.")
        self.can_attack = False  # Reset can_attack to False when the minion is summoned

# Define the Spell class (inherits from Card)
class Spell(Card):
    def __init__(self, name, mana_cost, description, effect):
        super().__init__(name, mana_cost, description)
        self.effect = effect

    def play(self, target):
        self.effect(target)

# Define specific spell effects
def fireball_effect(target):
    target.health -= 6
    print(f"{target.name} takes 6 damage! Health is now {target.health}.")

def flamestrike_effect(target):
    for minion in target.battlefield:
        minion.health -= 5
        print(f"{minion.name} takes 5 damage! Health is now {minion.health}.")

def arcane_intellect_effect(player):
    player.draw_card()
    player.draw_card()

def holy_nova_effect(player, opponent):
    for minion in opponent.battlefield:
        minion.health -= 2
        print(f"{minion.name} takes 2 damage! Health is now {minion.health}.")
    for minion in player.battlefield:
        minion.health += 2
        print(f"{minion.name} is healed by 2 health! Health is now {minion.health}.")

def polymorph_effect(target):
    target.name = "Sheep"
    target.attack = 1
    target.health = 1
    print(f"{target.name} has been transformed into a Sheep! Attack: {target.attack}, Health: {target.health}")

def cataclysm_effect(player):
    player.battlefield.clear()
    print(f"All minions destroyed!")

def deadly_shot_effect(opponent):
    if opponent.battlefield:
        minion = random.choice(opponent.battlefield)
        opponent.battlefield.remove(minion)
        print(f"{minion.name} is destroyed by Deadly Shot!")

# Create all minions
all_minions = [
    Minion("Chillwind Yeti", 4, 4, 5),
    Minion("Boulderfist Ogre", 6, 6, 7),
    Minion("Bloodfen Raptor", 2, 3, 2),
    Minion("Stormwind Champion", 7, 6, 6, ["Buff: +1/+1 to other minions"]),
    Minion("Booty Bay Bodyguard", 5, 5, 4, ["Taunt"]),
    Minion("Wolfrider", 3, 3, 1, ["Charge"]),
    Minion("Spymistress", 1, 3, 1, ["Stealth"])
]

# Create all spells
all_spells = [
    Spell("Fireball", 4, "Deal 6 damage.", fireball_effect),
    Spell("Flamestrike", 7, "Deal 5 damage to all enemy minions.", flamestrike_effect),
    Spell("Arcane Intellect", 3, "Draw 2 cards.", arcane_intellect_effect),
    Spell("Holy Nova", 3, "Deal 2 damage to all enemy minions, restore 2 health to all friendly characters.", holy_nova_effect),
    Spell("Polymorph", 4, "Transform a minion into a 1/1 Sheep.", polymorph_effect),
    Spell("Cataclysm", 5, "Destroy all minions. Discard 2 cards.", cataclysm_effect),
    Spell("Deadly Shot", 3, "Destroy a random enemy minion.", deadly_shot_effect)
]
