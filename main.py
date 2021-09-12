import random; import os
all_options = ['rock', 'paper', 'scissors', 'lizard', 'spock']
player_score = 0
computer_score = 0
choosing = True
player_choice = ''
while choosing:
    os.system('clear')
    print('''Welcome to Rock, Paper, Scissors, Lizard, Spock!
Exit - "1"
View Scores - "2"
Play - "rock", "paper", "scissors", "lizard" or "spock"
    ''')
    player_choice = input('> ').strip()
    if player_choice == '1':
        break
    elif player_choice == '2':
        print(f'''
Current Scores:
Player - {player_score}
Computer - {computer_score}
        ''')
        input('[Press Enter]')
    elif player_choice in all_options:
        def find_list():
            rock_win = ['rock', 'scissors', 'lizard']
            paper_win = ['paper', 'rock', 'spock']
            scissors_win = ['scissors', 'paper', 'lizard']
            lizard_win = ['lizard', 'paper', 'spock']
            spock_win = ['spock', 'rock', 'scissors']
            lists = [rock_win, paper_win, scissors_win, lizard_win, spock_win]
            for list in lists:
                if player_choice in list[0]:
                    return list
        computer_choice = random.choice(all_options)
        print()
        if computer_choice == player_choice:
            print(f'Its a Draw! You both picked {computer_choice.title()}!')
        elif computer_choice in find_list():
            print(f'You win! {player_choice.title()} beats {computer_choice.title()}!'); player_score+=1
        else:
            print(f'You Loose! {computer_choice.title()} beats {player_choice.title()}!'); computer_score+=1
        print()
        input('[Press Enter]')
    else:
        print('Invalid Option, Try Again')
        print()
        input('[Press Enter]')
print()
print('Thank You for Playing!')