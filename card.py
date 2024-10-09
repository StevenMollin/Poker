import random

class Card:

    CARD_LIST = []
    SUIT = 'BRMF'
    POINT = '23456789TJQKA'

    def __init__(self):
        self.create_card_list()
        self.shuffle()

    def shuffle(self) -> None:
        random.shuffle(self.CARD_LIST)

    def create_card_list(self) -> None:
        con = 0
        for s in self.SUIT:
            for n in self.POINT:
                self.CARD_LIST.append(s+n)
                con+=1

    def separate_point(self):
        NUM_LIST = []

        for n in self.CARD_LIST:
            NUM_LIST.append(n[1])

        return NUM_LIST

    def sparate_suit(self):
        SUIT_LIST = []
        for n in Card.CARD_LIST:
            SUIT_LIST.append(n[0])

        return SUIT_LIST

if __name__ == '__main__':
    Card = Card()
    print(Card.CARD_LIST)
    print(Card.separate_point())
    print(Card.sparate_suit())