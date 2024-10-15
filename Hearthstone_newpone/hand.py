from card import Spell, Minion 

class Hand:
    def __init__(self):
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)

    def play_card(self, card_index, player, opponent):
        if 0 <= card_index < len(self.cards):
            card = self.cards.pop(card_index)
            player.mana_crystals -= card.mana_cost
            if isinstance(card, Spell):
                card.play(opponent)
            elif isinstance(card, Minion):
                card.play()
                player.battlefield.append(card)
            return card
        return None

    def display_hand(self):
        print("Hand:")
        for i, card in enumerate(self.cards):
            print(f"{i}: {card}")
