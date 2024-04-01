lines_number = int(input())
my_list = []
balanced = True

for current_input in range(lines_number):
    user_input = input()
    if user_input != '(' and user_input != ')':
        continue
    else:
        my_list += user_input
        if len(my_list) != 1:
            if my_list[0] == '(' and user_input == '(':
                balanced = False
                break
        else:
            if my_list[0] == ')':
                my_list = []
                balanced = False
                break
        if len(my_list) == 2:
            my_list = []
            balanced = True
if not balanced:
    print('UNBALANCED')
else:
    print('BALANCED')
