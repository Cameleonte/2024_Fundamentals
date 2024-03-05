def check_user(dict1, user1, check_exists):
    if user1 in dict1:
        check_exists = True
    return check_exists


def register(user_data, existing_user, register_dictionary):
    username = user_data[1]
    license_plate_number = user_data[2]
    existing_user = check_user(register_dictionary, username, existing_user)
    if existing_user:
        print(f'ERROR: already registered with plate number {license_plate_number}')
    else:
        register_dictionary[username] = license_plate_number
        print(f'{username} registered {license_plate_number} successfully')


def unregister(user_data, checking_user, new_dict):
    username = user_data[1]
    if check_user(new_dict, username, checking_user):
        del new_dict[username]
        print(f'{username} unregistered successfully')
    else:
        print(f'ERROR: user {username} not found')


parking_users_count = int(input())
registered_users_dict = {}
for user in range(parking_users_count):
    system_input = input().split()
    user_check = False
    if len(system_input) == 2:
        unregister(system_input, user_check, registered_users_dict)
    elif len(system_input) == 3:
        register(system_input, user_check, registered_users_dict)
for user, license_num in registered_users_dict.items():
    print(f"{user} => {license_num}")
