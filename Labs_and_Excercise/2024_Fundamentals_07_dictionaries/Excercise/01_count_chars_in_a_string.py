user_input = input().split()

dicty = {}
for word in user_input:
    indexed_word = list(map(str, word))
    for letter in indexed_word:
        if letter not in dicty:
            dicty[letter] = 0
        dicty[letter] += 1
for letter, repetitive in dicty.items():
    print(f'{letter} -> {repetitive}')
