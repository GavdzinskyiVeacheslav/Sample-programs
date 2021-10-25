from random import choice

numbers = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_.'
chars = ''


def request_number(message):
    while True:
        result = input(message)

        if result.isdigit():
            result = int(result)
            break
        else:
            print('Вы ввели что-то не то. Введите число! --- ')
    return result


def digits():
    question = input('Добавлять в ваш пароль цифры 0123456789 ? --- ')
    while question != 'да' or question != 'нет':
        if question == 'нет':
            return False
        elif question == 'да':
            return True
        else:
            question = input('Вы ввели что-то не то. Введите Да или Нет! --- ').lower()


def letters():
    question = input('Добавлять в ваш пароль большие буквы ? --- ')
    while question != 'да' or question != 'нет':
        if question == 'нет':
            return False
        elif question == 'да':
            return True
        else:
            question = input('Вы ввели что-то не то. Введите Да или Нет! --- ').lower()


def strochnue():
    question = input('Добавлять в ваш пароль маленькие буквы? --- ')
    while question != 'да' or question != 'нет':
        if question == 'нет':
            return False
        elif question == 'да':
            return True
        else:
            question = input('Вы ввели что-то не то. Введите Да или Нет! --- ').lower()


def simbols():
    question = input('Добавлять в ваш пароль символы --- ? ')
    while question != 'да' or question != 'нет':
        if question == 'нет':
            return False
        elif question == 'да':
            return True
        else:
            question = input('Вы ввели что-то не то. Введите Да или Нет! --- ').lower()


def neodnoznach():
    question = input('Исключать ли неоднозначные символы il1Lo0O? --- ')
    while question != 'да' or question != 'нет':
        if question == 'нет':
            return True
        elif question == 'да':
            return False
        else:
            question = input('Исключить неоднозначные символы il1Lo0O? --- ').lower()


def generate_password(n, le_n, char):
    passwords = []
    for i in range(n):
        passwords.append(''.join(choice(char) for _ in range(le_n)))

    return passwords


print('Приветствую вас в генераторе паролей!')
number = request_number('Введите желаемое количество паролей для генерации --- ')
length = request_number('Введите длину пароля --- ')

if digits():
    chars += numbers
if letters():
    chars += lowercase_letters
if strochnue():
    chars += uppercase_letters
if simbols():
    chars += punctuation
if neodnoznach():
    for _ in 'il1Lo0O':
        chars = chars.replace(_, '')

if len(chars) > 0:
    print()
    print("Пожалуйста вот ваши пароль(и):")
    print(*generate_password(number, length, chars), sep=' ')
else:
    print('Вы не выбрали из чего генерировать пароль! Досвидания!')