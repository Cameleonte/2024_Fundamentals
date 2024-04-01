def creating_dictionaries():
    contests_info = input()
    contest_dictionary = {}
    individual_standings = {}
    while contests_info != 'no more time':
        username, contest, points = contests_info.split(' -> ')
        if contest not in contest_dictionary:
            contest_dictionary[contest] = {}

        if username not in contest_dictionary[contest]:
            contest_dictionary[contest][username] = int(points)
            if username not in individual_standings:
                individual_standings[username] = 0
            individual_standings[username] += int(points)
        else:
            if contest_dictionary[contest][username] < int(points):
                contest_dictionary[contest].update({username: points})
                individual_standings[username] = int(points)
        contests_info = input()
    return contest_dictionary, individual_standings


def sorting_students(first_dictionary, individuals):
    for contest_name, sub_dictionary in first_dictionary.items():
        print(f'{contest_name}: {len(sub_dictionary)} participants')
        sorted_points_dictionary = dict(sorted(sub_dictionary.items(), key=lambda x: (-int(x[1]), x[0])))

        number = 1
        for user in sorted_points_dictionary:
            print(f'{number}. {user} <::> {sorted_points_dictionary[user]}')
            number += 1

    print('Individual standings:')
    sorted_users_dictionary = dict(sorted(individuals.items(), key=lambda a: (-int(a[1]), a[0])))

    num = 1
    for name, data in sorted_users_dictionary.items():
        print(f'{num}. {name} -> {data}')
        num += 1


prime_dictionary, personal_ranking = creating_dictionaries()
sorting_students(prime_dictionary, personal_ranking)
