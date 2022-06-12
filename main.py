from random import choice
choices = ['R', 'P', 'S']
R, P, S = 'Rock', 'Paper', 'Scissors'
Play = True
while Flag:
    prompt = str(input('Do you want to play again? (y for yes / n for no) '))
    if prompt.lower() == 'y':
        user = str(input('R for Rock, P for Paper, S for Scissors) '))
        cpu = choice(choices)
        if user.lower() == cpu.lower():
            print('Player ({}) : CPU ({}) It is a tie'.format(user.capitalize(), cpu))
        elif user.lower() == 'r' and cpu == 'S':
            print('Player ({}) : CPU ({}) Player Wins'.format(R, S))
            
        elif user.lower() == 'p' and cpu == 'R':
            print('Player ({}) : CPU ({}) Player Wins'.format(P, R))
            
        elif user.lower() == 's' and cpu == 'P':
            print('Player ({}) : CPU ({}) Player Wins'.format(S, P))
            
        elif user.lower() == 's' and cpu == 'R':
            print('Player ({}) : CPU ({}) CPU Wins'.format(S, R))
            
        elif user.lower() == 'r' and cpu == 'P':
            print('Player ({}) : CPU ({}) CPU Wins'.format(R, P))
            
        elif user.lower() == 'p' and cpu == 'S':
            print('Player ({}) : CPU ({}) CPU Wins'.format(P, S))
            
        else:
            print('Enter the correct choice')
            Flag = True
    elif prompt.lower() == 'n':
        print('Game has Ended')
        Flag = False
    else:
        print('Enter the correct choice')
