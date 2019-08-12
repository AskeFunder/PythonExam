from deck import Deck
from not_enough_money_exception import NotEnoughMoneyError

class Player:
    def __init__(self, name: str):
        self.name = name
        self.hand = list()
        self.money = 200
        
    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        pass

    def draw_card(self, deck: Deck):
        print("{} draws a card".format(self.name))
        card = deck.cards.pop()
        self.hand.append(card)

        if self.calc_hand() > 21:
            return False
        else:
            return True

    def place_bet(self, bet: int):
        if self.money < bet:
            raise NotEnoughMoneyError
            
        self.money = self.money - bet

    def show_hand(self):

        hand_string = ""

        for card in self.hand:
            hand_string += card.__str__() 
            hand_string += ", "

        return hand_string
            

    def discard_hand(self):
        self.hand = list()

    def calc_hand(self):
        sum = 0

        non_aces = [card for card in self.hand if card.val != 1]
        aces = [card for card in self.hand if card.val == 1]

        for card in non_aces:
            if card.val >= 10:
                sum += 10
            else:
                sum += card.val
        
        aces_len = len(aces)

        sum += aces_len

        for card in aces:
            if sum <= 11:
                sum += 10

        return sum
