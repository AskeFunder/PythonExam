import unittest
from deck import Deck

class DeckTest(unittest.TestCase):

    def test_deck_build(self):
        deck = Deck()
        deck.shuffle()
        self.assertEqual(len(deck.cards), 52)


if __name__ == "__main__":
    unittest.main()