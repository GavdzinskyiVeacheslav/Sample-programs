"""
Действительный пароль BEEGEEK банка имеет вид a:b:c, где a, b и c – натуральные числа. Поскольку основатель BEEGEEK
фанатеет от математики, то он решил:

число a – должно быть палиндромом;
число b – должно быть простым;
число c – должно быть четным.
Напишите функцию is_valid_password(password),которая принимает в качестве аргумента строковое значение пароля password
и возвращает значение True если пароль является действительным паролем BEEGEEK банка и False в противном случае.

Примечание. Следующий программный код:
print(is_valid_password('1221:101:22'))
print(is_valid_password('565:30:50'))
print(is_valid_password('112:7:9'))
print(is_valid_password('1221:101:22:22'))

должен выводить:
True
False
False
False

"""


def is_valid_pin(pincode):
    """ Checking if all three properties match """
    if len(pincode) > 3:
        return False

    def is_prime(a):
        """ Checking for a prime number """
        if int(a) == 1:
            return False
        for i in range(2, int(a)):
            if int(a) % i == 0:
                return False
        return True

    def is_palindrome(b):
        """ Palindromicity check """
        for i in range(0, len(b) // 2):
            if b[i] != b[len(b) - i - 1]:
                return False
        return True

    def is_even(c):
        """ Parity check """
        if int(c) % 2 == 0:
            return True
        else:
            return False

    return is_prime(pincode[1]) and is_palindrome(pincode[0]) and is_even((pincode[2]))


pin = input().split(':')
print(is_valid_pin(pin))