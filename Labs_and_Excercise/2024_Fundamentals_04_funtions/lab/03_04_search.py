lines_number = int(input())
word = input()
words_list = []
list_without_word = []

for number in range(lines_number):
    current_string = input()
    words_list.append(current_string)
    if word in current_string:
        list_without_word.append(current_string)

print(words_list)
print(list_without_word)
