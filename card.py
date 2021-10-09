import random, pandas as pd, numpy as np

deck = []
CARDS_ON_HAND = 7
TRY_TIMES = 1000

# for alphabet in ['A','B','C','D','E','F','G']:
#     for i in range(1,5):
#         list.append(alphabet + str(i))
# dict = {}
# for i in list:
#     dict[i] = 0

dict = {'A1': 3, 'A2': 3, 'A3': 5, 'A4': 3, 'B1': 6, 'B2': 5, 'B3':5, 'B4': 5, 'C1': 5, 'C2': 5, 'C3': 4, 'C4': 20, 'D1': 5, 'D2': 5, 'D3': 5, 'D4': 4, 'E1': 5, 'E2': 3, 'E3': 5, 'E4': 5, 'F1': 4, 'F2': 5, 'F3': 3, 'F4': 3, 'G1': 4, 'G2': 4, 'G3': 4, 'G4': 3}
TOTAL_CARD = sum(dict.values())
print(TOTAL_CARD)

for i in dict:
    for cards_of_each in range (0, dict[i]):
        deck.append(i)

deck_current = deck.copy()

df = pd.DataFrame()
for TRY_TIME in range(0,TRY_TIMES):
    current_deck = TOTAL_CARD
    PLAYERS = {'1':{},'2':{},'3':{},'4':{}}
    deck_current = deck.copy()

    for time in range(0,CARDS_ON_HAND):
        for player in PLAYERS:
            y = random.randint(0,current_deck)
            card = deck_current.pop(y-1)
            current_deck = current_deck -1
            PLAYERS[player][time] = card


    df_player = pd.DataFrame.from_dict(PLAYERS, orient='index').reset_index() 
    df = df.append(df_player, ignore_index=True)
print('df', df)

g = df.apply(pd.value_counts).drop('index', axis=1)
g = g.drop(labels=['1','2','3','4'], axis=0)
g['sum'] = g[list(g.columns)].sum(axis=1)
print(g)
print(g / len(df))