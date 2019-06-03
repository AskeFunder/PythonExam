import random



class Card(object):
    def __init__(self, suit, val):
        self.suit = suit
        self.value = val

    def __str__(self):
        return self.show()

    def __repr__(self):
        return self.show()

    def show(self):
        if self.value == 1:
            val = "Ace"
        elif self.value == 11:
            val = "Jack"
        elif self.value == 12:
            val = "Queen"
        elif self.value == 13:
            val = "King"
        else:
            val = self.value

        return "{} of {}".format(val, self.suit)

class Deck(object):
    def __init__(self):
        self.cards = []
        self.build

    def __str__(self):
        return self.show()

    def __repr__(self):
        return self.show()

    def show(self):
        for card in self.cards:
            print(card.show())

    
    def build(self):
        self.cards = []
        for suit in ['Hearts', "Clubs", "Spades", "Diamonds"]:
            for val in range(1,14):
                self.cards.append(Card(suit, val))

    def shuffle(self):
        random.shuffle(self.cards)


class Player(object):
    def __init__(self):
        self.type = ""
        self.hand = []
        self.money = 100

    def showhand(self):
        return "Your hand: {}".format(self.hand)
    

    def draw(self, deck):
        print("You draw a card")
        self.hand.append(deck.cards.pop())

class AI():
    def __init__(self):
        self.hand = []
        self.type = ""

    def draw(self, deck):
        print("The {} draws a card".format(self.type))
        self.hand.append(deck.cards.pop())

    def showhandhidden(self):
        return "The dealers hand [?]{}".format(self.hand[1:len(self.hand)])


    def showhand(self):
        if self.type == "player":
            return "The player's hand: {}".format(self.hand)
        elif self.type == "dealer":
            return "The dealers hand {}".format(self.hand)



    
        
def dealcards(player, ai, deck):
    player.draw(deck)
    ai.draw(deck)
    player.draw(deck)
    ai.draw(deck)

def calchand(hand):
    non_aces = [c for c in hand if c.value != 1]
    aces = [c for c in hand if c.value == 1]

    hand_sum = 0

    for card in non_aces:
        if card.value < 11:
            hand_sum += card.value
        else:
            hand_sum += 10

    hand_sum += len(aces)

    for card in aces:
        if hand_sum <= 11:
            hand_sum += 10
    
    return hand_sum







print("Hello, and welcome to Aske's blackjack game")
print("Would you like to be a player or a dealer?")
print("")
print(" player")
print(" dealer")
print("")

ai = AI()
player = Player()

while player.money > 0:
        player_type = input("Input answer here: ")
        if player_type == "dealer":
            player.type = player_type
            ai.type = "player"
            break
        elif player_type == "player":
            player.type = player_type
            ai.type = "dealer"
            break
        else:
            print("")
            print("Not correct answer try again")
            print("")

is_playing = True


deck = Deck()
deck.build()
random.shuffle(deck.cards)

while is_playing == True:

    player.hand = []
    ai.hand = []
    dealcards(player, ai, deck)

    while True:
    
        
        print("")
        print(ai.showhandhidden())
        print("{} {}".format(player.showhand(), calchand(player.hand)))
        print("")

        current_bet = 0

        

        if len(deck.cards) < 20:
            print("")
            print("The deck was shuffled")
            deck.build()
            deck.shuffle()

        while True:
            print("Current money: {}".format(player.money))
            current_bet = int(input("Please enter your bet: "))
            if current_bet > player.money: 
                print("You can't afford that bet")
                current_bet = 0
                break
            else:
                player.money -= current_bet
                break

        while calchand(player.hand) < 22:
            print("You have {}$ and your current bet is {}$".format(player.money, current_bet))
            action = input("Do you want to hit or stay?: ")
            if action == "hit":
                player.draw(deck)
                print("{} {}".format(player.showhand(), calchand(player.hand)))
            if action == "stay":
                break

        
        if calchand(player.hand) > 21:
            print("")
            print("The {} win".format(ai.type))
            print("You lose")
            print("")
            print("{} {}".format(player.showhand(), calchand(player.hand)))
            print("{} {}".format(ai.showhand(), calchand(ai.hand)))
            break


        while calchand(ai.hand) < 16:
            ai.draw(deck)
            print(ai.showhandhidden())
        
        if calchand(ai.hand) > 21:
            print("")
            print("The {} were busted".format(ai.type))
            print("You win {}$".format(current_bet * 2))
            player.money += current_bet * 2
            print("")
            print("{} {}".format(player.showhand(), calchand(player.hand)))
            print("{} {}".format(ai.showhand(), calchand(ai.hand)))
            break

        if calchand(ai.hand) < calchand(player.hand):
            print("")
            print("You win {}$".format(current_bet * 2))
            player.money += current_bet * 2
            print("")
            print("{} {}".format(player.showhand(), calchand(player.hand)))
            print("{} {}".format(ai.showhand(), calchand(ai.hand)))
            break
        else: 
            print("")
            print("The {} win".format(ai.type))
            print("You lose")
            print("")
            print("{} {}".format(player.showhand(), calchand(player.hand)))
            print("{} {}".format(ai.showhand(), calchand(ai.hand)))
            break

    print("")

    action = input("Press N to stop playing, anything else will start a new round")
    
    if action == "N":
        break
    
    print("") 



        







    

    
    
