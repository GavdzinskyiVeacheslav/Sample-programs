"""
Программа читает с файла построчный список с оценками из 4-ёх элементов(Имя студента и три оценки).
Выводит среднюю оценку строки и всех столбцов по первой, второй и третей оценке.
Округляет ответ в(float) до 9 знака после запятой.

Для теста:
Sample Input:
Петров;85;92;78
Сидоров;100;88;94
Иванов;58;72;85

Sample Output:
85.0
94.0
71.666666667
81.0 84.0 85.666666667
"""

count_students, sum_grade_str = 0, 0
sum_grade_column1, sum_grade_column2, sum_grade_column3 = [], [], []

text = open("file.txt", "r", encoding='utf-8')


def add_indices_to_arr(lis_t: list, index: str):
    """ Эта функция - создаёт список чисел столбца по индексам строки.
    Например все первые или все вторые элементы строки """
    return lis_t.append(int(index))


def average(x: list):
    """ Эта функция - вычисляет среднее арифметческое оценок столбцов """
    return round(sum(x) / count_students, 9)


while True:
    work_space = text.read().split()

    if not work_space:
        break

    for line in work_space:
        count_students += 1  # number of lines in the file(number of students)
        line = line.strip().split(';')
        sum_grade_str = (int(line[1]) + int(line[2]) + int(line[3])) / (len(line) - 1)
        add_indices_to_arr(sum_grade_column1, line[1])
        add_indices_to_arr(sum_grade_column2, line[2])
        add_indices_to_arr(sum_grade_column3, line[3])
        print(round(sum_grade_str, 9))

print(average(sum_grade_column1), average(sum_grade_column2), average(sum_grade_column3))