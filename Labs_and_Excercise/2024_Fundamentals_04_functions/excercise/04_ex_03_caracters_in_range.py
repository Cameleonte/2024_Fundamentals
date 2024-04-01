def char_in_range(symbol1, symbol2):
    result = ''
    for current_number in range(ord(symbol1) + 1, ord(symbol2)):
        result += chr(current_number) + ' '
    return result


first_symbol = input()
second_symbol = input()
print(char_in_range(first_symbol, second_symbol))
