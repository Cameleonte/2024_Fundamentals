import random

computer_number = random.randint(1, 100)
user_supposition = 0

while user_supposition != computer_number:
    user_supposition = input('Write your suggestion, a random number from 1 to 100: ')
    if not user_supposition.isdigit():
        print("Invalid input! Please enter a valid number (1 to 100).")
    else:
        user_supposition = int(user_supposition)
        if user_supposition < computer_number:
            print('You\'re too low!')
        elif user_supposition > computer_number:
            print('You\'re too high!')

print('Congratulations! You guessed the number!')
print("If you'd like to play again write 'Y', else press any other key: ")
user_choice = input()
if user_choice == 'Y':
    pass
else:
    print('Thanks for playing! Have a nice time!')
