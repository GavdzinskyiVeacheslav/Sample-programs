
"""
Программа читает с файла построчный список с оценками из 4-ёх элементов,
выводит среднюю оценку строки и столбца. Округляет ответ(float) до 9 знака после запятой
"""

count_s, sum_gr, sum_gr1, sum_gr2, sum_gr3, = 0, 0, [], [], []

c = open("dataset_3363_4 (1).txt", "r", encoding='utf-8')

while True:
    s = c.read().split()

    if not s:
        break

    for line in s:
        count_s += 1
        line = line.strip().split(';')
        sum_gr = (int(line[1]) + int(line[2]) + int(line[3])) / (len(line) - 1)
        sum_gr1.append(int(line[1]))
        sum_gr2.append(int(line[2]))
        sum_gr3.append(int(line[3]))
        print(round(sum_gr, 9))


def f(x: list):
    return round(sum(x) / count_s, 9)


print(f(sum_gr1), f(sum_gr2), f(sum_gr3))

