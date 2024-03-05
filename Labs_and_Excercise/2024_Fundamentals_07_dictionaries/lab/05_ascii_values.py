user_input = input().split(', ')
new_dictionary = {}

for letter in user_input:
    value = ord(letter)
    new_dictionary[letter] = value
print(new_dictionary)
