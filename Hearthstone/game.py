# game.py

from player import Player
from board import Board

class Game:
    """Handles the main game flow."""
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.board = Board()

    def game_loop(self):
        """Runs the main game loop."""
        while self.player1.health > 0 and self.player2.health > 0:
            self.player_turn(self.player1, self.player2)
            if self.player2.health <= 0:
                print(f"{self.player1.name} wins!")
                return
            self.player_turn(self.player2, self.player1)
            if self.player1.health <= 0:
                print(f"{self.player2.name} wins!")
                return

    def player_turn(self, current_player, opponent):
        """Handles a player's turn, allowing them to draw cards and play cards."""
        current_player.start_turn()
        current_player.draw_card()
