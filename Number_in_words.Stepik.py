# Напишите функцию number_to_words(num), которая принимает в качестве аргумента натуральное число num и возвращает
# его словесное описание на русском языке.

# объявление функции
def number_to_words(num):
    se = [' ', 'один', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять', 'десять', 'одиннадцать',
          'двенадцать', 'тринадцать', 'четырнадцать', 'пятнадцать', 'шестнадцать', 'семнадцать', 'восемнадцать',
          'девятнадцать']
    sd = ['', '', 'двадцать', 'тридцать', 'сорок', 'пятьдесят', 'шестьдесят', 'семьдесят', 'восемьдесят', 'девяносто']
    if num < 20:
        return se[num]
    if num >= 20:
        return sd[num // 10 % 10] + se[0] + se[num % 10]

# считываем данные
n = int(input())

# вызываем функцию
print(number_to_words(n))