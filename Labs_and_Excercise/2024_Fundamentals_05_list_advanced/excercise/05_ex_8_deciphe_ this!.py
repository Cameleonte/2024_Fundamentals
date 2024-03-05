def swap_letters(current_word):
    first_letter = chr(int(''.join(x for x in current_word if x.isnumeric())))
    list_letters = [x for x in word if x.isalpha()]
    list_letters[0], list_letters[-1] = list_letters[-1], list_letters[0]
    word_list = [first_letter] + list_letters
    return word_list


secret_message = input().split()
result = []
for word in secret_message:
    result.append(''.join(swap_letters(word)))
print(' '.join(result))
