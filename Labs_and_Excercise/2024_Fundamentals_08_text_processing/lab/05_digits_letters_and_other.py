random_string = input()
digits = ''
letters = ''
symbols = ''

for character in random_string:
    if character.isdigit():
        digits += character
    elif character.isalpha():
        letters += character
    else:
        symbols += character
print(f'{digits}\n{letters}\n{symbols}')
