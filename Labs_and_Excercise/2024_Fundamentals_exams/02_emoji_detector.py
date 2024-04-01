import re
from functools import reduce


def regex(string):
    new_list = []
    string = string.split()
    for word in string:
        if '*' in word or ':' in word:
            pattern = r'(([:]{2}|[*]{2})([A-Z][a-z]{2,})\2)'
            found_emojis = re.findall(pattern, word)
            for elem in found_emojis:
                new_list.append(elem[0])
    return new_list


def cool_threshold():
    multiply_nums_list = []
    for symbol in initial_input:
        if symbol.isdigit():
            multiply_nums_list.append(int(symbol))
    result = reduce((lambda a, b: a * b), multiply_nums_list)
    return result


def calculate_valid_emojis(threshold, mylist):
    valid_emojis_lst = []
    for emoji in mylist:
        current_ascii_sum = 0
        for letter in emoji:
            if letter.isalpha():
                current_ascii_sum += ord(letter)
        if current_ascii_sum >= threshold:
            valid_emojis_lst.append(emoji)
    return valid_emojis_lst


def print_function(threshold, all_emojis, valid_emos):
    print(f'Cool threshold: {threshold}')
    print(f'{len(all_emojis)} emojis found in the text. The cool ones are:')
    for valid_emoji in valid_emos:
        print(valid_emoji)


initial_input = input()
value_threshold = cool_threshold()
emojis_list = regex(initial_input)
valid_emojis_list = calculate_valid_emojis(value_threshold, emojis_list)
print_function(value_threshold, emojis_list, valid_emojis_list)
