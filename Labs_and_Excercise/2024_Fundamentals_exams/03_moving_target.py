def validation(numbers_sequence):
    return 0 <= index < len(numbers_sequence)


def action_shoot(numbers_sequence):
    if validation(numbers_sequence):
        numbers_sequence[index] -= value
        if numbers_sequence[index] <= 0:
            numbers_sequence.pop(index)
    return numbers_sequence


def action_add(numbers_sequence):
    if validation(numbers_sequence):
        numbers_sequence.insert(index, value)
    else:
        print('Invalid placement!')
    return numbers_sequence


def action_strike(numbers_sequence):
    if validation(numbers_sequence):
        if 0 <= index - value < len(numbers_sequence) and 0 <= index + value < len(numbers_sequence):
            list1 = numbers_sequence[:index - value]
            list2 = numbers_sequence[index + value + 1:]
            numbers_sequence = list1 + list2
        else:
            print('Strike missed!')
    return numbers_sequence


def main_func(targets):
    action = command[0]
    if action == 'Shoot':
        action_shoot(targets)
    elif action == 'Add':
        action_add(targets)
    elif action == 'Strike':
        targets = action_strike(targets)
    return targets


targets_sequence = list(map(int, input().split()))

while True:
    command = input().split()
    if command[0] == 'End':
        result = '|'.join(map(str, targets_sequence))
        print(result)
        break

    index, value = int(command[1]), int(command[2])
    targets_sequence = main_func(targets_sequence)
