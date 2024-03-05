gifts_names = input().split()

command = input()
while command != 'No Money':
    command = command.split()
    replace_index = 0
    for current_gift in gifts_names:
        if 'OutOfStock' in command and command[1] in gifts_names:
            if replace_index == gifts_names.index(command[1]):
                gifts_names.remove(command[1])
                gifts_names.insert(replace_index, 'None')
        elif 'Required' in command:
            if 0 < int(command[2]) < len(gifts_names):
                gifts_names.pop(int(command[2]))
                gifts_names.insert(int(command[2]), command[1])
                break
        elif 'JustInCase' in command:
            gifts_names.pop()
            gifts_names.append(command[1])
            break
        replace_index += 1
    command = input()
for word in gifts_names:
    if 'None' in gifts_names:
        gifts_names.remove('None')
print(*gifts_names, sep=' ')
