def add_people(number_of_people):
    new_number_to_insert = wagon_list.pop() + number_of_people
    wagon_list.append(new_number_to_insert)


def insert_people(position, number_of_people):
    new_number_to_insert = wagon_list.pop(position) + number_of_people
    wagon_list.insert(position, new_number_to_insert)


def leave_people(position, number_of_people):
    new_number_to_insert = wagon_list.pop(position) - number_of_people
    wagon_list.insert(position, new_number_to_insert)


wagon_numbers = int(input())
wagon_list = [0] * wagon_numbers

command = input().split()
while command[0] != 'End':
    if len(command) > 2:
        people = int(command[2])
        index = int(command[1])
        if command[0] == 'insert':
            insert_people(index, people)
        elif command[0] == 'leave':
            leave_people(index, people)
    elif len(command) == 2:
        people = int(command[1])
        add_people(people)
    command = input().split()
    
print(wagon_list)
