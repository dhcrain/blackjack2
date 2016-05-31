import random


class Deck:

    def __init__(self):
        self.card_numbers = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        self.card_suit = ["♥", "♦", "♠", "♣"]
        self.deck = [(num + " " + suit) for num in self.card_numbers for suit in self.card_suit]
        self.deck *= 6      # 6 cards in the shoe

    def shuffle_deck(self):
        random.shuffle(self.deck)
        return self.deck
