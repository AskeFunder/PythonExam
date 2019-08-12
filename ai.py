from player import Player

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
