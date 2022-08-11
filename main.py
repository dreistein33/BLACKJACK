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

deck_df = pd.DataFrame(deck)
print(deck_df['card'])


def update_deck(player_set):
    global deck_df
    if player_set['card'] == deck_df['card']:
        deck_df['count'] = deck_df['count'] - player_set['count']
    
    
def distribute_cards(amount):
    player_set = random.choices(deck, k=amount)
    for items in player_set:
        items['count'] = 1
    return pd.DataFrame(player_set)

