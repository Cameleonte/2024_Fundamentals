banned_words = input().split(', ')
some_text = input()

for word in banned_words:
    while word in some_text:
        replace_word = len(word) * '*'
        some_text = some_text.replace(word, replace_word)
print(some_text)
