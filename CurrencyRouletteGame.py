#to install the directory:  pip install  currencyconverter
from currency_converter import CurrencyConverter
import random

c = CurrencyConverter()

def get_money_interval(money):
        t = c.convert(money, 'USD', 'ILS')
        t_From = t - (5-difficulty)
        t_To = t + (5-difficulty)
        return t_From, t_To



def get_guess_from_user():
        myGuess = input("Enter your answer:")
        return myGuess


def play(level):
        global difficulty
        difficulty = level
        oneToHundred = random.randint(1, 100)
        rangeFrom,rangeTo = get_money_interval(oneToHundred)
        print("what you thing is the value of the " + str(oneToHundred) + "$ in ISL?")
        myAnswer = get_guess_from_user()
        if int(myAnswer) >= int(rangeFrom) and int(myAnswer) <= int(rangeTo):
            return True
        else:
            return False







