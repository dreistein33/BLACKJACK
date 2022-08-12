import deck
import player
import random
import sys

class Game:
    def __init__(self):
        self.deck = deck.Deck()
        self.player1 = player.Player(self.deck, "Dealer")
        self.player2 = player.Player(self.deck, "Adam")

    def check_who_first(self):
        players = [self.player1, self.player2]
        return random.choice(players)

    def player_turn(self, player):
        while True:
            choice = input(f"SCORE: {player.score} # {player.name} # ADD CARD? [yes/no]\n>>").lower()
            if choice == 'yes':
                player.add_card()
                print(f"{player.name} -> {player.score}")
            elif choice == 'no':
                print(f"{player.name} -> {player.score}")
                break
            if player.score > 21:
                print(f'{player.name} LOSE!')
                sys.exit(0)
    
    def compare_score(self):
        if self.player1.score > self.player2.score:
            print(f"\n\t\t\t\t{self.player1.name} WINS!")
        else:
            print(f"\n\t\t\t\t{self.player2.name} WINS!")

    def display_start(self, player):
        greeting = "\t\t\t\tTHE GAME OF BLACKJACK!\n"
        start = f"\t\t\t\t{player.name} STARTS -> {player.score}\n"
        print(greeting)
        print(start)

    def start(self):
        if self.check_who_first() is self.player1:
            self.display_start(self.player1)
            self.player_turn(self.player1)
            self.player_turn(self.player2)
        else:
            self.display_start(self.player2)
            self.player_turn(self.player2)
            self.player_turn(self.player1)
        self.compare_score()
        

if __name__ == '__main__':
    game = Game()
    game.start()
