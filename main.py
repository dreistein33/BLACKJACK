import deck
import player


class Game:
    def __init__(self):
        self.deck = deck.Deck()
        self.player1 = player.Player(self.deck, "Wojtek")
        self.player2 = player.Player(self.deck, "Adam")

    def start(self):
        print("\t\t\t\tTHE GAME OF BLACKJACK")
        print(f"\n\t\t\t\t{self.player1.name} STARTS!")
        

if __name__ == '__main__':
    game = Game()
    game.start()
