explosion_string = input()
final_string = ''
strength = 0

for index in range(len(explosion_string)):
    if explosion_string[index] == '>':
        final_string += explosion_string[index]
        strength += int(explosion_string[index + 1])
    elif strength > 0 and explosion_string[index] != '>':
        strength -= 1
    else:
        final_string += explosion_string[index]

print(final_string)
