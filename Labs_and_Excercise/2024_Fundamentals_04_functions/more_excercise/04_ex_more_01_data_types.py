def input_type(string, number):
    if string == 'int':
        number = 2 * int(number)
    elif string == 'real':
        number = 1.5 * float(number)
        number = f'{number:.2f}'
    elif string == 'string':
        number = f'${number}$'
    return number


first_string = input()
second_string = input()
result = input_type(first_string, second_string)
print(result)
