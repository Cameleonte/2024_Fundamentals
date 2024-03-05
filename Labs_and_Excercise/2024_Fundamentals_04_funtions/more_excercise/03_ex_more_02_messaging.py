numbers_sequence = input().split()
random_string = input()

string_list = list(random_string)
final_message = ''
for numbers in numbers_sequence:
    symbol_found = False
    symbol_counter = - 1
    current_seq_numbers_sum = 0
    for number in numbers:
        current_seq_numbers_sum += int(number)
    while not symbol_found:
        for symbol in string_list:
            symbol_counter += 1
            if symbol_counter == current_seq_numbers_sum:
                final_message += symbol
                string_list.remove(symbol)
                symbol_found = True
                break
print(final_message)
