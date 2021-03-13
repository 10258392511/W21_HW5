import random
from hw5_cards import Card, print_hand

# create the Hand with an initial set of cards
class Hand:
    '''a hand for playing card
    Class Attributes
    ----------------
    None

    Instance Attributes
    -------------------
    init_card: list
        a list of cards
    '''

    def __init__(self, init_cards=None):
        if init_cards is None:
            init_cards = []
        self.init_cards = init_cards

    def add_card(self, card):
        '''add a card
        add a card to the hand
        silently fails if the card is already in the hand

        Parameters
        -------------------
        card: instance
            a card to add

        Returns
        -------
        None
        '''
        for card_iter in self.init_cards:
            if card_iter.__str__() == card.__str__():
                return

        self.init_cards.append(card)

    def remove_card(self, card):
        '''remove a card from the hand

        Parameters
        -------------------
        card: instance
            a card to remove

        Returns
        -------
        the card, or None if the card was not in the Hand
        '''
        try:
            self.init_cards.remove(card)
            return card
        except ValueError as e:
            return None

    def draw(self, deck):
        '''draw a card
        draw a card from a deck and add it to the hand
        side effect: the deck will be depleted by one card

        Parameters
        -------------------
        deck: instance
            a deck from which to draw

        Returns
        -------
        None
        '''
        card = deck.deal_card()
        self.add_card(card)

    def remove_pairs(self):
        '''Removes pairs of cards in a hand.
        If there are three of a kind, only one will be left.
        If there are four of a kind, none will be left.

        Returns
        -------
        None
        '''
        sort_hand = [[] for _ in range(13)]
        for card in self.init_cards:
            rank_list = sort_hand[card.rank - 1]
            if len(rank_list) == 0:
                rank_list.append(card)
            elif len(rank_list) == 1:
                sort_hand[card.rank - 1] = []

        self.init_cards = [rank_list[0] for rank_list in sort_hand if len(rank_list) > 0]


class Deck:
    '''a deck of Cards
    Instance Attributes
    -------------------
    cards: list
        the list of Cards currently in the Deck. Initialized to contain
        all 52 cards in a standard deck
    '''

    def __init__(self):

        self.cards = []
        for suit in range(4):
            for rank in range(1, 14):
                card = Card(suit, rank)
                self.cards.append(card)  # appends in a sorted order

    def deal_card(self, i=-1):
        '''remove a card from the Deck
        Parameters
        -------------------
        i: int (optional)
            the index of the ard to remove. Default (-1) will remove the "top" card
        Returns
        -------
        Card
            the Card that was removed
        '''
        return self.cards.pop(i)

    def shuffle(self):
        '''shuffles (randomizes the order) of the Cards
        self.cards is modified in place
        Parameters
        ----------
        None
        Returns
        -------
        None
        '''
        random.shuffle(self.cards)

    def replace_card(self, card):
        card_strs = []  # forming an empty list
        for c in self.cards:  # each card in self.cards (the initial list)
            card_strs.append(c.__str__())  # appends the string that represents that card to the empty list
        if card.__str__() not in card_strs:  # if the string representing this card is not in the list already
            self.cards.append(card)  # append it to the list

    def sort_cards(self):
        '''returns the Deck to its original order

        Cards will be in the same order as when Deck was constructed.
        self.cards is modified in place.
        Parameters
        ----------
        None
        Returns
        -------
        None
        '''
        self.cards = []
        for suit in range(4):
            for rank in range(1, 14):
                card = Card(suit, rank)
                self.cards.append(card)

    def deal_hand(self, hand_size):
        '''removes and returns hand_size cards from the Deck

        self.cards is modified in place. Deck size will be reduced
        by hand_size
        Parameters
        -------------------
        hand_size: int
            the number of cards to deal
        Returns
        -------
        list
            the top hand_size cards from the Deck
        '''
        hand_cards = []
        for i in range(hand_size):
            hand_cards.append(self.deal_card())
        return hand_cards

    def deal(self, num_hands, num_cards) -> list:
        '''Deals "num_hands" hands of "num_cards" cards for each one. If num_cards is -1, all cards in the deck should be
        dealt even though this may result in uneven hands.

        Parameters
        ----------
        num_hands: int
            Number of hands to generate.
        num_cards: int
            Number of cards per hand.

        Returns
        -------
        hands: list of Hand
            Hands generated.
        '''
        if num_cards > 0:
            assert num_hands * num_cards <= len(self.cards), "too many cards to be dealt"

        hands = []
        if num_cards == -1:
            num_cards_tgt = len(self.cards) // num_hands
            for _ in range(num_hands - 1):
                hands.append(Hand(self.deal_hand(num_cards_tgt)))
            hands.append(Hand(self.deal_hand(len(self.cards))))

        else:
            for _ in range(num_hands):
                hands.append(Hand(self.deal_hand(num_cards)))

        return hands
