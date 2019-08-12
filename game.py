from deck import Deck
from player import Player
from ai import AI
from deck import Deck
import time as t
from not_enough_money_exception import NotEnoughMoneyError

class Game:
    def __init__(self, deck: Deck, player: Player, ai: AI):
        self.deck = deck
        self.placed_bet = None
        self.player = player
        self.ai = ai
        self.player_busted = False
        self.ai_busted = False

    @classmethod
    def create_game(cls):
        deck = Deck()
        deck.shuffle()
        player = Player("You")
        ai = AI("The Dealer")

        return cls(deck, player, ai)

    def show_hands_hidden(self):
        print("Your hand: {} {}   AI hand: {} {} or higher".format(self.player.show_hand(), self.player.calc_hand(), self.ai.show_hand_hidden(), self.ai.calc_hand_hidden()))

    def show_hands(self):
        print("Your hand: {} {}   AI hand: {} {}".format(self.player.show_hand(), self.player.calc_hand(), self.ai.show_hand(), self.ai.calc_hand()))



    def prepare_round(self):
        if len(self.deck.cards) <= 20:

            self.ai_busted = False
            self.player_busted = False

            print("The deck only has 20 cards left and was shuffled")
            self.deck.shuffle()
            print()


        self.discard_hands()
        self.draw_hands(0.5)

        
    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        pass

    def discard_hands(self):
        self.player.discard_hand()
        self.ai.discard_hand()

    def draw_hands(self, delay: float=0):
        for i in range(2):
            self.player.draw_card(self.deck)
            t.sleep(delay)
            self.ai.draw_card(self.deck)
            t.sleep(delay)
            print()
    
    def take_bet(self, player: Player):
        print("Your money: {}$".format(player.money))
        bet = input("Please place your bet: ")
        print()

        if type(bet) is not int:
            bet = int(bet)

        while True:
            try:
                player.place_bet(bet)
                self.placed_bet = bet
                break
            except NotEnoughMoneyError as e:
                print("You don't have enough money")
                continue

    def clear_bet(self):
        self.placed_bet = None
