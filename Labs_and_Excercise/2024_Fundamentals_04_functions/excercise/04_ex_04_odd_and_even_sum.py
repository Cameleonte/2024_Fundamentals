def sum_digits(number):
    sum_even_digits = 0
    sum_odd_digits = 0

    for digit in str(number):
        if int(digit) % 2 == 0:
            sum_even_digits += int(digit)
        else:
            sum_odd_digits += int(digit)
    return f'Odd sum = {sum_odd_digits}, Even sum = {sum_even_digits}'


user_number = int(input())
print(sum_digits(user_number))
