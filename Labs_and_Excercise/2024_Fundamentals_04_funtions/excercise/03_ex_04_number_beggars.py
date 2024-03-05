string_beggars_income = input().split(', ')
beggars_number = int(input())

integer_income = []
for number in string_beggars_income:
    integer_income.append(int(number))
final_sums = []
start_index = 0
for current_beggar in range(1, beggars_number + 1):
    current_beggar_income = 0
    for index in range(start_index, len(integer_income), beggars_number):
        current_beggar_income += integer_income[index]
    final_sums.append(current_beggar_income)
    start_index += 1
print(final_sums)
