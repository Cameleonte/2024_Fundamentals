strings_number = int(input())
current_string = ''

for string in range(1, strings_number + 1):
    current_string = input()
    pure = False
    not_pure = False
    for symbol in range(len(current_string)):
        if current_string[symbol] != '_' and current_string[symbol] != '.' and current_string[symbol] != ',':
            pure = True
        else:
            not_pure = True
            pure = False
    if not_pure:
        print(f'{current_string} is not pure!')
    else:
        print(f'{current_string} is pure.')
