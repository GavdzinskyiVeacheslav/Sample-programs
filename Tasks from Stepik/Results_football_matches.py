"""
The program takes as input a list of games of football teams with the result
match and displays a summary table of the results of all matches.
For a victory, a team is awarded 3 points, for a defeat - 0, for a draw - 1.
The input format is as follows:
The first line contains an integer nn - the number of completed games.
After that, nn lines follow, in which the results of the game are written in the following format:
First_command; Scored by_first_command; Second_team; Scored by_second_command

The output of the program must be formatted as follows:
Team: Total_games Wins Draw Losses Total_points
For tests:
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