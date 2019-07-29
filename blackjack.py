import time as t

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

class AI(Player):

    def calc_hand_hidden(self):
        sum = 0

        hand_copy = list(self.hand)
        hand_copy.pop(0)

        non_aces = [card for card in hand_copy if card.val != 1]
        aces = [card for card in hand_copy if card.val == 1]

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

    def show_hand_hidden(self):

        hand_string = ""

        first_iteration = True

        for card in self.hand:

            if first_iteration:
                hand_string += "?, "
                first_iteration = False
                continue
            
            hand_string += card.__str__() 
            hand_string += ", "

        return hand_string


            
        

class Game:
    def __init__(self, deck: Deck, player: Player, ai: AI):
        self.deck = deck
        self.placed_bet = None
        self.player = player
        self.ai = ai
        self.player_busted = False
        self.ai_busted = False

    

    def show_hands_hidden(self):
        print("Your hand: {} {}   AI hand: {} {} or higher".format(p.show_hand(), p.calc_hand(), ai.show_hand_hidden(), ai.calc_hand_hidden()))

    def show_hands(self):
        print("Your hand: {} {}   AI hand: {} {}".format(p.show_hand(), p.calc_hand(), ai.show_hand(), ai.calc_hand()))



    def prepare_round(self):
        if len(self.deck.cards) <= 20:

            self.ai_busted = False
            self.player_busted = False

            print("The deck only has 20 cards left and was shuffled")
            self.deck.shuffle()
            print()


        self.discard_hands()
        self.draw_hands()

        
    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        pass

    def discard_hands(self):
        self.player.discard_hand()
        self.ai.discard_hand()

    def draw_hands(self):
        for i in range(2):
            self.player.draw_card(self.deck)
            t.sleep(0.5)
            self.ai.draw_card(self.deck)
            t.sleep(0.5)
            print()
    
    def take_bet(self, player: Player):
        print("Your money: {}$".format(player.money))
        bet = input("Please place your bet: ")
        print()

        if type(bet) is not int:
            bet = int(bet)

        player.place_bet(bet)
        self.placed_bet = bet

    def clear_bet(self):
        self.placed_bet = None


def setup_game():
        player = Player("You")
        ai = AI("Dealer")
        deck = Deck()
        game = Game(deck, player, ai)

        return game




game = setup_game()

with game.player as p:
    with game.ai as ai:
        while True:
            if game.placed_bet != None:
                game.clear_bet()

            game.prepare_round()
            game.show_hands_hidden()#print("Your hand: {} {}   AI hand: {} {}".format(p.show_hand(), p.calc_hand(), ai.show_hand(), ai.calc_hand_hidden()))
            game.take_bet(game.player)

            
            while True:
                print("Your money: {}$   Your bet: {}$".format(p.money, game.placed_bet))
                game.show_hands_hidden()#print("Your hand: {} {}   AI hand: {} {}".format(p.show_hand(), p.calc_hand(), ai.show_hand(), ai.calc_hand_hidden()))
                print()
                inp = input("Would you like to draw another card? Y/N  ")
                print()

                inp = str.lower(inp)
                
                if inp == "y":
                    if not p.draw_card(game.deck):
                        game.player_busted = True
                        
                        print()
                        game.show_hands()
                        print("{} were busted".format(p.name))
                        print("{} lost {}$".format(p.name, game.placed_bet))
                        #print("Your hand: {} {}   AI hand: {} {}".format(p.show_hand(), p.calc_hand(), ai.show_hand(), ai.calc_hand_hidden()))
                        print()
                        break
                elif inp == "n":
                    break

                if not game.player_busted:
                    if ai.calc_hand() < 17:
                        if not ai.draw_card(game.deck):
                            game.ai_busted = True
                            print()
                            print("{} were busted".format(ai.name))
                            game.show_hands()#print("Your hand: {} {}   AI hand: {} {}".format(p.show_hand(), p.calc_hand(), ai.show_hand(), ai.calc_hand_hidden()))
                            print("You win {}$".format(game.placed_bet))
                            p.money += (game.placed_bet * 2)

                            print()
                            break
            
            if not game.player_busted:
                while ai.calc_hand() < 17:
                    if not ai.draw_card(game.deck):
                        game.ai_busted = True
                        print()
                        game.show_hands()#print("Your hand: {} {}   AI hand: {} {}".format(p.show_hand(), p.calc_hand(), ai.show_hand(), ai.calc_hand_hidden()))
                        print("{} were busted".format(ai.name))
                        print("You win {}$".format(game.placed_bet))
                        print()
                        p.money += (game.placed_bet * 2)

                        break
                    t.sleep(0.5)

            if game.ai_busted != True and game.player_busted != True:
                if p.calc_hand() > ai.calc_hand() and p.calc_hand() < 22 and ai.calc_hand() < 22:
                    print("{} wins {}$".format(p.name, (game.placed_bet * 2)))
                    game.show_hands()
                    print()
                    p.money += (game.placed_bet * 2)
                else:
                    print("{} wins".format(ai.name))
                    game.show_hands()
                    print("You lose {}$".format(game.placed_bet))
                    print()

            print("New game begins in 5 seconds")
            print()
            t.sleep(5)

    


    