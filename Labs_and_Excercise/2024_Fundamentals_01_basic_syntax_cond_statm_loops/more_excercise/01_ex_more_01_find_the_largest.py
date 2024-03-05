number = int(input())
number_str = str(number)
my_list = []
result = ''
for digit in number_str:
    my_list += digit
list.sort(my_list)
list.reverse(my_list)
for digit in my_list:
    result += digit
print(result)
