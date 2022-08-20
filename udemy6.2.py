# Duplets

def calc_dice_scores(list):
    return sum([a + b for a, b in list]) if not any([a == b for a, b in list]) else 0

print(calc_dice_scores([(1, 2), (3, 4), (5, 6)]))
print(calc_dice_scores([(4, 5), (4, 5), (4, 5)]))