user_input = input().split()

result_words = [x for x in user_input if len(x) % 2 == 0]
for word in result_words:
    print(word)
