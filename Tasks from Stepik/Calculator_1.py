"""
From binary to 9 and 16 to 10 sn
"""


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


print('Welcome to a calculator translator from some random sn to decimal sn.')
while True:
    print('Enter the base sn followed by the number itself.')
    base, number = int(input()), input()
    print('Result in decimal sn =', calculator(base, number))
    output = input(
        'If you want to leave the program, just write EXIT and press ENTER\notherwise press ENTER\n')
    if output == 'EXIT':
        break