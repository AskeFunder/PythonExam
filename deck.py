from card import Card

class Deck:
    def __init__(self):
        self.cards = list()

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        pass


    def shuffle(self):
        import random as r

        for suit in ["Hearts", "Clubs", "Spades", "Diamonds"]:
            for val in range(1, 14):
                card = Card(val, suit)
                self.cards.append(card)

        r.shuffle(self.cards) 

    def show(self):
        for card in self.cards:
            card.show()