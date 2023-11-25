from Utils import *
from flask import Flask, render_template


def Score_server():
    score_file = open(SCORES_FILE_NAME, 'r')

    current_score = score_file.read()

    score_file.close()

    app = Flask(__name__)

    @app.route("/")
    def index():

        if current_score == "":
            return render_template('error.html', error_message=f"{BAD_RETURN_CODE}")

        return render_template('score.html', score=current_score)

    app.run(host="0.0.0.0", port=80)

Score_server()
