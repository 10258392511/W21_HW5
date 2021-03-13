import unittest
import random
from hw5_cards_ec2 import *


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

    def test_remove_pairs(self):
        # make a hand with one entire suit
        cards = [Card(0, i) for i in range(1, 14)]
        hand_copy = Hand(cards.copy())

        # case 1: no pairs at all
        hand = Hand(cards.copy())
        hand.remove_pairs()
        for card, card_c in zip(hand.init_cards, hand_copy.init_cards):
            self.assertEqual(card.__str__(), card_c.__str__())

        # case 2: only contains pairs
        hand = Hand(cards.copy())
        num_cards_add = random.randint(1, 13)
        # print(f"num_cards_add: {num_cards_add}")
        inds = random.sample(range(1, 14), num_cards_add)
        for ind in inds:
            hand.add_card(Card(1, ind))
        hand.remove_pairs()
        # print(len(hand_copy.init_cards))
        self.assertEqual(len(hand.init_cards), len(hand_copy.init_cards) - num_cards_add)

        # case 3: pairs + three of a kind
        hand = Hand(cards.copy())
        for rank in range(1, 14):
            hand.add_card(Card(1, rank))

        num_cards_add = random.randint(1, 13)
        inds = random.sample(range(1, 14), num_cards_add)
        for ind in inds:
            hand.add_card(Card(2, ind))

        hand.remove_pairs()
        self.assertEqual(len(hand.init_cards), num_cards_add)

        # case 4 pairs + three of a kind + fours
        num_ranks = 4
        ranks = random.sample(range(1, 14), num_ranks)
        hand = Hand()
        for i, rank in enumerate(ranks):
            for suit in range(i + 1):
                hand.add_card(Card(suit, rank))

        hand.remove_pairs()
        self.assertEqual(len(hand.init_cards), 2)

    def test_deal(self):
        # case 1: number of cards to be dealt is greater than 52
        num_hands = random.randint(1, 10)
        num_cards = len(self.deck.cards) // num_hands + 2
        with self.assertRaises(AssertionError):
            self.deck.deal(num_hands, num_cards)

        # case 2: num_cards == -1
        self.deck = Deck()
        orig_len = len(self.deck.cards)
        num_hands = random.randint(1, 10)
        hands = self.deck.deal(num_hands, -1)
        # for hand in hands:
        #     print_hand(hand.init_cards)
        out_len = 0
        for hand in hands:
            out_len += len(hand.init_cards)
        self.assertEqual(out_len, orig_len)
        # print(self.deck.cards)
        self.assertEqual(len(self.deck.cards), 0)

        # case 3: a normal dealt
        self.deck = Deck()
        orig_len = len(self.deck.cards)
        num_hands = random.randint(1, 10)
        num_cards = len(self.deck.cards) // num_hands
        hands = self.deck.deal(num_hands, num_cards)
        acc_len = 0
        for hand in hands:
            self.assertEqual(len(hand.init_cards), num_cards)
            acc_len += len(hand.init_cards)
        self.assertEqual(acc_len + len(self.deck.cards), orig_len)


if __name__ == "__main__":
    unittest.main()
