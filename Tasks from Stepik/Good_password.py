"""
The program takes the password string value password as an argument and returns
True if the password is strong, False otherwise.
The password is strong if:

* its length is at least 8 characters
* it contains at least one uppercase letter (uppercase)
* it contains at least one lowercase letter (lowercase)
* оit contains at least one digit

For tests:
'aabbCC11OP' -- True
'abC1pu' -- False

"""


def is_password_good(pas):
    digits = 0
    capital = 0
    lowercase = 0
    if len(pas) < 8:
        return False
    else:
        for i in pas:
            if i in '0123456789':
                digits += 1
            if i.isupper():
                capital += 1
            if i.islower():
                lowercase += 1
    if digits >= 1 and capital >= 1 and lowercase >= 1:
        return True
    return False


txt = input()

print(is_password_good(txt))