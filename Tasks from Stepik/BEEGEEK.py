
# Действительный пароль BEEGEEK банка имеет вид a:b:c, где a, b и c – натуральные числа. Поскольку основатель BEEGEEK
# фанатеет от математики, то он решил:

# число a – должно быть палиндромом;
# число b – должно быть простым;
# число c – должно быть четным.
# Напишите функцию is_valid_password(password),которая принимает в качестве аргумента строковое значение пароля password
# и возвращает значение True если пароль является действительным паролем BEEGEEK банка и False в противном случае.


def is_valid_pin(pin):
    if len(pin) > 3:
        return False

    def is_prime(a):
        if int(a) == 1:
            return False
        for i in range(2, int(a)):
            if int(a) % i == 0:
                return False
        return True

    def is_palindrome(b):
        for i in range(0, len(b) // 2):
            if b[i] != b[len(b) - i - 1]:
                return False
        return True

    def is_even(c):
        if int(c) % 2 == 0:
            return True
        else:
            return False

    return is_prime(pin[1]) and is_palindrome(pin[0]) and is_even((pin[2]))


pin = input().split(':')
print(is_valid_pin(pin))