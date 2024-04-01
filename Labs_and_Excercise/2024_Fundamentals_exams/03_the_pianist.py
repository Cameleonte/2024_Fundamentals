def change_func(pieces_dict, piece, new_key):
    if check_function(pieces_dict, piece):
        new_list = list(pieces_dict[piece])
        new_list[1] = new_key
        new_list = tuple(new_list)
        pieces_dict.update({piece: new_list})
        print(f'Changed the key of {piece} to {new_key}!')
    else:
        print(f'Invalid operation! {piece} does not exist in the collection.')


def remove_func(pieces_dict, piece):
    if check_function(pieces_dict, piece):
        del pieces_dict[piece]
        print(f'Successfully removed {piece}!')
    else:
        print(f'Invalid operation! {piece} does not exist in the collection.')


def add_func(pieces_dict, piece, composer, key):
    if check_function(pieces_dict, piece):
        print(f'{piece} is already in the collection!')
    else:
        pieces_dict.update({piece: [composer, key]})
        print(f'{piece} by {composer} in {key} added to the collection!')


def check_function(information, song):
    if song in information:
        return True
    return False


def final_print(info):
    for piece in info.keys():
        for _ in info:
            composer, key = info[piece][0], info[piece][1]
            print(f'{piece} -> Composer: {composer}, Key: {key}')
            break


def command_function(collection):
    while True:
        command = input()
        if command == 'Stop':
            final_print(collection)
            break
        initial_split = command.split('|')
        action, piece = initial_split[0], initial_split[1]
        if action == 'Add':
            composer, key = initial_split[2], initial_split[3]
            add_func(collection, piece, composer, key)
        elif action == 'Remove':
            remove_func(collection, piece)
        elif action == 'ChangeKey':
            new_key = initial_split[2]
            change_func(collection, piece, new_key)


def main_function():
    pieces_dictionary = {}
    for current_piece in range(1, initial_pieces + 1):
        piece, composer, key = input().split('|')
        pieces_dictionary[piece] = composer, key
    command_function(pieces_dictionary)


initial_pieces = int(input())
main_function()
