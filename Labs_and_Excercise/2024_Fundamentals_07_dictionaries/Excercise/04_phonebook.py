dictionary_users = {}
while True:
    user_data = input()
    if len(user_data) == 1:
        for i in range(int(user_data)):
            names_to_display = input()
            if names_to_display not in dictionary_users:
                print(f'Contact {names_to_display} does not exist.')
            else:
                print(f'{names_to_display} -> {dictionary_users[names_to_display]}')
        break
    name, num = user_data.split('-')
    if name not in dictionary_users:
        dictionary_users[name] = num
