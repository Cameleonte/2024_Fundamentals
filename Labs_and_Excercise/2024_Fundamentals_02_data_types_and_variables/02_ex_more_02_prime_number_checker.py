user_number = int(input())
result = False
special_number = False
for number1 in range(1, user_number):
    for number2 in range(1, user_number):
        if number1 * number2 == user_number or number2 * number2 == user_number:
            result = False
            special_number = True
            break
        else:
            result = True
    if special_number:
        break
print(result)
