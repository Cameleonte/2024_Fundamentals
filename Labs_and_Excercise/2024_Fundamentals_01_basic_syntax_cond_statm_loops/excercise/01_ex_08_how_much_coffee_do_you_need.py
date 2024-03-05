command = input()

coffee_number = 0

while command != 'END':
    event = command
    if event == 'CODING' or event == 'MOVIE' or event == 'DOG' or event == 'CAT':
        coffee_number += 2
    elif event.lower() == 'coding' or event.lower() == 'movie' or event.lower() == 'dog' or event.lower() == 'cat':
        coffee_number += 1
    command = input()
if coffee_number > 5:
    print('You need extra sleep')
else:
    print(coffee_number)
