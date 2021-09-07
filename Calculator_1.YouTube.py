from colorama import init

init()

what = input('\033[30m\033[42m' + "Что делаем? (+, -):  ")

a = float(input('\033[30m\033[44m' + "Введите первое число:  "))
b = float(input('\033[30m\033[44m' + "Введите второе число:  "))

if what == "+":
    c = a + b
    print('\033[30m\033[43m' + "Результат: " + str(c))
elif what == "-":
    c = a - b
    print("Результат: " + str(c))
else:
    print("Выбрана не верная операция!")