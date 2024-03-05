lines_number = int(input())

result_list = []
final_list = []
for line in range(lines_number):
    current_number = int(input())
    result_list.append(current_number)
command = input()
for value in result_list:
    if command == 'odd' and value % 2 != 0:
        final_list.append(value)
    if command == 'even' and value % 2 == 0:
        final_list.append(value)
    if command == 'positive' and value >= 0:
        final_list.append(value)
    if command == 'negative' and value < 0:
        final_list.append(value)
print(final_list)

'''
lines_number = int(input())

even_numbers_list = []
odd_numbers_list = []
positive_numbers_list = []
negative_numbers_list = []

for num in range(lines_number):
    current_number = int(input())
    if current_number % 2 == 0:
        even_numbers_list.append(current_number)
    else:
        odd_numbers_list.append(current_number)
    if current_number >= 0:
        positive_numbers_list.append(current_number)
    else:
        negative_numbers_list.append(current_number)

command = input()
if command == 'even':
    print(even_numbers_list)
elif command == 'odd':
    print(odd_numbers_list)
elif command == 'positive':
    print(positive_numbers_list)
elif command == 'negative':
    print(negative_numbers_list)
'''
