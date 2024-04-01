gamers_string = input()
rage_string = ''
series_string = ''
next_symbols = ''

for index in range(len(gamers_string)):
    if not gamers_string[index].isdigit():
        series_string += gamers_string[index].upper()
    else:
        for next_index in range(index, len(gamers_string)):
            if not gamers_string[next_index].isdigit():
                break
            next_symbols += gamers_string[next_index]
        rage_string += series_string * int(next_symbols)
        series_string = ''
        next_symbols = ''

unique_symbols = len(set(rage_string))

print(f'Unique symbols used: {unique_symbols}\n{rage_string}')
