#rock,paper,scissors game
#import the random
import random

#create a variable with a randomized value
choice = random.randint(0,2)
winner = ''

#set values to the random numbers to a object(r/p/s)
if choice == 0:
    computer_choice = 'rock'    
elif choice == 1:
    computer_choice = 'paper'
else:
    computer_choice ='scissors'
#get user's choice
user_choice = ''
while (user_choice != 'rock' and
        user_choice != 'paper' and
        user_choice != 'scissors'):
    user_choice = input('rock, paper or scissors? ')
    print('User chose',user_choice)
#determine winner through set of decisions
if computer_choice == user_choice:
    winner = 'Tie'
elif computer_choice == 'rock' and user_choice == 'scissors':
    winner = 'Computer'
elif computer_choice == 'scissors' and user_choice == 'paper':
    winner = 'Computer'
elif computer_choice == 'paper' and user_choice == 'rock':
    winner = 'Computer'
else:
    winner = 'User'

if winner == 'Tie':
    print('We both chose', computer_choice + ',play again')
else:
    print( winner ,'won, I chose ', computer_choice +'.')
    
