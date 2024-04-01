def pass_valid(string):
    errors = []

    if not 6 <= len(string) <= 10:
        errors.append('Password must be between 6 and 10 characters')
    if not string.isalnum():
        errors.append('Password must consist only of letters and digits')
    if sum(char.isdigit() for char in string) < 2:
        errors.append('Password must have at least 2 digits')

    if errors:
        for error in errors:
            print(error)
    else:
        print('Password is valid')


user_password = input()
pass_valid(user_password)
