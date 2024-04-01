user_input = input().split()
result = 0

for sequence in user_input:
    first_letter = sequence[0]
    last_letter = sequence[-1]
    current_number = int(sequence[1: len(sequence) - 1])
    if first_letter.isupper():
        first_position = ord(first_letter) - 64
        result += current_number / first_position
    elif first_letter.islower():
        first_position = ord(first_letter) - 96
        result += current_number * first_position
    if last_letter.isupper():
        last_position = ord(last_letter) - 64
        result -= last_position
    elif last_letter.islower():
        last_position = ord(last_letter) - 96
        result += last_position

print(f'{result:.2f}')
