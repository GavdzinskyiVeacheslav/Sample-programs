"""
A valid BEEGEEK bank password is a: b: c, where a, b and c are natural numbers. Since the founder of BEEGEEK
is a fan of math, then he decided:

* number a - must be palindrome
* number b - must be prime
* number c - must be even

Write a function is_valid_password (password) that takes the password string value as an argument
and returns True if the password is a valid BEEGEEK bank password and False otherwise.

For tests:
'1221:101:22' -- True
'565:30:50' -- False
'112:7:9' -- False
'1221:101:22:22' -- False

"""


def is_valid_pin(pincode: list):
    """ Checking if all three properties match """
    if len(pincode) > 3:
        return False

    def is_prime(a: str):
        """ Checking for a prime number """
        if int(a) == 1:
            return False
        for i in range(2, int(a)):
            if int(a) % i == 0:
                return False
        return True

    def is_palindrome(b: str):
        """ Palindromicity check """
        for i in range(0, len(b) // 2):
            if b[i] != b[len(b) - i - 1]:
                return False
        return True

    def is_even(c: str):
        """ Parity check """
        if int(c) % 2 == 0:
            return True
        else:
            return False

    return is_prime(pincode[1]) and is_palindrome(pincode[0]) and is_even((pincode[2]))


pin = input().split(':')
print(is_valid_pin(pin))