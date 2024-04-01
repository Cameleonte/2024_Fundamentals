def operations(num1, num2, operator):
    result = None
    if operator == 'multiply':
        result = num1 * num2
    elif operator == 'divide':
        if num2 != 0:
            result = num1 / num2
    elif operator == 'add':
        result = num1 + num2
    elif operator == 'subtract':
        result = num1 - num2
    return int(result)


user_operator = input()
first_number = int(input())
second_number = int(input())
print(operations(first_number, second_number, user_operator))
