user_input = input().split()

new_dictionary = {}
for item in user_input:
    item = item.lower()
    if item in new_dictionary:
        new_dictionary[item] += 1
    else:
        new_dictionary[item] = 1
for current_key, current_value in new_dictionary.items():
    if current_value % 2 != 0:
        print(current_key, end=' ')
