phrase = input().lower()
list_phrase = list(phrase)
new_word = ''
index = 0
counter = 0
while list_phrase[:]:
    if list_phrase[0] != 's' and list_phrase[0] != 'f' and list_phrase[0] != 'w':
        list_phrase.remove(list_phrase[0])
    else:
        if list_phrase[index] == 'h' and list_phrase[index + 1] == 's':
            list_phrase.remove(list_phrase[0])
        else:
            new_word += list_phrase[index]
            index += 1
    if new_word == 'sand' or new_word == 'sun' or new_word == 'water' or new_word == 'fish':
        counter += 1
        new_word = ''
        index = 0
        list_phrase.remove(list_phrase[0])
print(counter)

# gOfIshsunesunFiSh