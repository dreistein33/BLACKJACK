import random


class Deck:
    def __init__(self):
        self.deck = [
        {"card": "2", "count": 1, "points": 2},
        {"card": "3", "count": 1, "points": 3},
        {"card": "4", "count": 1, "points": 4},
        {"card": "5", "count": 1, "points": 5},
        {"card": "6", "count": 1, "points": 6},
        {"card": "7", "count": 1, "points": 7},
        {"card": "8", "count": 1, "points": 8},
        {"card": "9", "count": 1, "points": 9},
        {"card": "10", "count": 1, "points": 10},
        {"card": "Jack", "count": 1, "points": 10},
        {"card": "Queen", "count": 1, "points": 10},
        {"card": "King", "count": 1, "points": 10},
        {"card": "Ace", "count": 1, "points": 11}
    ]
        self.deck = self.deck * 4

    def distribute(self):
        return self.deck.pop(random.randrange(len(self.deck)))

    def make_set(self, k):
        player_set = []
        for i in range(k):
            player_set.append(self.distribute())
        return player_set
    

if __name__ == '__main__':
    deck = Deck()
    print(deck.deck)        
