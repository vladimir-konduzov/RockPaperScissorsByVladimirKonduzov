from random import randint

rock = 'Rock'
paper = 'Paper'
scissors = 'Scissors'

while True:
    player_move = input("Choose [r]ock, [p]aper, or [s]cissors: ")

    if player_move == 'r':
        player_move = rock
    elif player_move == 'p':
        player_move = paper
    elif player_move == 's':
        player_move = scissors
    else:
        raise SystemExit('Invalid input. try again...')

    # print(f'your move is: {player_move}')

    computer_random_number = randint(1, 3)

    computer_move = ''

    if computer_random_number == 1:
        computer_move = rock
    elif computer_random_number == 2:
        computer_move = paper
    elif computer_random_number == 3:
        computer_move = scissors
    else:
        raise SystemExit('Invalid computer move :). try again...')

    # print(f'Computer move is: {computer_move}')

    if (player_move == rock and computer_move == scissors) or \
            (player_move == paper and computer_move == rock) or \
            (player_move == scissors and computer_move == paper):
        print("You win!")
    elif (player_move == rock and computer_move == rock) or \
            (player_move == paper and computer_move == paper) or \
            (player_move == scissors and computer_move == scissors):
        print("Draw!")
    else:
        print("Computer win!")

