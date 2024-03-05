def check_info(courses, course):
    return True if course not in courses else False


def add_students(courses_info, name_c, name_st):
    if check_info(courses_info, name_c):
        dictionary_courses[course_name] = [students_name]
    else:
        dictionary_courses[course_name] += [students_name]


def end_command(dictionary):
    for name_of_course, value in dictionary.items():
        print(f'{name_of_course}: {len(value)}')
        for index in range(len(value)):
            pearson_names = value[index]
            print(f'-- {pearson_names}')


dictionary_courses = {}

while True:
    subscription_info = input()
    if subscription_info == 'end':
        end_command(dictionary_courses)
        break

    course_name, students_name = subscription_info.split(' : ')
    add_students(dictionary_courses, course_name, students_name)
