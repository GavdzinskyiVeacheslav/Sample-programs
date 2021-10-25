# Из бинарной до 9 и 16 в 10 сс.


def calculator(b, n):
    if b != 16:
        return sum([int(n[-1 - i]) * b ** i for i in range(len(n))])
    else:
        s = list()
        for i in range(len(n)):
            if n[-1 - i] not in {'A', 'B', 'C', 'D', 'E', 'F'}:
                s.append(int(n[-1 - i]) * b ** i)
            else:
                s.append((ord(n[-1 - i]) - 55) * b ** i)
        return sum(s)


print('Вас приветствует калькулятор переводчик из какой-то случайной сс в десятичную сс.')
while True:
    print('Введите основание сс, а затем само число.')
    base, number = int(input()), input()
    print('Результат в десятичной сс =', calculator(base, number))
    output = input(
        'Если желаете покинуть программу, просто напишите EXIT и нажмите ENTER\nВ противном случае нажмите ENTER\n')
    if output == 'EXIT':
        break