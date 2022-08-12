import deck
import threading
import sys


class Player:
    def __init__(self, deck, name):
        self.deck = deck
        self.name = name
        self.set = self.deck.make_set(2)
        self.score = self.return_points()

    def add_card(self):
        self.set.append(self.deck.make_set(1)[0])
        self.score = self.return_points()

    def return_points(self):
        points = [x['points'] for x in self.set]
        score = sum(points)
        return score
    # def check_score(self):
    #     if self.score > 21:
    #         print(f"{self.name} LOSE")
            


if __name__ == '__main__':
    deck_ = deck.Deck()
    p1 = Player(deck_, "Wojtek")
    print(p1.set)
    p1.add_card()
    print(p1.set)
    
