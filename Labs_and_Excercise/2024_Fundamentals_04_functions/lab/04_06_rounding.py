# user_input = input().split()
# new_list = []
# for number in user_input:
#     new_list.append(round(float(number)))
# print(new_list)


def rounded_numbers(current_number):
    return round(current_number)


user_input = input().split()
new_list = []
for number in user_input:
    new_list.append(rounded_numbers(float(number)))
print(new_list)
