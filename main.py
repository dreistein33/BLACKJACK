import numpy as np
import random
import pandas as pd

deck = [
    {"card": "2", "count": 4, "points": 2},
    {"card": "3", "count": 4, "points": 3},
    {"card": "4", "count": 4, "points": 4},
    {"card": "5", "count": 4, "points": 5},
    {"card": "6", "count": 4, "points": 6},
    {"card": "7", "count": 4, "points": 7},
    {"card": "8", "count": 4, "points": 8},
    {"card": "9", "count": 4, "points": 9},
    {"card": "10", "count": 4, "points": 10},
    {"card": "Jack", "count": 4, "points": 10},
    {"card": "Queen", "count": 4, "points": 10},
    {"card": "King", "count": 4, "points": 10},
    {"card": "Ace", "count": 4, "points": (1, 11)}
]

# deck_df = pd.DataFrame(deck)


# def update_deck(player_set):
#     global deck_df
#     card_names = player_set.card
#     index_ = np.where(deck_df.card == card_names)
        
    
    
def distribute_cards(amount: int) -> list:
    player_set = random.choices(deck, k=amount)
    for items in player_set:
        items['count'] = 1
    return player_set


def its_ace():
    chosen_point = int(input('Do you want to choose 1 or 11?\n>>'))
    if chosen_point == 1:
        return 1
    elif chosen_point == 11:
        return 11
    else:
        print("Invalid point.")


def count_score(player_set: list) -> int:
    score = 0
    for items in player_set:
        if items['card'] != 'Ace':
            score += items['points']
        else:
            score += its_ace()
    return score


def game():
    p1_set = distribute_cards(amount=2)
    p2_set = distribute_cards(amount=2)
    p1_score = count_score(p1_set)
    p2_score = count_score(p2_set)
    who_first = random.choice(['p1', 'p2'])
    if who_first == 'p1':
        print("PLAYER 1 STARTS\n")
        while p1_score <= 21:
            keep_going = input("Do you want to take another card?\n>>").lower()
            if 'y' in keep_going:
                p1_set.append(distribute_cards(1))
                p1_score = count_score(p1_set)
                print(f"\nSCORE: {p1_score}")
            else:
                break
            if p1_score > 21:
                print(f"\nTHE GAME IS OVER\tPLAYER 1 WINS!")
    else:
        print("PLAYER 2 STARTS\n")
        while p2_score <= 21:
            keep_going = input("Do you want to take another card?\n>>").lower()
            if 'y' in keep_going:
                p2_set.append(distribute_cards(1))
                p2_score = count_score(p2_set)
                print(f"\nSCORE: {p2_score}")
            if p2_score > 21:
                print(f"\nTHE GAME IS OVER\tPLAYER 1 WINS!")
        


game()