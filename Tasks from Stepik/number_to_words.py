""" The program takes a natural number num as an argument and returns
its verbal description in Russian. """


def number_to_words(num):
    se = [' ', 'один', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять', 'десять', 'одиннадцать',
          'двенадцать', 'тринадцать', 'четырнадцать', 'пятнадцать', 'шестнадцать', 'семнадцать', 'восемнадцать',
          'девятнадцать']
    sd = ['', '', 'двадцать', 'тридцать', 'сорок', 'пятьдесят', 'шестьдесят', 'семьдесят', 'восемьдесят', 'девяносто']
    if num < 20:
        return se[num]
    if num >= 20:
        return sd[num // 10 % 10] + se[0] + se[num % 10]


n = int(input())

print(number_to_words(n))