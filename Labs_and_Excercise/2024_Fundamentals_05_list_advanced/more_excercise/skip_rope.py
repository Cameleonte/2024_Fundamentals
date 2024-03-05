def creating_new_list(non_number_list):
    result_list = []
    begin_slicing = 0
    skip_index = 0
    for take_num in take_list:
        end_slicing = begin_slicing + take_num
        result_list += non_number_list[begin_slicing:end_slicing]
        begin_slicing = end_slicing + skip_list[skip_index]
        skip_index += 1
    return result_list


def dividing_numbers(my_list):
    first_list = []
    second_list = []
    for index in range(len(my_list)):
        if index % 2 == 0:
            first_list.append(my_list[index])
        else:
            second_list.append(my_list[index])
    return first_list, second_list


initial_string = input()

numbers_string = list(map(int, (x for x in initial_string if x.isnumeric())))
take_list, skip_list = dividing_numbers(numbers_string)
symbols_string = [x for x in initial_string if not x.isnumeric()]
final_list = ''.join(creating_new_list(symbols_string))
print(final_list)
