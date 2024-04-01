def my_function(digit):
    if int(digit) % 2 == 0:
        return True
    else:
        return False


user_numbers = input().split()
even_numbers = filter(my_function, user_numbers)
my_list = []

for x in even_numbers:
    my_list.append(int(x))
print(my_list)
