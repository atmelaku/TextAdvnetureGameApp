from flask import (
    Blueprint,  redirect, render_template, request, url_for
)

from werkzeug.exceptions import abort

bp = Blueprint('math', __name__)

@bp.route('/', methods=("GET", "POST"))
def home():
    return render_template("base.html")
@bp.route('/1', methods=("GET", "POST"))
def one():
    if request.method == "POST":
        answer1 = request.form['answer1']
        answer2 = request.form['answer2']
        answer3 = request.form['answer3']
        answer4 = request.form['answer4']
        if answer1 == "3" and answer2 == "8" and answer3 == "4" and answer4 == "7":

            return "100%, nice Job!, try the next level" + render_template("part1.html")
        elif answer1 == "3" and answer2 == "8" and answer3 == "4" and answer4 != "7":
            return "75%, good. you missed number 4, try agin." + render_template("part1.html")
        elif answer1 == "3" and answer2 == "8" and answer3 != "4" and answer4 != "7":
            return "50%, you missed number 3 1nd 4, try agin." + render_template("part1.html")
        elif answer1 == "3" and answer2 != "8" and answer3 != "4" and answer4 != "7":
            return "25%, you missed number 2, 3, and 4, try agin." + render_template("part1.html")
        elif answer1 != "3" and answer2 != "8" and answer3 != "4" and answer4 != "7":
            return "you got 0%. you missed all of them, try agin." + render_template("part1.html")
        return render_template('base.html')


    return render_template("part1.html")
@bp.route('/2', methods=("GET", "POST"))
def two():
    if request.method == "POST":
        answer1 = request.form['answer1']
        answer2 = request.form['answer2']
        answer3 = request.form['answer3']
        answer4 = request.form['answer4']
        if answer1 == "1" and answer2 == "8" and answer3 == "-1" and answer4 == "-3":

            return "100%, nice Job!, try the next level" + render_template("part1.html")
        elif answer1 == "1" and answer2 == "8" and answer3 == "-1" and answer4 != "-3":
            return "75%, good. you missed number 4, try agin." + render_template("part1.html")
        elif answer1 == "1" and answer2 == "8" and answer3 != "-1" and answer4 != "-3":
            return "50%, you missed number 3 1nd 4, try agin." + render_template("part1.html")
        elif answer1 == "1" and answer2 != "8" and answer3 != "-1" and answer4 != "-3":
            return "25%, you missed number 2, 3, and 4, try agin." + render_template("part1.html")
        elif answer1 != "1" and answer2 != "8" and answer3 != "-1" and answer4 != "-3":
            return "you got 0%. you missed all of them, try agin." + render_template("part1.html")

    return render_template("part2.html")
@bp.route('/3', methods=("GET", "POST"))
def three():
    if request.method == "POST":
        answer1 = request.form['answer1']
        answer2 = request.form['answer2']
        answer3 = request.form['answer3']
        answer4 = request.form['answer4']
        if answer1 == "2" and answer2 == "30" and answer3 == "0" and answer4 == "-9":

            return "100%, nice Job!, try the next level" + render_template("part1.html")
        elif answer1 == "2" and answer2 == "30" and answer3 == "0" and answer4 != "-9":
            return "75%, good. you missed number 4, try agin." + render_template("part1.html")
        elif answer1 == "2" and answer2 == "30" and answer3 != "0" and answer4 != "-9":
            return "50%, you missed number 3 1nd 4, try agin." + render_template("part1.html")
        elif answer1 == "2" and answer2 != "30" and answer3 != "0" and answer4 != "-9":
            return "25%, you missed number 2, 3, and 4, try agin." + render_template("part1.html")
        elif answer1 != "2" and answer2 != "30" and answer3 != "0" and answer4 != "-9":
            return "you got 0%. you missed all of them, try agin." + render_template("part1.html")

    return render_template("part3.html")
@bp.route('/4', methods=("GET", "POST"))
def four():
    if request.method == "POST":
        answer1 = request.form['answer1']
        answer2 = request.form['answer2']
        answer3 = request.form['answer3']
        answer4 = request.form['answer4']
        if answer1 == "2" and answer2 == "0" and answer3 == "1" and answer4 == "4":

            return "100%, nice Job!, try the next level" + render_template("part1.html")
        elif answer1 == "2" and answer2 == "0" and answer3 == "1" and answer4 != "4":
            return "75%, good. you missed number 4, try agin." + render_template("part1.html")
        elif answer1 == "2" and answer2 == "0" and answer3 != "1" and answer4 != "4":
            return "50%, you missed number 3 1nd 4, try agin." + render_template("part1.html")
        elif answer1 == "2" and answer2 != "0" and answer3 != "1" and answer4 != "4":
            return "25%, you missed number 2, 3, and 4, try agin." + render_template("part1.html")
        elif answer1 != "2" and answer2 != "0" and answer3 != "1" and answer4 != "4":
            return "you got 0%. you missed all of them, try agin." + render_template("part1.html")

    return render_template("part4.html")
