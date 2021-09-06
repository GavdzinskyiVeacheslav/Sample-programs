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
    print('Вас приветствует программа шифратор.')
    while True:
        stor = input('Введите, что будем делать: шифровать или дешифровать.\nSHIFR/DESHIFR\n')
        if stor in {'SHIFR', 'DESHIFR'}:
            break
        else:
            print('Некоректное слово. Введите значение из указанных на выбор')
    while True:
        alf = input('Введите, используемый алфавит: английский или русский.\nEN/RU\n')
        if alf in {'EN', 'RU'}:
            break
        else:
            print('Некоректное слово. Введите значение из указанных на выбор')
    while True:
        shag = input('Введите, числовое значение сдвига.\n')
        if shag.isdigit():
            shag = int(shag)
            break
        else:
            print('Некоректный символ. Введите иное значение.')
    LINE = input('Введите текст, который нужно дешифровать или шифровать без ошибок, иначе ответ будет некоректный\n')
    print('Вот ваша зашифрованная строка:\n', *shifr(stor, alf, shag), sep='')
    x = input('Если вы желаете выйти из программы, то просто нажмите ENTER!!! Иначе напишите что-нибудь.\n')
    if x == '':
        print('Всего хорошего!')
        break