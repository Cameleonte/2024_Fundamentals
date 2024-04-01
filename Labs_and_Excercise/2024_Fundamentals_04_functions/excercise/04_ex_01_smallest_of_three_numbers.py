def smallest_number(num1, num2, num3):
    return min(num1, num2, num3)


user_number1 = int(input())
user_number2 = int(input())
user_number3 = int(input())
result = smallest_number(user_number1, user_number2, user_number3)
print(result)
