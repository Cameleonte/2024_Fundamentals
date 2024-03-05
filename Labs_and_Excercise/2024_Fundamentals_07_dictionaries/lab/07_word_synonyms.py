word_numbers = int(input())

new_dictionary = {}
for i in range(word_numbers):
    key = input()
    value = input()
    if key not in new_dictionary:
        new_dictionary[key] = [value]
    else:
        new_dictionary[key] += [value]
for key, value in new_dictionary.items():
    synonyms = ', '.join(value)
    print(f'{key} - {synonyms}')
