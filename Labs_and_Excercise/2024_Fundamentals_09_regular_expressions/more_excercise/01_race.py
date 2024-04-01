import re


def find_names(participants):
    person_name_pattern = r"([a-zA-Z])"
    name_list = re.findall(person_name_pattern, info)
    name = ''.join(name_list)
    return name


def calculate_distance():
    numbers_pattern = r"\d"
    numbers = re.findall(numbers_pattern, info)
    distance = 0
    for current_number in numbers:
        distance += int(current_number)
    return distance


def winners(dictionary):
    sorted_by_values_list = sorted(dictionary.items(), key=lambda a: a[1], reverse=True)
    return sorted_by_values_list


def printing(final_list):
    finalists_list = [i for i, j in final_list]
    finalists_list = finalists_list[:3]
    return finalists_list


participants_list = input().split(', ')
participants_dict = {}

while True:
    info = input()
    if info == 'end of race':
        sorted_list = winners(participants_dict)
        list_to_print = printing(sorted_list)
        print(f'1st place: {list_to_print[0]}\n2nd place: {list_to_print[1]}\n3rd place: {list_to_print[2]}')
        break
    some_name = find_names(participants_list)
    if some_name in participants_list:
        tot_distance = calculate_distance()
        if some_name in participants_dict.keys():
            participants_dict[some_name] += tot_distance
        else:
            participants_dict[some_name] = tot_distance
