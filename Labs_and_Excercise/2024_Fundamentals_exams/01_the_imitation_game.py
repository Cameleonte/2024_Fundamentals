def check(message):
    return 0 <= index <= len(message)


def act_move(message):
    if check(message):
        list_to_back = message[:index]
        list_to_front = message[index:]
        message = list_to_front + list_to_back
        return message


def act_insert(action, message):
    if check(message):
        if len(action[2]) > 1:
            list_message = ''.join(map(str, message))
            new_list = list_message[:index] + action[2] + list_message[index:]
            message = list(map(str, new_list))
        else:
            message.insert(index, action[2])
    return message


def act_change(action, message):
    for letter in message:
        if letter == action[1]:
            indexes = message.index(letter)
            message.remove(letter)
            message.insert(indexes, action[2])
    return message


encrypted_message = list(map(str, input()))

while True:
    instructions = input().split('|')
    if instructions[0] == 'Decode':
        decrypted_message = ''.join(map(str, encrypted_message))
        print(f'The decrypted message is: {decrypted_message}')
        break

    if instructions[0] == 'ChangeAll':
        act_change(instructions, encrypted_message)
    else:
        index = int(instructions[1])
        if instructions[0] == 'Move':
            encrypted_message = act_move(encrypted_message)
        elif instructions[0] == 'Insert':
            encrypted_message = act_insert(instructions, encrypted_message)
