from player import Player
from card import all_minions, all_spells

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
        valid_input = False
        while not valid_input:
            print(f"{current_player.name}, choose a card to play (or type 'skip' to pass your turn):")
            choice = input(f"Enter card index (0-{len(current_player.hand.cards) - 1}) or 'skip': ").strip()

            if choice == 'skip':
                print(f"{current_player.name} skips their turn.")
                valid_input = True
            else:
                try:
                    card_index = int(choice)
                    if 0 <= card_index < len(current_player.hand.cards):
                        current_player.hand.play_card(card_index, current_player, opponent)
                        valid_input = True
                    else:
                        print("Invalid choice. Please choose a valid card index.")
                except (ValueError, IndexError):
                    print("Invalid input. Please enter a valid number or 'skip'.")
    else:
        print(f"{current_player.name} has no cards to play.")

    # Minion attacks
    if len(current_player.battlefield) > 0:
        valid_input = False
        while not valid_input:
            print(f"{current_player.name}, choose a minion to attack with (or type 'skip'): ")
            for i, minion in enumerate(current_player.battlefield):
                print(f"{i}: {minion}")
            choice = input(f"Enter minion index (0-{len(current_player.battlefield) - 1}) or 'skip': ").strip()

            if choice == 'skip':
                print(f"{current_player.name} skips attacking.")
                valid_input = True
            else:
                try:
                    minion_index = int(choice)
                    if 0 <= minion_index < len(current_player.battlefield):
                        print("Do you want to attack the opponent or a minion? (type 'player' or 'minion')")
                        target_choice = input().lower()

                        if target_choice == 'player':
                            current_player.attack_with_minion(minion_index, target_player=opponent)
                        elif target_choice == 'minion':
                            if len(opponent.battlefield) > 0:
                                for i, minion in enumerate(opponent.battlefield):
                                    print(f"{i}: {minion}")
                                target_minion_index = int(input(f"Choose an opponent's minion to attack (0-{len(opponent.battlefield) - 1}): "))
                                current_player.attack_with_minion(minion_index, target_minion=opponent.battlefield[target_minion_index])
                                if opponent.battlefield[target_minion_index].health <= 0:
                                    opponent.battlefield.remove(opponent.battlefield[target_minion_index])
                            else:
                                print("Opponent has no minions to attack.")
                        valid_input = True
                    else:
                        print("Invalid choice. Please choose a valid minion index.")
                except (ValueError, IndexError):
                    print("Invalid input. Please enter a valid number or 'skip'.")
    else:
        print(f"{current_player.name} has no minions to attack with.")

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

# Setup the game
deck1 = all_minions + all_spells
deck2 = all_minions + all_spells

# Create two players with their respective decks
player1 = Player("Player 1", deck1)
player2 = Player("Player 2", deck2)

# Draw starting hands
player1.draw_starting_hand()
player2.draw_starting_hand()

# Player 2 draws an extra card for being second
player2.draw_card()

# Start the game loop
game_loop(player1, player2)