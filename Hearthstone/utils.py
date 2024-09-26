# utils.py

def display_hand(hand):
    """Displays the cards in the player's hand."""
    print("Hand:")
    for i, card in enumerate(hand):
        print(f"{i}: {card}")
