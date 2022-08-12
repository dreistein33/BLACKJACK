import deck
import threading
import sys


class Player:
    def __init__(self, deck, name):
        self.deck = deck
        self.name = name
        self.score = 0
        self.set = self.deck.make_set(2)

    def add_card(self):
        self.set.append(self.deck.make_set(1)[0])

    def count_score(self):
        for i in self.set:
            self.score += i['points']
            check_thread = threading.Thread(target=self.check_score)
            check_thread.start()
        print(f"{self.name} -> {self.score}")

    def check_score(self):
        if self.score > 21:
            print(f"{self.name} LOSE")
            sys.exit(0)


if __name__ == '__main__':
    deck_ = deck.Deck()
    p1 = Player(deck_, "Wojtek")
    print(p1.set)
    p1.add_card()
    print(p1.set)
    p1.count_score()
