""" The program generates a specified number of passwords and includes a smart setting for the password length,
as well as which characters you want to include and which ones to exclude. """


from random import choice

numbers = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_.'
chars = ''


def request_number(message: str):
    """This function checks if the user entered a digit exactly, if not, asks again"""
    while True:
        result = input(message)

        if result.isdigit():
            result = int(result)
            break
        else:
            print('You entered something wrong. Enter the number! --- ')
    return result


def digits():
    """Asks if to add numbers to the generated password"""
    question = input('Add numbers 0123456789 to your password? --- ')
    while question != 'yes' or question != 'no':
        if question == 'no':
            return False
        elif question == 'yes':
            return True
        else:
            question = input('You entered something wrong. Enter Yes or No! --- ').lower()


def upper_case():
    """Asks if to add uppercase letters to the generated password"""
    question = input('Add uppercase letters to your password? --- ')
    while question != 'yes' or question != 'no':
        if question == 'no':
            return False
        elif question == 'yes':
            return True
        else:
            question = input('You entered something wrong. Enter Yes or No! --- ').lower()


def lower_case():
    """Asks if to add lowercase letters to the generated password"""
    question = input('Add small letters to your password? --- ')
    while question != 'yes' or question != 'no':
        if question == 'yes':
            return False
        elif question == 'no':
            return True
        else:
            question = input('You entered something wrong. Enter Yes or No! --- ').lower()


def symbols():
    """Asks if to add symbols !#$%&*+-=?@^_. to the generated password"""
    question = input('Add characters !#$%&*+-=?@^_. to your password? ---  ')
    while question != 'yes' or question != 'no':
        if question == 'no':
            return False
        elif question == 'yes':
            return True
        else:
            question = input('You entered something wrong. Enter Yes or No! --- ').lower()


def ambiguous():
    """Asks if to add ambiguous symbols il1Lo0O to the generated password"""
    question = input('Whether to exclude ambiguous il1Lo0O characters? --- ')
    while question != 'yes' or question != 'no':
        if question == 'no':
            return True
        elif question == 'yes':
            return False
        else:
            question = input('You entered something wrong. Enter Yes or No! --- ').lower()


def generate_password(n: int, le_n: int, char: str):
    """ Generates and gives out passwords"""
    passwords = []
    for i in range(n):
        passwords.append(''.join(choice(char) for _ in range(le_n)))

    return passwords


print('Welcome to the password generator!')
number = request_number('Enter the desired number of passwords to generate --- ')
length = request_number('Enter password length --- ')

if digits():
    chars += numbers
if upper_case():
    chars += lowercase_letters
if lower_case():
    chars += uppercase_letters
if symbols():
    chars += punctuation
if ambiguous():
    for _ in 'il1Lo0O':
        chars = chars.replace(_, '')

if len(chars) > 0:
    print()
    print("Please, here are your password(s):")
    print(*generate_password(number, length, chars), sep=' ')
else:
    print('You have not chosen what to generate a password from! Goodbye!')
