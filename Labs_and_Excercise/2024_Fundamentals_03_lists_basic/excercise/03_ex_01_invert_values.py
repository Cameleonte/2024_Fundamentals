initial_string = input().split(' ')
my_list = []

for digit in initial_string:
    digit = -int(digit)
    my_list.append(digit)
print(my_list)
