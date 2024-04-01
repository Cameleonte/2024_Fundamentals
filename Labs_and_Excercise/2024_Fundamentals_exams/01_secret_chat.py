def reverse_case(frase, message):
    substring = frase.split(':|:')[1]
    if substring in message:
        new_message = message.replace(substring, '', 1)
        rev_frase = substring[::-1]
        new_message = new_message + rev_frase
        print(new_message)
        return new_message
    else:
        print('error')
        return message


def change_case(frase, message):
    substring = frase.split(':|:')[1]
    replacement = frase.split(':|:')[2]
    new_message = message.replace(substring, replacement)
    print(new_message)
    return new_message


def insert_case(frase, message):
    index = frase.split(':|:')[1]
    message = message[:int(index)] + ' ' + message[int(index):]
    print(message)
    return message


def main(message):
    command = input()
    while command != 'Reveal':
        action = command.split(':|:')[0]
        if action == 'Reverse':
            message = reverse_case(command, message)
        if action == 'ChangeAll':
            message = change_case(command, message)
        if action == 'InsertSpace':
            message = insert_case(command, message)
        command = input()
    return message


initial_message = input()
final_message = main(initial_message)
print(f'You have a new text message: {final_message}')
