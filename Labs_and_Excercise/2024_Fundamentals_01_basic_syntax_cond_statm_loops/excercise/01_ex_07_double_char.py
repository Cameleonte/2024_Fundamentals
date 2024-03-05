command = input()
current_string = ''

while command != 'End':
    current_string = command
    if current_string != 'SoftUni':
        for char in range(len(current_string)):
            print(current_string[char], end='')
            print(current_string[char], end='')
        print()
    command = input()
