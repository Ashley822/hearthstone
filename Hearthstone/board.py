# board.py

class Board:
    """Represents the game board where minions battle."""
    def __init__(self):
        self.player1_minions = []
        self.player2_minions = []

    def add_minion(self, player, minion):
        """Adds a minion to the appropriate player's side of the board."""
        if player == 1:
            self.player1_minions.append(minion)
        else:
            self.player2_minions.append(minion)

    def remove_minion(self, player, minion):
        """Removes a minion from the appropriate player's side of the board."""
        if player == 1:
            self.player1_minions.remove(minion)
        else:
            self.player2_minions.remove(minion)
