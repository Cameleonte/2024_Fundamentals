import random

rock = 'Rock'
paper = 'Paper'
scissors = 'Scissors'
player_move = ''
game_over = False

while not game_over:
    while True:
        player_move = input('Please, choose [r]ock, [p]aper or [s]cissors: ')
        if player_move != 'r' and player_move != 's' and player_move != 'p':
            print('Invalid input. Try again...')
        else:
            if player_move == 'r':
                player_move = rock
            elif player_move == 'p':
                player_move = paper
            elif player_move == 's':
                player_move = scissors
            break

    computer_random_move = random.randint(1, 3)
    computer_move = ''
    if computer_random_move == 1:
        computer_move = rock
    elif computer_random_move == 2:
        computer_move = paper
    else:
        computer_move = scissors

    print(f'The computer chose: {computer_move}.')

    if (computer_move == rock and player_move == scissors) or \
            (computer_move == paper and player_move == rock) or \
            (computer_move == scissors and player_move == paper):
        print('You lose!')
    elif computer_move == player_move:
        print('Draw!')
    else:
        print('You win!')

    user_choice = input('If you want to play again write "Y": ')
    if user_choice == 'Y':
        continue
    else:
        print('Thanks for playing!')
        game_over = True
