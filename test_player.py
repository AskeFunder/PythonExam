from deck import Deck
from player import Player
from not_enough_money_exception import NotEnoughMoneyError

import unittest

class PlayerTest(unittest.TestCase):

    def test_draw_card(self):
        deck = Deck()
        deck.shuffle()
        player = Player("Jens")

        self.assertEqual(0, len(player.hand))

        counter = 0

        for i in range(5):
            player.draw_card(deck)
            counter += 1
            self.assertEqual(counter, len(player.hand))

    def test_place_bet(self):
        player = Player("Jens")
        self.assertEqual(200, player.money)
        player.place_bet(10)
        self.assertEqual(190, player.money)

        with self.assertRaises(NotEnoughMoneyError):
            player.place_bet(1000)

    def test_discard_hand(self):
        player = Player("Jens")
        deck = Deck()
        deck.shuffle()

        self.assertEqual(0, len(player.hand))
        
        for i in range(5):
            player.draw_card(deck)

        self.assertEqual(5, len(player.hand))
        player.discard_hand()
        self.assertEqual(0, len(player.hand))



if __name__ == "__main__":
    unittest.main()