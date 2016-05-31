from my_deck import Deck
from my_player import Dealer
from my_player import User
import os
import time


class Game:

    def __init__(self):
        self.dealer = Dealer()
        self.user = User()
        self.game_deck = Deck().shuffle_deck()

    def play_blackjack(self):
        os.system("clear")
        print("\n               -*-*- Blackjack -*-*-               \n\n"
              "Closest to 21 without going over, Dealer stands on 17\n"
              "You have ${} in the bank, each game is for $10\n"
              "-----------------------------------------------------".format(self.user.money))
        self.deal_cards()
        print("Dealer's Cards: ", end="")
        print(self.dealer.show_hand()[0], "| ##")
        print("\nYour Cards:     ", end="")
        print(" | ".join(self.user.show_hand()))
        self.user_draw()
        print("Dealers Hand: ", " | ".join(self.dealer.show_hand()))
        self.dealer_draw()
        print("\nDealer has {}, and you have {}.\n".format(self.hand_value(self.dealer.show_hand()), self.hand_value(self.user.show_hand())))
        game.winner()

    def hand_value(self, hand):
        self.ace_reorder(hand)
        self.hand_total = 0
        for card in hand:
            if card[0] in "1JQK":
                self.hand_total += 10
            elif card[0] is "A":
                if self.hand_total + 11 <= 21:
                    self.hand_total += 11
                elif self.hand_total > 21:
                    self.hand_total += 1
            else:
                self.hand_total += int(card[0])
        return int(self.hand_total)

    def ace_reorder(self, hand):
        for index, card in enumerate(hand):
            if card[0] is "A":
                hand += [hand.pop(index)]

    def win_bust(self, hand):
        if self.hand_value(hand) >= 22:
            print("\n ** Bust! ** \n")
        elif self.hand_value(hand) == 21:
            print("\n *** Blackjack! *** \n")
            blackjack = True

    def winner(self):
        you_win = " *** You Win! ***\n"
        dealer_win = " * Dealer Wins! *\n"
        dealer_hand_value = self.hand_value(self.dealer.show_hand())
        user_hand_value = self.hand_value(self.user.show_hand())
        dealer_blackjack = dealer_hand_value == 21
        user_blackjack = user_hand_value == 21
        dealer_bust = dealer_hand_value >= 22
        user_bust = user_hand_value >= 22
        if user_bust and dealer_bust:
            print("Both busted, Dealer wins")
            self.pay_dealer(self.user)
        elif dealer_blackjack and not user_blackjack:
            print(dealer_win)
            self.pay_dealer(self.user)
        elif dealer_hand_value > user_hand_value:
            if dealer_bust:
                print(you_win)
                self.pay_player(self.user)
                game.play_again()
            if user_bust:
                print(dealer_win)
                self.pay_dealer(self.user)
            print(dealer_win)
            self.pay_dealer(self.user)
            game.play_again()
        elif dealer_hand_value < user_hand_value:
            if user_bust:
                print(dealer_win)
                self.pay_dealer(self.user)
                game.play_again()
            print(you_win)
            self.pay_player(self.user)
        elif dealer_hand_value == user_hand_value:
            if dealer_blackjack and user_blackjack:
                print(" * Both have Blackjack, Dealer Wins! *")
                self.pay_dealer(self.user)
            else:
                print("Push, tie, keep your money.")
        else:
            print("Well, that was an odd hand!?!?")
        game.play_again()

    def deal_cards(self):
        for _ in range(2):
            self.give_card(self.user)
            self.give_card(self.dealer)

    def give_card(self, player):
        if len(self.game_deck) <= 26:
            self.game_deck = Deck().shuffle_deck()
        card = self.game_deck.pop()
        player.add_card_to_hand(card)

    def pay_dealer(self, player):
        player.give_money(10)

    def pay_player(self, player):
        player.get_money(10)

    def dealer_draw(self):
        while self.hand_value(self.dealer.show_hand()) < 17:
            self.give_card(self.dealer)
            time.sleep(.25)
            print("Dealer Draws: ", " | ".join(self.dealer.show_hand()))
        self.win_bust(self.dealer.show_hand())

    def user_draw(self):
        while self.hand_value(self.user.show_hand()) < 21 and self.user.user_draw():
            self.give_card(self.user)
            print("Your new cards: ", " | ".join(self.user.show_hand()))
        self.win_bust(self.user.show_hand())

    def play_again(self):
        print("You have ${} in the bank.".format(self.user.money))
        if self.user.money <= 0:
            print("Sorry, you're out of money, see you later.")
            exit()
        elif input("\nPlay Again? Y/n ").lower() != "n":
            self.dealer.clear_hand()
            self.user.clear_hand()
            game.play_blackjack()
        else:
            print("\nThanks for playing Blackjack")
            exit()

game = Game()
game.play_blackjack()
