words_input = input().split()
palindrome_input = input()

palindrome_list = []
palindrome_coincidence = 0
for word in range(len(words_input)):
    reversed_word = words_input[word][::-1]
    if words_input[word] == reversed_word:
        palindrome_list.append(reversed_word)
        if reversed_word == palindrome_input:
            palindrome_coincidence += 1

print(palindrome_list)
print(f'Found palindrome {palindrome_coincidence} times')
