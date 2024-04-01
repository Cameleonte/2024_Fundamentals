def take_odd(init_password):
    letters_list = [init_password[i] for i in range(len(init_password)) if i % 2 != 0]
    raw_password = ''.join(letters_list)
    print(raw_password)
    return raw_password


def cut(init_password, order):
    unused_verb, index, length = order.split()
    removed_part = init_password[int(index): (int(index) + int(length))]
    raw_password = init_password.replace(removed_part, '', 1)
    print(raw_password)
    return raw_password


def substitute(init_password, order):
    unused_verb, substring, new_string = order.split()
    if substring in init_password:
        init_password = init_password.replace(substring, new_string)
        print(init_password)
    else:
        print('Nothing to replace!')
    return init_password


initial_string = input()

command = input()
while command != 'Done':
    if command == 'TakeOdd':
        initial_string = take_odd(initial_string)
    action = command.split()[0]
    if action == 'Cut':
        initial_string = cut(initial_string, command)
    elif action == 'Substitute':
        initial_string = substitute(initial_string, command)
    command = input()
print(f'Your password is: {initial_string}')
