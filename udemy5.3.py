# Poker combination
table_cards = ["A_S", "J_H", "7_D", "8_D", "10_D"], ["J_D", "3_D"]
hand_cards = ["3_D", "3_D"]

table_suites = [i[-1] for i in table_cards]
hand_suites = [i[-1] for i in hand_cards]

suites_in_game = table_suites + hand_suites

#list comprehension
# flush = any([suites_in_game.count(suit) >=5 for suit in "CHSD"])
flush = False
for suit in "CHSD":
    if suites_in_game. count(suit) >= 5:
        flush = True
if flush:
    print("Flush")
else:
    print("No flush")




