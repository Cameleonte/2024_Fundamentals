user_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(user_list)

user_list.sort(key=lambda a: a % 2 == 0)
print(user_list)
