def min_number(my_list):
    return min(my_list)


def max_number(my_list):
    return max(my_list)


def sum_numbers(my_list):
    return sum(my_number_list)


user_input = input().split()
my_number_list = []
for digit in user_input:
    my_number_list.append(int(digit))
minimum_number = min_number(my_number_list)
maximum_number = max_number(my_number_list)
tot_sum = sum_numbers(my_number_list)

print(f'The minimum number is {minimum_number}')
print(f'The maximum number is {maximum_number}')
print(f'The sum number is: {tot_sum}')
