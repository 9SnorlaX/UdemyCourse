# Named func
sticks_count = 10
player_turn = 1
def can_take(sticks):
    return sticks >= 1 and sticks <= 3
def switch_player_turn(turn):
    return 1 if player_turn == 2 else 2
def end_game(sticks):
    return sticks_count <= 0
while (not end_game(sticks_count)):
    print(f'How many sticks u take? Remaining {sticks_count}')
    taken = int(input())
    if not can_take(taken):
        print(f'Please, take anouther count of sticks, {taken} is too much. Take 1, 2 or 3 sticks')
        continue
    sticks_count -= taken
    print(f'Sticks taken: {taken}\n')
    if sticks_count <= 0:
        print(f'No more sticks in game. \nPlayer {player_turn} loose')
        break

    player_turn = switch_player_turn(player_turn)
