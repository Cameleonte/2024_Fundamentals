messages_sent = int(input())

for i in range(1, messages_sent + 1):
    user_number = int(input())
    if user_number == 88:
        print('Hello')
    elif user_number == 86:
        print('How are you?')
    elif user_number < 88:
        print('GREAT!')
    elif user_number > 88:
        print('Bye.')
