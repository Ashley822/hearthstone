from card import Minion, Spell, fireball_effect, polymorph_effect
from player import Player
from deck import Deck
from hand import Hand

# Game loop logic
def game_loop(player1, player2):
    while player1.health > 0 and player2.health > 0:
        # Player 1's turn
        player_turn(player1, player2)
        if player2.health <= 0:
            print(f"{player1.name} wins!")
            return

        # Player 2's turn
        player_turn(player2, player1)
        if player1.health <= 0:
            print(f"{player2.name} wins!")
            return

def player_turn(current_player, opponent):
    # Start the player's turn
    current_player.start_turn()

    # Draw a card
    current_player.draw_card()

    # Display the player's hand and battlefield
    current_player.hand.display_hand()
    print(f"{current_player.name}'s battlefield: {[str(minion) for minion in current_player.battlefield]}")

    # Let the player choose a card to play
    if len(current_player.hand.cards) > 0:
        print(f"{current_player.name}, choose a card to play (or type 'skip' to pass your turn):")
        choice = input(f"Enter card index (0-{len(current_player.hand.cards) - 1}) or 'skip': ")

        if choice != 'skip':
            try:
                card_index = int(choice)
                current_player.hand.play_card(card_index, current_player, opponent)
            except (ValueError, IndexError):
                print("Invalid choice. Turn skipped.")
        else:
            print(f"{current_player.name} skips their turn.")
    else:
        print(f"{current_player.name} has no cards to play.")

    # Minion attacks
    if len(current_player.battlefield) > 0:
        print(f"{current_player.name}, choose a minion to attack with (or type 'skip'): ")
        for i, minion in enumerate(current_player.battlefield):
            print(f"{i}: {minion}")
        choice = input(f"Enter minion index (0-{len(current_player.battlefield) - 1}) or 'skip': ")

        if choice != 'skip':
            try:
                minion_index = int(choice)
                if len(opponent.battlefield) > 0:
                    print(f"Do you want to attack the opponent or a minion? (type 'player' or 'minion')")
                    target = input()
                    if target == 'player':
                        current_player.attack_with_minion(minion_index, target_player=opponent)
                    elif target == 'minion':
                        print(f"Choose an opponent's minion to attack:")
                        for i, minion in enumerate(opponent.battlefield):
                            print(f"{i}: {minion}")
                        target_minion_index = int(input(f"Choose an opponent's minion to attack (0-{len(opponent.battlefield) - 1}): "))
                        
                        # Ensure battlefield is valid before attacking
                        current_player.ensure_battlefield()
                        opponent.ensure_battlefield()

                        current_player.attack_with_minion(minion_index, target_minion=opponent.battlefield[target_minion_index])

                        if opponent.battlefield[target_minion_index].health <= 0:
                            opponent.battlefield.remove(opponent.battlefield[target_minion_index])
                    else:
                        print("Invalid choice. Attack skipped.")
                else:
                    print("Opponent has no minions to attack.")
            except (ValueError, IndexError):
                print("Invalid choice. Attack skipped.")
        else:
            print(f"{current_player.name} skips attacking.")

# Setup the game
minions = [
    Minion("Chillwind Yeti", 4, 4, 5),
    Minion("Boulderfist Ogre", 6, 6, 7),
    Minion("Bloodfen Raptor", 2, 3, 2),
    Minion("Stormwind Champion", 7, 6, 6, ["Buff: +1/+1 to other minions"]),
    Minion("Booty Bay Bodyguard", 5, 5, 4, ["Taunt"]),
    Minion("Wolfrider", 3, 3, 1, ["Charge"]),
]

spells = [
    Spell("Fireball", 4, "Deal 6 damage.", fireball_effect),
    Spell("Polymorph", 4, "Transform a minion into a 1/1 Sheep.", polymorph_effect),
]

# Create player decks by combining minions and spells
deck1 = minions + spells
deck2 = minions + spells

# Create two players with their respective decks
player1 = Player("Player 1", deck1)
player2 = Player("Player 2", deck2)

# Draw starting hands
player1.draw_starting_hand()  # Player 1 draws 3 cards
player2.draw_starting_hand()  # Player 2 draws 3 cards
player2.draw_card()  # Player 2 draws an extra card (for going second)

# Start the game loop
game_loop(player1, player2)
