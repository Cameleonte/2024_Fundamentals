user_input = int(input())

for num in range(user_input):
    for num1 in range(user_input):
        for num2 in range(user_input):
            print(f'{chr(num + 97)}{chr(num1 + 97)}{chr(num2 + 97)}')
