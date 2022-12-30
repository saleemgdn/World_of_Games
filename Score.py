from Utils import SCORES_FILE_NAME

def add_score(DIFFICULTY):
    POINTS_OF_WINNING = (DIFFICULTY * 3) + 5
    print("Congratulations! , you have won " + str(POINTS_OF_WINNING) + " points")
    try:
        # r+ is an open mode that is used to open an existing file for both reading and writing.
        # This mode will raise an error if the file does not already exist.
        with open(SCORES_FILE_NAME,'r+') as f:
            currentVal = f.read()
            if currentVal == '':
                f.write(str(POINTS_OF_WINNING))
            else:
                data = int(currentVal) + POINTS_OF_WINNING
                f.seek(0)
                f.write(str(data))
    except FileNotFoundError:
        # x+ is an open mode that is used to open a file with exclusive creation access.
        # This mode will open an existing file or create a new file if it does not exist.
        # If the file already exists, opening it with x+ will raise an error.
        with open(SCORES_FILE_NAME, 'x+') as f:
            f.write(str(POINTS_OF_WINNING))






