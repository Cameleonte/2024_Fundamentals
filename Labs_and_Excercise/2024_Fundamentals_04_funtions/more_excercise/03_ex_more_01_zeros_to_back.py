single_string = input().split(', ')

integer_list = []
zero_counter = 0
for index in single_string:
    integer_list.append(int(index))
for number in integer_list:
    if number == 0:
        integer_list.remove(0)
        integer_list.append(0)
print(integer_list)
