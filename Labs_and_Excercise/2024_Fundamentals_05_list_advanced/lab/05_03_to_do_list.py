def sorting_tasks():
    list_tasks = []
    command = input()
    while command != 'End':
        list_tasks.append(command)
        command = input()

    sorted_tasks = sorted(list_tasks, key=lambda x: int(x.split('-')[0]))
    sorted_tasks = [command.split('-')[1] for command in sorted_tasks]
    return sorted_tasks


result = sorting_tasks()
print(result)
