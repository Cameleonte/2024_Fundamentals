def sum_numbers(a, b):
    return a + b


def subtract(result, c):
    return result - c


def add_and_subtract(a, b, c):
    result = sum_numbers(a, b)
    return subtract(result, c)


first_num, second_num, third_num = int(input()), int(input()), int(input())
print(add_and_subtract(first_num, second_num, third_num))
