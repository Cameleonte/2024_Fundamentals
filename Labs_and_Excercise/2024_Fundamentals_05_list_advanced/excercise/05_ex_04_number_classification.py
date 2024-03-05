numbers_sequence = input().split(', ')

even_numbers = ', '.join([x for x in numbers_sequence if int(x) % 2 == 0])
odd_numbers = ', '.join([x for x in numbers_sequence if int(x) % 2 != 0])
positive_numbers = ', '.join([x for x in numbers_sequence if int(x) >= 0])
negative_numbers = ', '.join([x for x in numbers_sequence if int(x) < 0])

print(f'Positive: {positive_numbers}')
print(f'Negative: {negative_numbers}')
print(f'Even: {even_numbers}')
print(f'Odd: {odd_numbers}')
