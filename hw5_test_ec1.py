import unittest
import random
from hw5_cards_ec1 import *


class TestHand(unittest.TestCase):
    def setUp(self) -> None:
        self.deck = Deck()
        self.hand = Hand()

    @staticmethod
    def generate_hand(num_cards=0):
        """
        Generate a Hand object with >=1 num_cards / random number of cards
        """
        deck = Deck()
        deck.shuffle()
        max_num_cards = 52
        if num_cards == 0:
            num_cards = random.randint(1, max_num_cards)

        return Hand(deck.deal_hand(num_cards))

    def test_init(self):
        max_num_cards = 52
        num_cards = random.randint(0, max_num_cards)
        self.deck.shuffle()
        hand_list = self.deck.deal_hand(num_cards)
        hand = Hand(hand_list)

        # test default constructor
        self.assertIsInstance(self.hand, Hand)
        self.assertIsInstance(self.hand.init_cards, list)

        # test constructor with input
        self.assertIsInstance(hand, Hand)
        self.assertIsInstance(hand.init_cards, list)

        if len(hand.init_cards) > 0:
            for card in hand.init_cards:
                self.assertIsInstance(card, Card)

    def test_add_and_remove(self):
        # generate a Hand with >= 1 card(s)
        hand = self.generate_hand()
        assert isinstance(hand, Hand), "hand is not not a Hand"
        card = hand.init_cards[0]

        # cannot add "card" again
        orig_len = len(hand.init_cards)
        hand.add_card(card)
        self.assertEqual(orig_len, len(hand.init_cards))

        # test whether can remove a card in the hand
        orig_len = len(hand.init_cards)
        card_rm = hand.remove_card(card)
        self.assertIsInstance(card_rm, Card)
        self.assertEqual(len(hand.init_cards), orig_len - 1)

        # test whether can remove a card not in the hand
        orig_len = len(hand.init_cards)
        card_rm = hand.remove_card(card)
        self.assertIsInstance(card_rm, type(None))
        self.assertEqual(len(hand.init_cards), orig_len)

        # test whether can add a new card
        orig_len = len(hand.init_cards)
        hand.add_card(card)
        self.assertEqual(len(hand.init_cards), orig_len + 1)

    def test_draw(self):
        self.deck.shuffle()
        hand_size = random.randint(1, len(self.deck.cards))
        # next line ensures that no duplicate exists in the union of "hand" and "deck"
        hand = Hand(self.deck.deal_hand(hand_size))
        deck_len_orig = len(self.deck.cards)
        hand_len_orig = len(hand.init_cards)
        hand.draw(self.deck)
        self.assertEqual(len(self.deck.cards), deck_len_orig - 1)
        self.assertEqual(len(hand.init_cards), hand_len_orig + 1)


if __name__ == "__main__":
    unittest.main()
