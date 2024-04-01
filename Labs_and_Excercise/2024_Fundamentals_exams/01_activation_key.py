def check_contain(string, command):
    substring = command[1]
    if substring in string:
        print(f'{string} contains {substring}')
    else:
        print('Substring not found!')


def flip(string, command):
    changing_mode = command[1]
    start_index = int(command[2])
    end_index = int(command[3])
    letters_to_change = string[start_index: end_index]
    if changing_mode == "Upper":
        letters_to_change = letters_to_change.upper()
    elif changing_mode == 'Lower':
        letters_to_change = letters_to_change.lower()
    new_string = string[:start_index] + letters_to_change + string[end_index:]
    print(new_string)
    return new_string


def slice_func(string, command):
    start_index = int(command[1])
    end_index = int(command[2])
    new_string = string[:start_index] + string[end_index:]
    print(new_string)
    return new_string


def main(current_key):
    instructions = input()
    while instructions != "Generate":
        instructions = instructions.split('>>>')
        action = instructions[0]
        if action == 'Contains':
            check_contain(current_key, instructions)
        elif action == 'Flip':
            current_key = flip(current_key, instructions)
        elif action == 'Slice':
            current_key = slice_func(current_key, instructions)
        instructions = input()
    return current_key


raw_key = input()
final_key = main(raw_key)
print(f'Your activation key is: {final_key}')
