from random import randint
from time import sleep


def answer():
    print("Хотите сыграть ещё раз? да/нет")
    while 1:
        res = input().lower().strip()
        if res not in ("да", "нет"):
            print("Введите 'да' или 'нет'")
            continue
        if res == 'да':
            game()
        if res == 'нет':
            print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
        break


def is_valid(num, limit):
    if num.isdigit():
        num = int(num)
        if 1 <= num <= int(limit):
            return True
        else:
            return False
    else:
        return False


def is_valid_right(num):
    if not num.isdigit():
        return False
    if int(num) < 2:
        return False

    return True


def game():
    print('Добро пожаловать в "Числовую Угадайку", я предлагаю тебе угадать число в диапазоне от 1 до... выбери сам =)')
    sleep(0.3)
    print("Кстати, у тебя будет всего 5 попыток, так что удачи =)")
    attempts = 1
    sleep(0.3)
    limit = input('Введите верхнюю границу диапазона игры:    ')
    while not is_valid_right(limit):
        limit = input('Вы ввели что-то не то, введите число(цифу)!   ')

    num = randint(1, int(limit))

    while True:
        sleep(0.3)
        response = input('Угадывайте --  ')
        if not is_valid(response, limit):
            print(f'Вы ввели что-то не то, введите число(цифу) в диапазоне от 1 до {limit}!')
            continue
        response = int(response)

        if attempts == 1:
            s = "попытка"
        elif 1 < attempts < 5:
            s = "попытки"
        else:
            s = "попыток"

        if attempts > 5:
            print('Попытки закончились - Ты проиграл. Было загадано число ', num)
            break
        if response < num:
            print('Слишком МАЛО, попробуйте еще раз')
            attempts += 1
        elif response > num:
            print('Слишком МНОГО, попробуйте еще раз')
            attempts += 1
        else:
            print(f'Вы угадали, поздравляем! Вам понадобилось - {attempts} {s} =)')
            break


game()
answer()

