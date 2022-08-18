# Chinese stick game

sticks_count = 10
player_turn = 1
while sticks_count > 0:
    print(f'Take sticks, sticks availeble {sticks_count}')
    taken = int(input())
    if taken < 1 or taken > 3:
        print(f'Please, take anouther count of sticks, {taken} is too much. Take 1, 2 or 3 sticks')
        continue
    sticks_count -= taken
    print(f'Sticks taken: {taken}\n')
    if sticks_count <= 0:
        print(f'No more sticks in game. \nPlayer {player_turn} loose')
    player_turn = 1 if player_turn == 2 else 2