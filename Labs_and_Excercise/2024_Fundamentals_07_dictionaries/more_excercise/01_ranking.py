def filtering(submissions):
    alfa_filtered_dict = dict(sorted(submissions.items(), key=lambda a: a[0]))

    for student in alfa_filtered_dict.keys():
        print(student)
        current_students_dictionary = submissions[student]
        value_filtered_list = list(sorted(current_students_dictionary.items(), key=lambda b: b[1], reverse=True))
        for index in range(len(value_filtered_list)):
            key, value = value_filtered_list[index][0], value_filtered_list[index][1]
            print(f'#  {key} -> {value}')


def check_max_points(best_student, best_points, submissions):
    for contestant in submissions.keys():
        tot_points = 0
        for contest in submissions[contestant].keys():
            value = submissions[contestant][contest]
            tot_points += value
        if best_points < tot_points:
            best_student = contestant
            best_points = tot_points
    return best_student, best_points


def check_exams(my_dict):
    while True:
        exams_info = input()
        if exams_info == 'end of contests':
            break
        contest, secrets = exams_info.split(':')
        my_dict[contest] = secrets
    return my_dict


def check_submissions(exams, submissions):
    while True:
        submissions_info = input()
        if submissions_info == 'end of submissions':
            break
        contest, password, student, points = submissions_info.split('=>')
        if contest in exams.keys():
            if password in exams[contest]:
                if student in submissions.keys():
                    if contest in submissions[student].keys() and int(points) > submissions[student][contest]:
                        submissions[student].update({contest: int(points)})
                    elif contest in submissions[student].keys() and int(points) <= submissions[student][contest]:
                        continue
                    else:
                        submissions[student].update({contest: int(points)})
                else:
                    submissions[student] = {contest: int(points)}
    return submissions


exams_dictionary = {}
submissions_dictionary = {}
max_points_student = ''
max_points = 0

exams_dictionary = check_exams(exams_dictionary)
submissions_dictionary = check_submissions(exams_dictionary, submissions_dictionary)
max_points_student, max_points = check_max_points(max_points_student, max_points, submissions_dictionary)
print(f'Best candidate is {max_points_student} with total {max_points} points.')
print('Ranking:')

filtering(submissions_dictionary)
