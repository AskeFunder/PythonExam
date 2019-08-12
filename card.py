class Card:
    def __init__(self, val: int, suit: str):
        self.val = val
        self.suit = suit

        
    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        pass

    def show(self):
        print(self.__str__())

    def __str__(self):

        if self.val == 1:
            rank = "Ace"
        elif self.val == 11:
            rank = "Jack"
        elif self.val == 12:
            rank = "Queen"
        elif self.val == 13:
            rank = "King"
        else:
            rank = str(self.val)

        return "{} of {}".format(rank, self.suit)