user_string = input()
counter = int(input())

repeat_string = lambda m, n: m * n
result = repeat_string(user_string, counter)
print(result)
