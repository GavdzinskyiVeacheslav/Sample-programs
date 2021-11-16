""" The game shows the meaning of the word that you need to guess,
you can also see the number of letters with closed asterisks.
The player can immediately name the full word or guess by the letter:

* If the letter is in the word, then it will open in its place (if there are several such letters, all open).
* If there is no such letter in the word, then a points will be taken away """

import random
text = open("word list for field of dreams.txt")
words = {}
points = 100
for line in text:
    words[line] = text.readline()
choice = random.choice(list(words.keys()))
word = choice.strip()
print()
print("Hello, player, I welcome you to the game field of miracles:\n "
      " * you have 100 points\n "
      " * for each letter of which is not in the word you will be deducted 10 points\n "
      " * for each correctly guessed +5 points\n "
      " * if you get to 0 you lost\n "
      " * if you don't guess the whole word at once -60 points\n"
      "Good luck!\n")

if len(words[choice]) >= 120:
    print(words[choice][:100], words[choice][100:], sep='\n')
elif 120 <= len(words[choice]) <= 300:
    print(words[choice][:100], words[choice][100:200], words[choice][200:], sep='\n')
else:
    print(words[choice])

field = "*" * len(word)
print(field)
while "*" in field:
    user = input("Guess the letter ")
    if not user.isalpha():
        print("You entered a number, please enter a letter or full word")
    if user in word:
        points += 5
        print(f"Your points now {points}")
    if user not in word:
        points -= 10
        print(f"Your points now {points}")
    if len(user) > 1 and user != word:
        points -= 50
        print(f"Your points now {points}")
    if points <= 0:
        print("I'm sorry but you ran out of points and lost")
        break
    if user == word:
        print("Congratulations you did it, you won!")
        break
    auxiliary_variable = ""
    for number in range(len(word)):
        if user == word[number]:
            auxiliary_variable += user
        else:
            auxiliary_variable += field[number]
    field = auxiliary_variable
    print(field)
print("Do you want to play again?")
# print("If you want enter - yes if not enter - no")
# TODO: Rewrite code normally !

