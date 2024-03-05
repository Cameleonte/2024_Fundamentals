students_info = input()

info_university = {}

while True:
    if ':' in students_info:
        student, id_num, course = students_info.split(':')
        if course not in info_university:
            info_university[course] = {}
        info_university[course][student] = id_num
        students_info = input()
    else:
        new_students_info = ' '.join(students_info.split('_'))
        for key, value in info_university.items():
            if key == new_students_info:
                for name, id_num in value.items():
                    print(f"{name} - {id_num}")
        break
