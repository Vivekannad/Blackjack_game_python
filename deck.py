
from card import Card,suits,ranks,values
import random

class Deck:

    def __init__(self):
        self.all_cards = []
        for suit in suits:
            for rank in ranks:
                self.all_cards.append(Card(suit,rank))


    def shuffle_cards(self):
        """
        shuffles the cards
        :return:
        """
        random.shuffle(self.all_cards)

    def deal_one(self):
        """
        takes one card out as in real life game
        :return:
        """
        return self.all_cards.pop(0)

    def __str__(self):
        """
        returns the cards in a deck
        :return:
        """
        return f"THe deck has {len(self.all_cards)} cards"