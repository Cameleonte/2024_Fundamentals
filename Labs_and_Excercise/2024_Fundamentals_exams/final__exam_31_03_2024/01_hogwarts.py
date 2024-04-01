def abjuration(current_spell):
    current_spell = current_spell.upper()
    print(current_spell)
    return current_spell


def necromancy(current_spell):
    current_spell = current_spell.lower()
    print(current_spell)
    return current_spell


def illusion(data, current_spell):
    index, letter = data.split()[1], data.split()[2]
    new_spell = ''
    if int(index) not in range(len(current_spell)):
        print('The spell was too weak.')
    else:
        letter_list = list(current_spell)
        letter_list[int(index)] = letter
        new_spell = ''.join(letter_list)
        print('Done!')
    return new_spell


def divination(data, current_spell):
    first_substring, second_substring = data.split()[1], data.split()[2]
    if first_substring in current_spell:
        current_spell = current_spell.replace(first_substring, second_substring)
        print(current_spell)
    return current_spell


def alteration(data, current_spell):
    substring = data.split()[1]
    if substring in current_spell:
        current_spell = current_spell.replace(substring, '')
        print(current_spell)
    return current_spell


def main():
    initial_spell = input()
    command = input()
    while command != 'Abracadabra':
        action = command.split()[0]
        if action == 'Abjuration':
            initial_spell = abjuration(initial_spell)
        elif action == 'Necromancy':
            initial_spell = necromancy(initial_spell)
        elif action == 'Illusion':
            initial_spell = illusion(command, initial_spell)
        elif action == 'Divination':
            initial_spell = divination(command, initial_spell)
        elif action == 'Alteration':
            initial_spell = alteration(command, initial_spell)
        else:
            print('The spell did not work!')
        command = input()


if __name__ == "__main__":
    main()
