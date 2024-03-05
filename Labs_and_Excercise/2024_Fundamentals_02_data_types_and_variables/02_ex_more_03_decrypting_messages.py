user_key = int(input())
lines_number = int(input())
new_word = ''
for current_number in range(1, lines_number + 1):
    current_letter = input()
    int_letter = ord(current_letter)
    new_letter = int_letter + user_key
    new_current_letter = chr(new_letter)
    new_word += new_current_letter
print(new_word)
