from Utils import SCORES_FILE_NAME, BAD_RETURN_CODE
from flask import Flask


app = Flask(__name__)

@app.route("/")
def score_server():
    try:
        with open(SCORES_FILE_NAME, 'r+') as f:
            points = f.read()
            return "<html>" \
                       "<head>" \
                         "<title>Scores Game</title>" \
                       "</head>" \
                       "<body>" \
                         "<h1>The score is <div id=\"score\">" + points + "</h1>" \
                       "</body>" \
                   "</html>"
    except:
            return "<html>" \
                      "<head>" \
                        "<title>Scores Game</title>" \
                      "</head>" \
                      "<body>" \
                         "<h1><div id=\"score\" style=\"color:red\">" + str(BAD_RETURN_CODE) + "</h1>" \
                      "</body>" \
                  "</html>"






app.run()