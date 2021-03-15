#################################
#####    Name: Zhexin Wu    #####
#####  Uniqname: zhexinwu   #####
#################################

import unittest
import hw5_cards
import random


class TestCard(unittest.TestCase):

    def test_construct_Card(self):
        c1 = hw5_cards.Card(0, 2)  # suit, rank: D, 2
        c2 = hw5_cards.Card(1, 1)  # C, 1

        self.assertEqual(c1.suit, 0)
        self.assertEqual(c1.suit_name, "Diamonds")
        self.assertEqual(c1.rank, 2)
        self.assertEqual(c1.rank_name, "2")

        self.assertIsInstance(c1.suit, int)
        self.assertIsInstance(c1.suit_name, str)
        self.assertIsInstance(c1.rank, int)
        self.assertIsInstance(c1.rank_name, str)

        self.assertEqual(c2.suit, 1)
        self.assertEqual(c2.suit_name, "Clubs")
        self.assertEqual(c2.rank, 1)
        self.assertEqual(c2.rank_name, "Ace")

    def setUp(self) -> None:
        self.deck = hw5_cards.Deck()
        
    def test_q1(self):
        '''
        1. fill in your test method for question 1:
        Test that if you create a card with rank 12, its rank_name will be "Queen"
        
        2. remove the pass command
        
        3. uncomment the return command and 
        3b. change X, Y to the values from your assert statement
        ### please note: normally unit test methods do not have return statements. But returning will allow for unit testing of your unit test, and allow you to check your answer with the autograder.  This is optional today.

        '''
        card = hw5_cards.Card(rank=12)
        self.assertEqual(card.rank_name, "Queen")
        return card.rank_name, "Queen"
    
    def test_q2(self):
        '''
        1. fill in your test method for question 2:
        Test that if you create a card instance with suit 1, its suit_name will be "Clubs"
        
        2. remove the pass command
        
        3. uncomment the return command and 
        3b. change X, Y to the values from your assert statement
        ### please note: normally unit test methods do not have return statements. But returning will allow for unit testing of your unit test, and allow you to check your answer with the autograder.  This is optional today.

        '''
        card = hw5_cards.Card(suit=1)
        self.assertEqual(card.suit_name, "Clubs")
        return card.suit_name, "Clubs"
    

    def test_q3(self):
        '''
        1. fill in your test method for question 3:
        Test that if you invoke the __str__ method of a card instance that is created with suit=3, rank=13, it returns the string "King of Spades"

        
        2. remove the pass command
        
        3. uncomment the return command and 
        3b. change X, Y to the values from your assert statement
        ### please note: normally unit test methods do not have return statements. But returning will allow for unit testing of your unit test, and allow you to check your answer with the autograder.  This is optional today.

        '''
        card = hw5_cards.Card(suit=3, rank=13)
        out_str = card.__str__()
        self.assertEqual(out_str, "King of Spades")
        return out_str, "King of Spades"
    
    def test_q4(self):
        '''
        1. fill in your test method for question 4:
        Test that if you create a eck instance, it will have 52 cards in its cards instance variable
        
        2. remove the pass command
        
        3. uncomment the return command and 
        3b. change X, Y to the values from your assert statement
        ### please note: normally unit test methods do not have return statements. But returning will allow for unit testing of your unit test, and allow you to check your answer with the autograder.  This is optional today.

        '''
        deck = hw5_cards.Deck()
        # out_l = len(self.deck.cards)
        out_l = len(deck.cards)
        self.assertEqual(out_l, 52)
        return out_l, 52

    def test_q5(self):
        '''
        1. fill in your test method for question 5:
        Test that if you invoke the deal_card method on a deck, it will return a card instance.
        
        2. remove the pass command
        
        3. uncomment the return command and 
        3b. change X, Y to the values from your assert statement
        ### please note: normally unit test methods do not have return statements. But returning will allow for unit testing of your unit test, and allow you to check your answer with the autograder.  This is optional today.

        '''
        deck = hw5_cards.Deck()
        # card = self.deck.deal_card()
        card = deck.deal_card()
        self.assertIsInstance(card, hw5_cards.Card)
        return card, hw5_cards.Card
    
    def test_q6(self):
        '''
        1. fill in your test method for question 6:
        
        Test that if you invoke the deal_card method on a deck, the deck has one fewer cards in it afterwards.
        
        2. remove the pass command
        
        3. uncomment the return command and 
        3b. change X, Y to the values from your assert statement
        ### please note: normally unit test methods do not have return statements. But returning will allow for unit testing of your unit test, and allow you to check your answer with the autograder.  This is optional today.

        '''
        deck = hw5_cards.Deck()
        # orig_len = len(self.deck.cards)
        orig_len = len(deck.cards)
        _ = deck.deal_card()
        self.assertEqual(orig_len - 1, len(deck.cards))

        return orig_len - 1, len(deck.cards)
    

    def test_q7(self):
        '''
        1. fill in your test method for question 7:
        Test that if you invoke the replace_card method, the deck has one more card in it afterwards. (Please note that you want to use deal_card function first to remove a card from the deck and then add the same card back in)

        
        2. remove the pass command
        
        3. uncomment the return command and 
        3b. change X, Y to the values from your assert statement
        ### please note: normally unit test methods do not have return statements. But returning will allow for unit testing of your unit test, and allow you to check your answer with the autograder.  This is optional today.

        '''
        deck = hw5_cards.Deck()
        undealt_len = len(deck.cards)
        card = deck.deal_card()
        orig_len = len(deck.cards)
        self.assertEqual(undealt_len, orig_len + 1)
        deck.replace_card(card)
        self.assertEqual(len(deck.cards), orig_len + 1)
        return undealt_len, len(deck.cards), orig_len + 1
    
    def test_q8(self):
        '''
        1. fill in your test method for question 8:
        Test that if you invoke the replace_card method with a card that is already in the deck, the deck size is not affected.(The function must silently ignore it if you try to add a card that’s already in the deck)

        
        2. remove the pass command
        
        3. uncomment the return command and 
        3b. change X, Y to the values from your assert statement
        ### please note: normally unit test methods do not have return statements. But returning will allow for unit testing of your unit test, and allow you to check your answer with the autograder.  This is optional today.

        '''
        deck = hw5_cards.Deck()
        card = hw5_cards.Card(rank=random.randint(1, 13), suit=random.randint(0, 3))
        orig_len = len(deck.cards)
        deck.replace_card(card)
        self.assertEqual(orig_len, len(deck.cards))
        return orig_len, len(deck.cards)


if __name__=="__main__":
    unittest.main()
    # tester = TestCard()
    # print(tester.test_q1())
