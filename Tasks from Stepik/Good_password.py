
# Принимает в качестве аргумента строковое значение пароля password и возвращает значение True если пароль является
# надежным и False в противном случае.
# его длина не менее 88 символов;
# он содержит как минимум одну заглавную букву (верхний регистр);
# он содержит как минимум одну строчную букву (нижний регистр);
# он содержит хотя бы одну цифру.

# объявление функции
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


# считываем данные
txt = input()

# вызываем функцию
print(is_password_good(txt))