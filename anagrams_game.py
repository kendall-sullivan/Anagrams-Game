# Anagrams Game by Kendall Sullivan #
"""
This program runs a game called Anagrams, based on the Game Pigeon game with the
same name, where the user gets six letters and must make words out of them in
thirty seconds. There is more explanation of how the game works in the "How to
Play" and "Rules" sections that are printed when the program runs.
"""

import random
import time

# ---------------------------------------- #
# set-up #
print("Anagrams")
print()
print("How to Play: Using only the six letters given to you, enter as many \n"
      "words as you can in 30 seconds. You will be awarded points for valid \n"
      "words based on the length of the word. At the end of the 30 seconds, \n"
      "your total points will be revealed.")
print()
print("Rules Regarding Validity of Guesses: \n"
      "   - Each word you guess must be between 3 and 6 letters long \n"
      "   - Each word must use only the letters given to you \n"
      "   - You can only use a given letter in your word the number of \n"
      "     times it appears in your given letters")
print()

fileIn = open("sullivan_anagramsWords.txt", 'r')
wordString = fileIn.read()
wordString = wordString.strip()
wordList = wordString.split()

fileIn2 = open("sullivan_anagramsSixWords.txt", 'r')
wordString6 = fileIn2.read()
wordString6 = wordString6.strip()
wordList6 = wordString6.split()


# ---------------------------------------- #
# function definitions #


def getLetters():
    """Chooses a random six-letter word and adds each letter to a list, then
    shuffles the order of the letters in the list"""
    letters = random.choice(wordList6)
    userLetters = []
    for i in letters:
        userLetters.append(i)
    random.shuffle(userLetters)
    return userLetters


def makeListString(aList):
    """Takes a list and adds each character to a string with assigned space and
    the '|' character after each string, to form the letters for the user"""
    string = ""
    for k in aList:
        string = string + k + "  |  "
    return string


def game(pts, letters):
    """Performs one iteration of the user guessing a word or shuffling their
    letters, then if they guess a word it checks its validity, then assigns
    corresponding points if it is valid, if not it tells the user their word is
    not valid"""
    word = input("Enter a word (or enter 's' to shuffle): ")
    wordLength = len(word)
    if word == "s":
        random.shuffle(letters)
    elif word in wordList:
        validWord = True
        dictLetters = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0,
                       'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0,
                       'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0,
                       'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0}
        for lt in letters:
            dictLetters[lt] += 1
        dictWord = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0,
                    'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0,
                    'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0,
                    'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0}
        for ch in word:
            dictWord[ch] += 1
        for key in dictWord:
            if dictWord[key] > dictLetters[key]:
                print()
                print("That is not a valid word.")
                validWord = False
                break
        if validWord:
            print()
            if wordLength == 3:
                pts.append(100)
                print("+100 points")
            elif wordLength == 4:
                pts.append(200)
                print("+200 points")
            elif wordLength == 5:
                pts.append(300)
                print("+300 points")
            elif wordLength == 6:
                pts.append(400)
                print("+400 points")
    else:
        print()
        print("That is not a valid word.")
    return pts


def startGame():
    """Performs one round of Anagrams game, setting the time and having the game
    run until 30 seconds is up, then prints the total points scored"""
    startTime = time.time()
    endTime = time.time()
    points = []
    letters = getLetters()
    while endTime < startTime + 30:
        print()
        print("Your letters: | ",  makeListString(letters))
        print()
        game(points, letters)
        endTime = time.time()
        print()
        if endTime < startTime + 30:
            print("// Time left:", round(startTime + 30 - endTime, 2), "secs //")
        else:
            print("//// Time's up! ////")
        print()
    totalPoints = 0
    for num in points:
        totalPoints += num
    print("Total Points: ", totalPoints)
    print()


def gameWithReplay():
    """Runs the startGame() function, then asks the user if they want to play
    again and runs the same function again if user says 'yes'"""
    choice = "yes"
    while choice == "yes":
        print()
        startGame()
        choice = input("Would you like to play again? (enter 'yes' or 'no'): ")
        if choice == "no":
            print()
            print("Thanks for playing Anagrams!")
        elif choice != "yes":
            while choice != "yes" and choice != "no":
                choice = input("Please enter 'yes' or 'no': ")
                if choice == "no":
                    print()
                    print("Thanks for playing Anagrams!")


# ---------------------------------------- #
# run game #
begin = input("Enter any key when you are ready to begin: ")
if begin or begin == "":
    gameWithReplay()
