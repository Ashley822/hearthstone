# main.py

from cards import Minion, Spell
from player import Player
from game import Game

# Create some example cards
minions = [
    Minion("Chillwind Yeti", 4, 4, 5, "A classic yeti minion with solid stats."),
    Minion("Boulderfist Ogre", 6, 6, 7, "A powerful ogre minion with high attack and health."),
]

# Define the Spell effect as regular functions
def fireball_effect(target):
    target.health -= 6

spells = [
    Spell("Fireball", 4, "Deal 6 damage.", fireball_effect),
]

# Create player decks by combining minions and spells
deck1 = minions + spells
deck2 = minions + spells

# Create two players
player1 = Player("Player 1", deck1)
player2 = Player("Player 2", deck2)

# Create a game and start it
game = Game(player1, player2)
game.game_loop()
