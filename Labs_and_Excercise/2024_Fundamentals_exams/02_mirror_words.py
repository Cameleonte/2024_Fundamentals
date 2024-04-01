import re

initial_string = input()
pattern = r'([@#])([A-Za-z]{3,})\1\1([a-zA-Z]{3,})\1'
valid_words_list = []
result = re.finditer(pattern, initial_string)

for element in result:
    current_word = element.group(2)
    pair_word = element.group(3)
    valid_words_list.append((current_word, pair_word))

if not valid_words_list:
    print('No word pairs found!')
else:
    print(f'{len(valid_words_list)} word pairs found!')

pair_list = []
pairs = False
for pair in valid_words_list:
    if pair[0] == pair[1][::-1]:
        pairs = True
        pair_list.append((pair[0], pair[1]))
if pairs:
    print(f'The mirror words are:')
    for element in pair_list:
        if pair_list[-1] == element:
            print(f'{element[0]} <=> {element[1]}')
            break
        print(f'{element[0]} <=> {element[1]}', end=', ')
else:
    print('No mirror words!')
