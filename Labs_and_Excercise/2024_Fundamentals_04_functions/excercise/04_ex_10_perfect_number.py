def perf_num(number):
    is_perfect = False
    divisors_sum = 0
    for num in range(1, number):
        if number % num == 0:
            divisors_sum += num
    if divisors_sum == number:
        is_perfect = True
    if is_perfect:
        return 'We have a perfect number!'
    else:
        return 'It\'s not so perfect.'


user_number = int(input())
result = perf_num(user_number)
print(result)
