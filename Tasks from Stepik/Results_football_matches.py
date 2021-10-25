"""
Программа принимает на  вход список игр футбольных команд с результатом
матча и выводит сводную таблицу результатов всех матчей.
За победу команде начисляется 3 очка, за поражение — 0, за ничью — 1.
Формат ввода следующий:
В первой строке указано целое число nn — количество завершенных игр.
После этого идет nn строк, в которых записаны результаты игры в следующем формате:
Первая_команда;Забито_первой_командой;Вторая_команда;Забито_второй_командой

Вывод программы необходимо оформить следующим образом:
Команда:Всего_игр Побед Ничьих Поражений Всего_очков

Пример:
Sample Input:
3
Спартак;9;Зенит;10
Локомотив;12;Зенит;3
Спартак;8;Локомотив;15

Sample Output:
Спартак:2 0 0 2 0
Зенит:2 1 0 1 3
Локомотив:2 2 0 0 6
"""
import collections

results = collections.defaultdict(list)
lines_number = int(input())
for _ in range(lines_number):
    team1, score1, team2, score2 = input().strip().split(';')
    score1 = int(score1)
    score2 = int(score2)
    if score1 == score2:
        results[team1].append(1)
        results[team2].append(1)
        continue

    if score1 > score2:
        results[team1].append(3)
        results[team2].append(0)
    else:
        results[team2].append(3)
        results[team1].append(0)

for team, scores in results.items():
    games = str(len(scores))
    wins = str(scores.count(3))
    draws = str(scores.count(1))
    loses = str(scores.count(0))
    total = str(sum(scores))
    print('%s:%s' % (team, ' '.join((games, wins, draws, loses, total))))