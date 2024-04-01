user_input = input().split()
numbers_list = []
for digit in user_input:
    numbers_list.append(int(digit))
a = sorted(numbers_list)
print(a)
