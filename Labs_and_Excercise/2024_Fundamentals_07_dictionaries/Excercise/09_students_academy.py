def check_vote():
    for name, x_list in dictionary.items():
        average_vote = x_list[0] / x_list[1]
        if average_vote >= 4.50:
            print_dictionary[name] = average_vote


def add_student():
    if students_name not in dictionary:
        dictionary[students_name] = [grade, 1]
    else:
        dictionary[students_name][0] += grade
        dictionary[students_name][1] += 1


couples_number = int(input())
dictionary = {}
print_dictionary = {}

for num in range(couples_number):
    students_name = input()
    grade = float(input())
    add_student()

check_vote()
for pearson, vote in print_dictionary.items():
    print(f'{pearson} -> {vote:.2f}')
