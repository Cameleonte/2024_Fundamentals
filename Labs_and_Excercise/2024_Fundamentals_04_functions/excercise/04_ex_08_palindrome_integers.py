def check_palindrome(my_list):
    result = ''

    for index in my_list:
        if index == index[::-1]:
            result += 'True\n'
        else:
            result += 'False\n'

    return result


user_input = input().split(', ')
print(check_palindrome(user_input))
