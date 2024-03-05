def check_for_valentine(neighbours, index):
    if index + 1 > len(neighbours):
        index = 0
    if neighbours[index] > 0:
        neighbours[index] -= 2
        if neighbours[index] == 0:
            print(f'Place {index} has Valentine\'s day.')
    elif neighbours[index] == 0:
        print(f'Place {index} already had Valentine\'s day.')
    return index


neighbourhood = list(map(int, input().split('@')))

current_index = 0
while True:
    command = input()
    if command == 'Love!':
        print(f'Cupid\'s last position was {current_index}.')
        value_with_zero = neighbourhood.count(0)
        houses_without_valentine = len(neighbourhood) - value_with_zero
        if houses_without_valentine == 0:
            print('Mission was successful.')
        else:
            print(f'Cupid has failed {houses_without_valentine} places.')
        break
    else:
        if current_index > len(neighbourhood):
            current_index = 0
        jump_index = int(command.split(' ')[-1]) + current_index
        current_index = check_for_valentine(neighbourhood, jump_index)
        if jump_index == 0:
            current_index = 0
