# user_numbers = list(map(int, input().split(', ')))
#
# check_for_even_or_no = map(lambda x: x if user_numbers[x] % 2 == 0 else 'no', range(len(user_numbers)))
# searched_result = list(filter(lambda z: z != 'no', check_for_even_or_no))
# print(searched_result)

#100

user_numbers = input().split(', ')

even_numbers_indexes = []
for string in user_numbers:
    if int(string) % 2 == 0:
        even_numbers_indexes.append(user_numbers.index(string))

print(even_numbers_indexes)

# ev_num_ind = list(user_numbers.index(string) for string in user_numbers if int(string) % 2 == 0)
# print(ev_num_ind)
#80