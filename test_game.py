import unittest

from game import Game
from deck import Deck
from player import Player
from ai import AI

class GameTest(unittest.TestCase):

    def test_draw_hands(self):
    
        game = Game.create_game()

        self.assertEqual(0, len(game.ai.hand))
        self.assertEqual(0, len(game.player.hand))

        game.draw_hands()

        self.assertEqual(2, len(game.ai.hand))
        self.assertEqual(2, len(game.player.hand))


if __name__ == "__main__":
    unittest.main()

        