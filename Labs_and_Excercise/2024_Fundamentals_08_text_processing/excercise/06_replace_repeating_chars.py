input_string = input()
previous_symbol = ''
new_string = ''
for symbol in input_string:
    if symbol != previous_symbol:
        new_string += symbol
        previous_symbol = symbol

print(new_string)
