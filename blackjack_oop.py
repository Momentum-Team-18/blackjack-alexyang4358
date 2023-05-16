import random

suits = ['♥︎', '♠︎', '♣︎', '♦︎']
ranks = [
    {"rank": 'A', "value": 11 or 1},
    {"rank": '2', "value": 2},
    {"rank": '3', "value": 3},
    {"rank": '4', "value": 4},
    {"rank": '5', "value": 5},
    {"rank": '6', "value": 6},
    {"rank": '7', "value": 7},
    {"rank": '8', "value": 8},
    {"rank": '9', "value": 9},
    {"rank": '10', "value": 10},
    {"rank": 'J', "value": 10},
    {"rank": 'Q', "value": 10},
    {"rank": 'K', "value": 10},
]


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f"{self.rank} of {self.suit}"


class Deck:
    def __init__(self, suits, ranks):
        self.cards = []
        for suit in suits:
            for rank in ranks:
                new_card = Card(suit, rank)
                self.cards.append(new_card)

    def __str__(self):
        deck_string = ''
        for card in self.cards:
            deck_string += ' ' + str(card)
        return deck_string

    def shuffle(self):
        random.shuffle(self.cards)


class Dealer:
    def __init__(self):
        self.hand = []

    def __str__(self):
        return 'Dealer'


class Player:
    def __init__(self, name):
        self.hand = []
        self.name = name

    def __str__(self):
        return self.name

    def choice(self):
        choice = input("Would you like to (h)it or (s)tay: ")
        return choice


# sample_deck = Deck(suits, ranks)
# sample_deck.shuffle()
# print(sample_deck)
