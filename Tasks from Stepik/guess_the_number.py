""" The program generates a random number in the range from 1 to n and asks the user to guess this number.
If the user's guess is greater than a random number, then the program should display a message -
'Too many, try again.' If the guess is less than a random number, then the program should print a message -
'Too little, try again.' If the user guesses the number, then the program should congratulate him
and display the message - 'You guessed it, congratulations!'. """

from random import randint
from time import sleep


def answer():
    """ This function asks the player if he wants to play again.
     If the answer is yes it starts the game.
     If the answer is no it says goodbye to the player. """
    print("Want to play again? yes/no")
    while 1:
        res = input().lower().strip()
        if res not in ("yes", "no"):
            print("Enter 'yes' or 'no'")
            continue
        if res == 'yes':
            game()
        if res == 'no':
            print('Thanks for playing the number guessing game. See you...')
        break


def is_valid(num, limit):
    """This function checks if the player has made the correct input.(i.e. number)"""
    if num.isdigit():
        num = int(num)
        if 1 <= num <= int(limit):
            return True
        else:
            return False
    else:
        return False


def is_valid_right(num):
    """This function checks if the player has entered the upper bound correctly."""
    if not num.isdigit():
        return False
    if int(num) < 2:
        return False

    return True


def game():
    """ This is the main function, everything happens here """
    print('Welcome to "Number Guess", I suggest you guess a number in the range from 1 to ... choose yourself =) ')
    sleep(0.3)
    print("By the way, you will only have 5 attempts, so good luck =)")
    attempts = 1
    sleep(0.3)
    limit = input('Enter the upper limit of the game range:    ')
    while not is_valid_right(limit):
        limit = input('You entered something wrong, enter a number (digit)!   ')

    num = randint(1, int(limit))

    while True:
        sleep(0.3)
        response = input('Guess --  ')
        if not is_valid(response, limit):
            print(f'You entered something wrong, enter a number (digit) in the range from 1 to {limit}!')
            continue
        response = int(response)

        if attempts == 1:
            s = "attempt"
        else:
            s = "attempts"

        if attempts > 5:
            print('Attempts ended - you lost. The number was conceived ', num)
            break
        if response < num:
            print('Too LITTLE, try again')
            attempts += 1
        elif response > num:
            print('Too MUCH, try again')
            attempts += 1
        else:
            print(f'You guessed it, congratulations! You needed - {attempts} {s} =)')
            break
    answer()


game()


