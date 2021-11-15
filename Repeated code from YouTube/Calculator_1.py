""" I am learning to do something ... """

from colorama import init

init()

what = input('\033[30m\033[42m' + "What do we do? (+, -):  ")

a = float(input('\033[30m\033[44m' + "Enter the first number:  "))
b = float(input('\033[30m\033[44m' + "Enter the second number:  "))

if what == "+":
    c = a + b
    print('\033[30m\033[43m' + "Result: " + str(c))
elif what == "-":
    c = a - b
    print("Result: " + str(c))
else:
    print("Invalid operation selected!")