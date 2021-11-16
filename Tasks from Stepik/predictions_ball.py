""" Magic ball 8 (ball of fate) is a comic way to predict the future. The program should ask the user to ask a question
in order to randomly answer it."""

from random import choice
from time import sleep

answers = ['Indisputably', 'I think so', "It's not clear yet, try again", 'Do not even think',
           'A foregone conclusion', 'Most likely', 'Ask later', 'My answer is - no', 'Without any doubts',
           'Good prospects', 'Better not to tell', 'According to my data - no', 'Definitely yes',
           'The signs say yes', "Can't predict now", 'Prospects are not very good',
           'You can be sure of this', 'Yes', 'Concentrate and ask again', 'Highly doubtful']

sleep(0.5)
print('Hello World, I am a magic ball, and I know the answer to any of your questions.')

sleep(0.2)
name = input('What is your name? --- ')
print('Hello', name.title())

answer = 'yes'

while answer.lower().strip() == 'yes':
    sleep(0.2)
    question = input('Ask: ')
    sleep(0.2)
    print(choice(answers))
    answer = input('Do you want to ask something else? Enter yes or no --- ')
    while answer != 'yes' or answer != 'no':
        if answer == 'no':
            print('Come back if you have any questions!')
            break
        elif answer == 'yes':
            break
        else:
            answer = input('You entered something wrong. Enter Yes or No! --- ').lower()
