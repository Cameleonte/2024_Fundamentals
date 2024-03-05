def check_indexes(user_list, ind_list, non_valid_input, move):
    for value in ind_list:
        if (0 > int(value) or int(value) > len(user_list) - 1) or len(set(ind_list)) == 1:
            user_list.insert(int(len(user_list) / 2), f'-{move}a')
            user_list.insert(int(len(user_list) / 2), f'-{move}a')
            print('Invalid input! Adding additional elements to the board')
            non_valid_input = True
            break
    return non_valid_input


def checks_found_element(user_list1, indexes_list1):
    if user_list1[int(indexes_list1[0])] == user_list1[int(indexes_list1[1])]:
        symbol = user_list1[int(indexes_list1[0])]
        print(f'Congrats! You have found matching elements - {symbol}!')
        for index in range(len(indexes_list1)):
            command.remove(symbol)
    else:
        print('Try again!')
    return user_list1


def check_equal_pair(user_list, indexes_list):
    current_move = 0
    while indexes_list != ['end']:
        current_move += 1
        invalid_input = False
        invalid_input = check_indexes(command, indexes_list, invalid_input, current_move)
        if invalid_input:
            indexes_list = input().split()
            continue
        checks_found_element(user_list, indexes_list)
        if len(user_list) == 0:
            print(f'You have won in {current_move} turns!')
            break
        indexes_list = input().split()
    return user_list


command = input().split()
list_indexes = input().split()

command = check_equal_pair(command, list_indexes)
if len(command) != 0:
    print('Sorry you lose :(')
    print(*command)
