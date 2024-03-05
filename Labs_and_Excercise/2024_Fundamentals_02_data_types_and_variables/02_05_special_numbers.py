user_number = int(input())

for number in range(1, user_number + 1):
    number = str(number)
    sum_digits = 0
    for digit in range(len(number)):
        sum_digits += int(number[digit])
    is_special = False
    if sum_digits == 5 or sum_digits == 7 or sum_digits == 11:
        is_special = True
    print(f'{number} -> {is_special}')
