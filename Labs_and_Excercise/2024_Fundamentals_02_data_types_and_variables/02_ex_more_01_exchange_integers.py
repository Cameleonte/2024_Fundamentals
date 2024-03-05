first_number = int(input())
second_number = int(input())
print(f'Before:\na = {first_number}\nb = {second_number}')
new_integer = second_number
second_number = first_number
first_number = new_integer
print(f'After:\na = {first_number}\nb = {second_number}')
