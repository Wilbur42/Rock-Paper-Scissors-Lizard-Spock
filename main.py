import random
import os

options = {
    'rock': ['scissors', 'lizard'],
    'paper': ['rock', 'spock'],
    'scissors': ['paper', 'lizard'],
    'lizard': ['paper', 'spock'],
    'spock': ['rock', 'scissors']
}

player_score = 0
computer_score = 0

while True:
    os.system('clear')
    print('Welcome to Rock, Paper, Scissors, Lizard, Spock!')
    print('Exit - "1"\nView Scores - "2"\nPlay - "rock", "paper", "scissors", "lizard" or "spock"')

    player_choice = input('> ').lower().strip()

    if player_choice == '1':
        print(f'\nFinal Scores:\nPlayer - {player_score}\nComputer - {computer_score}')
        break

    if player_choice == '2':
        print(f'\nCurrent Scores:\nPlayer - {player_score}\nComputer - {computer_score}')

    elif player_choice in options:
        computer_choice = random.choice(options[player_choice])

        if computer_choice == player_choice:
            print(f"\nIt's a Draw! You both picked {computer_choice.title()}!")
        elif computer_choice in options[player_choice]:
            player_score += 1
            print(f'\nYou win! {player_choice.title()} beats {computer_choice.title()}!')
        else:
            computer_score += 1
            print(f'\nYou Lose! {computer_choice.title()} beats {player_choice.title()}!')

    else:
        print('Invalid Option, Try Again')

    input('\n[Press Enter]')

print('\nThank You for Playing!')