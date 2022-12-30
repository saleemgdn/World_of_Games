
import random


secret_number = 0

def generate_number():
    global secret_number
    secret_number = random.randint(0, difficulty)



def get_guess_from_user():
    number = input("insert number between 0 to " + str(difficulty) + ": ")
    return number

def compare_result_from_user(guessNumber):
    if int(guessNumber) == int(secret_number):
        return True
    else:
        return False

def play(level):
        global difficulty
        difficulty = level
        generate_number()
        guessNumber = get_guess_from_user()
        isSuccess = compare_result_from_user(guessNumber)
        if (isSuccess):
           return True
        else:
           return False






