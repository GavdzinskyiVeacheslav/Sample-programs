"""
The program reads from a file a line-by-line list with grades of 4 elements (Student name and three grades).
Displays the average score for the row and all columns for the first, second, and third scores.
Rounds the answer in (float) to the 9th decimal place.

For tests:
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
    """ This function - creates a list of column numbers by row indices.
    For example, all the first or all the second elements of the string"""
    return lis_t.append(int(index))


def average(x: list):
    """ This function - calculates the arithmetic mean of the column scores """
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