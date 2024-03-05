user_number = int(input())

for rows in range(1, user_number + 1):
    for columns in range(1, user_number + 1):
        if columns > rows:
            break
        print('*', end='')
    print()
for rows in range(1, user_number):
    for columns in range(user_number, 1, - 1):
        if rows >= columns:
            break
        print('*', end='')
    print()
