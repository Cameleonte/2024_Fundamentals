initial_char_number = int(input())
final_char_number = int(input())

for character in range(initial_char_number, final_char_number + 1):
    print(f'{chr(character)}', end=' ')
