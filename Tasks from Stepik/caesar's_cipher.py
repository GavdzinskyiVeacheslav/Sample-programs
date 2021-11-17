""" This program can encrypt and decrypt text according to the Caesar algorithm.
Requests the user for the following data:

* direction: encryption or decryption
* alphabet language: Russian or English
* shift step (with shift to the right)

"""


def shifr(side, alphabet, step):
    line = list(LINE)
    if alphabet == 'EN':
        step %= 26
    else:
        step %= 33
    if side == 'SHIFR':
        if alphabet == 'EN':
            for i in range(len(line)):
                if 96 < ord(line[i].lower()) < 123:
                    if ord(line[i].lower()) + step < 123:
                        if line[i].isupper():
                            line[i] = chr(ord(line[i].lower()) + step).upper()
                        else:
                            line[i] = chr(ord(line[i]) + step)
                    else:
                        if line[i].isupper():
                            line[i] = chr(ord(line[i].lower()) - 26 + step).upper()
                        else:
                            line[i] = chr(ord(line[i]) - 26 + step)
        else:
            for i in range(len(line)):
                if 1071 < ord(line[i].lower()) < 1104:
                    if ord(line[i].lower()) + step < 1104:
                        if line[i].isupper():
                            line[i] = chr(ord(line[i].lower()) + step).upper()
                        else:
                            line[i] = chr(ord(line[i]) + step)
                    else:
                        if line[i].isupper():
                            line[i] = chr(ord(line[i].lower()) - 32 + step).upper()
                        else:
                            line[i] = chr(ord(line[i]) - 32 + step)
    else:
        if alphabet == 'EN':
            for i in range(len(line)):
                if 96 < ord(line[i].lower()) < 123:
                    if 96 < ord(line[i].lower()) - step:
                        if line[i].isupper():
                            line[i] = chr(ord(line[i].lower()) - step).upper()
                        else:
                            line[i] = chr(ord(line[i]) - step)
                    else:
                        if line[i].isupper():
                            line[i] = chr(ord(line[i].lower()) + 26 - step).upper()
                        else:
                            line[i] = chr(ord(line[i]) + 26 - step)
        else:
            for i in range(len(line)):
                if 1071 < ord(line[i].lower()) < 1104:
                    if 1071 < ord(line[i].lower()) - step:
                        if line[i].isupper():
                            line[i] = chr(ord(line[i].lower()) - step).upper()
                        else:
                            line[i] = chr(ord(line[i]) - step)
                    else:
                        if line[i].isupper():
                            line[i] = chr(ord(line[i].lower()) + 32 - step).upper()
                        else:
                            line[i] = chr(ord(line[i]) + 32 - step)

    return line


while True:
    print('Welcome to the encryptor program.')
    while True:
        stor = input('Enter what we will do: encrypt or decrypt.\nSHIFR/DESHIFR\n')
        if stor in {'SHIFR', 'DESHIFR'}:
            break
        else:
            print('Incorrect word. Enter a value from the following to choose from')
    while True:
        alf = input('Enter the alphabet used: English or Russian.\nEN/RU\n')
        if alf in {'EN', 'RU'}:
            break
        else:
            print('Incorrect word. Enter a value from the following to choose from')
    while True:
        shag = input('Enter, numeric offset value.\n')
        if shag.isdigit():
            shag = int(shag)
            break
        else:
            print('Invalid character. Please enter a different value.')
    LINE = input('Enter the text that you want to decrypt or encrypt without errors, '
                 'otherwise the answer will be incorrect\n')
    print('Here is your encrypted string:\n', *shifr(stor, alf, shag), sep='')
    x = input('f you want to exit the program, just press ENTER!!! Otherwise write something.\n')
    if x == '':
        print('Good luck!')
        break