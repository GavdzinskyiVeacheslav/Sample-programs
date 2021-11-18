""" The game shows the meaning of the word that you need to guess,
you can also see the number of letters with closed asterisks.
The player can immediately name the full word or guess by the letter:

* If the letter is in the word, then it will open in its place (if there are several such letters, all open).
* If there is no such letter in the word, then a points will be taken away """

import random


def greetings():
    """ Greets the player and display the rules of the game.
    If the player wants to play again, the rules will no longer be duplicated """
    print("Hello, player, I welcome you to the game field of miracles:\n "
          " * you have 100 points\n "
          " * for each letter of which is not in the word you will be deducted 10 points\n "
          " * for each correctly guessed +5 points\n "
          " * if you get to 0 you lost\n "
          " * if you don't guess the whole word at once -60 points\n"
          "Good luck!\n")


def word_choice():

    """
    * Reads material for a game from a txt file
    * Creates an empty dictionary
    * Arranges a random selection of the hidden word
    * Displays a description of the meaning of a word
    * And it returns (passes) the word further to the main function of the game

    """

    text = open("word list for field of dreams.txt")
    words = {}

    for line in text:
        words[line] = text.readline()
    choice = random.choice(list(words.keys()))
    word = choice.strip()
    print(words[choice])
    return word


def game(word: str):
    """ The main function of the game:
        * Gives the player starting points
        * Closes the word with asterisks - (how many letters are in the word)
        * Checks if the letter was entered exactly and not something else,
          if the input is incorrect, asks to enter what is needed
        * Keeps records the count of points when to subtract when to add,
          depending on the loss or on the winnings, displays a corresponding message and ends the game
        * If the letter is guessed correctly, then it opens these letters in the word """
    points = 100
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
    answer()


def answer():
    """ This function asks the player if he wants to play again.
     If the answer is yes it starts the game.
     If the answer is no it says goodbye to the player. """
    print("Do you want to play again?\n"
          "If you want enter - Yes if not enter - No")
    while 1:
        res = input().lower().strip()
        if res not in ("yes", "no"):
            print("Enter 'yes' or 'no'")
            continue
        if res == 'yes':
            game(word_choice())
        if res == 'no':
            print('Thanks for playing the "Field of dreams" game. See you...')
        break


greetings()
game(word_choice())