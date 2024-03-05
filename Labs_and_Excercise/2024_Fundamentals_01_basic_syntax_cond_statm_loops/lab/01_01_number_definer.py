user_number = float(input())

if user_number == 0:
    print('zero')
elif user_number < 0:
    if abs(user_number) < 1:
        print('small negative')
    elif abs(user_number) > 1000000:
        print('large negative')
    else:
        print('negative')
elif user_number > 0:
    if abs(user_number) < 1:
        print('small positive')
    elif user_number > 1000000:
        print('large positive')
    else:
        print('positive')
