# BMI calculation software

from colorama import init, Fore, Back, Style

init()
print(Fore.GREEN + "Hi there, Welcome to BMI calculation software!")
print(Fore.CYAN)

weight = float(input("What's your weight?: "))
height = float(input("And what's your height?: "))
print("")

bmi = float("{0:.2f}".format(weight / ((height / 100) * (height / 100))))
print(Back.RESET + "Your current BMI is " + str(bmi))

if bmi <= 16:
    print(Fore.RED + "High body mass deficit", end='')
if 16 <= bmi <= 18.5:
    print(Fore.YELLOW + "Insufficient body weight", end='')
if 18.5 <= bmi <= 25:
    print(Fore.GREEN + "Your weight is OK", end='')
if 25 <= bmi <= 30:
    print(Fore.YELLOW + "Excess body weight", end='')
if 30 <= bmi <= 35:
    print(Fore.RED + "Obesity of the 1 degree", end='')
if 35 <= bmi <= 40:
    print(Fore.RED + "Obesity of the 2 degree", end='')
if bmi > 40:
    print(Fore.RED + "Obesity of the 3 degree (morbid)", end='')

print(")", end='')
print(Style.RESET_ALL)
input()