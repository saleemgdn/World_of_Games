from selenium.webdriver.common.by import By
from Utils import SCORES_FILE_NAME, BAD_RETURN_CODE
from selenium.webdriver.chrome.service import Service
from selenium import webdriver

def test_scores_service(URL):
    # open the flask url using webdriver
    driver = webdriver.Chrome(executable_path=r'/Users/test/Downloads/chromedriver_win32/chromedriver.exe')
    driver.get(URL)

    # get the score value from the page
    score_element = driver.find_element(By.ID, 'score')
    score = score_element.text

    # check if score is between 1 and 1000
    if int(score) >= 1 and int(score) <= 1000:
        #Score is between 1 and 1000
        return True
    else:
        #Score is not between 1 and 1000")
        return False




def  main_function():
     isValid = test_scores_service("http://127.0.0.1:8777")
     if isValid:
         return 0
     else:
         return -1



main_function()
