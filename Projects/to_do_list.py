def main_menu(choice, tasks_list, marked_list):
    """Here the program chooses witch of the following functions to start depending on the user's choice."""
    if int(choice) == 1:
        add_task(tasks_list, marked_list)
    elif int(choice) == 2:
        task_completed(tasks_list, marked_list)
    elif int(choice) == 3:
        view_all_tasks(tasks_list, marked_list)


def check_value(value, control):
    """This function controls if the inserted user's value is correct to proceed with the program."""
    while not control:
        if value.isnumeric():
            if int(value) not in range(1, 5):
                print("\nPlease, enter a valid choice (1, 2, 3 or 4) and press enter: ", end='')
                value = input()
            else:
                control = True
        else:
            print("\nPlease, enter a valid choice (1, 2, 3 or 4) and press enter: ", end='')
            value = input()
    return value, control


def add_task(tasks_list, done_list):
    """Asks to add a new task and displays that it's memorised."""
    print("\nPlease, enter a task description: ", end='')
    task_to_enter = input()
    tasks_list.extend([task_to_enter])
    done_list.append('[ ]')
    print(f"Task \"{task_to_enter}\"" + " added successfully!")
    return tasks_list


def task_completed(lists, done_list):
    """Displays current tasks and asks the user to check the completed one so returns marked as completed."""
    if len(lists) > 0:
        print('\n===== Tasks =====')
        for index in range(len(lists)):
            print(f"{index}. {done_list[index]} {lists[index]}")
        print('\nPlease, enter the index of the task to mark as completed: ', end='')
        marked_index = int(input())
        for index in range(len(lists)):
            if marked_index == index:
                marked_value = '[X]'
                done_list.pop(index)
                done_list.insert(index, marked_value)
        print('Task marked as completed!')
    else:
        print('There are no current task to display.')
    return lists, done_list


def view_all_tasks(lists, done_list):
    """Displays all memorised the tasks on the list."""
    if len(lists) > 0:
        print('\n===== Tasks =====')
        for index in range(len(lists)):
            print(f"{index}. {done_list[index]} {lists[index]}")
    else:
        print('There are no current task to display.')


print("Welcome to your To-Do List!")
list_tasks = []
list_marked_done = []

while True:
    print("\n===== To-Do List Menu =====\n1. Add a new task\n2. Mark a task as completed\n3. View all tasks\n4. Quit\n")
    print("Enter your choice (1-4) and press enter: ", end='')
    user_choice = input()
    controlled_value = False
    user_choice, controlled_value = check_value(user_choice, controlled_value)
    if int(user_choice) == 4:
        print("Exiting the program. Goodbye!")
        break
    main_menu(user_choice, list_tasks, list_marked_done)
