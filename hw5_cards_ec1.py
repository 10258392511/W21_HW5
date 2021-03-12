from hw5_cards import *


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
