

class Player:

    def __init__(self):
        self.hand = []
        self.hand_total = 0
        self.win = False
        self.money = 100

    def clear_hand(self):
        self.hand = []

    def add_card_to_hand(self, card):
        self.hand.append(card)

    def show_hand(self):
        return self.hand

    def give_money(self, value):
        self.money -= value

    def get_money(self, value):
        self.money += value


class Dealer(Player):

    pass

class User(Player):

    def user_draw(self):
        if input("Hit or Stand? H/s ").lower() != "s":
            return True
        else:
            print(" ")
            return False
