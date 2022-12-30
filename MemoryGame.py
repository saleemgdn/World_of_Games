
import random
import os
import time
from Utils import screen_cleaner

randomList = []
userGuessList = []

def generate_sequence():
    global randomList
    for i in range(difficulty):
         randomList.insert(len(randomList), random.randint(1, 101))


def get_list_from_user():
    for i in range(difficulty):
        number = input("insert number (" + str(i) + "):")
        userGuessList.insert(len(userGuessList), number)

def is_list_equal():
    for i in range(difficulty):
        if(int(userGuessList[i]) != int(randomList[i])):
            return False
    return True


def play(level):
        global difficulty
        difficulty = level
        generate_sequence()
        time.sleep(0.7)
        screen_cleaner()
        get_list_from_user()
        isEqual = is_list_equal()
        if(isEqual):
            return True
        else:
            return False




