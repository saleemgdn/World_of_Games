import sys
import GuessGame
import MemoryGame
import CurrencyRouletteGame
import Score
from Utils import screen_cleaner


def welcome(name):
    return "Hello " + name + " and welcome to the World of Games (WoG). \nHere you can find many cool games to play."


def load_game():
    print("Please choose a game to play:")
    print("1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back")
    print("2. Guess Game - guess a number and see if you chose like the computer")
    print("3. Currency Roulette - try and guess the value of a random amount of USD in ILS")

    try:
        game_number = int(input())
    except:
        print("error: input is not integer type")
        sys.exit()

    if game_number > 3 or game_number < 1:
        print("number must be between 1 to 3")
        sys.exit()

    difficulty = input("Please choose game difficulty from 1 to 5: ")

    try:
        difficulty = int(difficulty)
        if difficulty > 5 or difficulty < 1:
            print("number must be between 1 to 5")
            sys.exit()
    except:
        print("error: input is not integer type")
        sys.exit()

    if game_number == 1:
        isWin =MemoryGame.play(difficulty)
    elif game_number == 2:
        isWin =GuessGame.play(difficulty)
    else:
        isWin =CurrencyRouletteGame.play(difficulty)

    if isWin:
        print("Excellent!!, your answer is correct.")
        Score.add_score(difficulty)
    else:
        print("Your answer is incorrect, Game Over :(")

    print("Do you want to play again (y/n) ?")
    ans = input()

    if ans == "y":
        screen_cleaner()
        load_game()
    else:
        print("Thanks! , see you later my friend :)")








