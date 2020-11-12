import os

# from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
# from werkzeug.security import check_password_hash, generate_password_hash

from helpers import login_required, apology, usd

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True


# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


@app.route("/")
# @login_required
def index():
#     """Show portfolio of stocks"""

#     if request.method == "POST":
#         if not request.form.get("username"):
#             return apology("please enter a username",400)

#         return render_template("question1.html")

#     else:
    return render_template("index.html")

@app.route("/index", methods=["GET","POST"])
# @login_required
def index1():
    """Show portfolio of stocks"""

    if request.method == "POST":
        if not request.form.get("username"):
            return apology("please enter a username",400)

        return render_template("question1_home.html")

    else:
        return render_template("index.html")

@app.route("/islands")
# @login_required
def islands():
    """islands"""

    return render_template("islands.html")


@app.route("/question1_home", methods=["GET", "POST"])
# @login_required
def question1_home():
    """first question"""

    if request.method=="POST":
        return apology("TODO")

    else:
        return render_template("question1_home.html")

@app.route("/reco1_home")
# @login_required
def reco1_home():
    """reco1_home"""

    return render_template("reco1_home.html")

@app.route("/question2_home")
# @login_required
def question2_home():
    """q2_home"""

    return render_template("question2_home.html")

@app.route("/reco2_home")
# @login_required
def reco2_home():
    """reco2_home"""

    return render_template("reco2_home.html")

@app.route("/question3_home", methods=["GET", "POST"])
# @login_required
def question3_home():
    """q3"""

    return render_template("question3_home.html")

@app.route("/reco3_home")
# @login_required
def reco3_home():
    """reco3_home"""

    return render_template("reco3_home.html")

@app.route("/question1_trans", methods=["GET", "POST"])
# @login_required
def question1_trans():
    """first questiontrans"""

    if request.method=="POST":
        return apology("TODO")

    else:
        return render_template("question1_trans.html")

@app.route("/reco1_trans")
# @login_required
def reco1_trans():
    """reco1_trans"""

    return render_template("reco1_trans.html")

@app.route("/question2_trans")
# @login_required
def question2_trans():
    """q2_trans"""

    return render_template("question2_trans.html")

@app.route("/reco2_trans")
# @login_required
def reco2_trans():
    """reco2_trans"""

    return render_template("reco2_trans.html")

@app.route("/question3_trans", methods=["GET", "POST"])
# @login_required
def question3_trans():
    """q3_trans"""

    return render_template("question3_trans.html")

@app.route("/reco3_trans")
# @login_required
def reco3_trans():
    """reco3_trans"""

    return render_template("reco3_trans.html")

@app.route("/question1_food", methods=["GET", "POST"])
# @login_required
def question1_food():
    """first question_food"""

    if request.method=="POST":
        return apology("TODO")

    else:
        return render_template("question1_food.html")

@app.route("/reco1_food")
# @login_required
def reco1_food():
    """reco1_food"""

    return render_template("reco1_food.html")

@app.route("/question2_food")
# @login_required
def question2_food():
    """q2_food"""

    return render_template("question2_food.html")

@app.route("/reco2_food")
# @login_required
def reco2_food():
    """reco2_food"""

    return render_template("reco2_food.html")



def errorhandler(e):
    """Handle error"""
    if not isinstance(e, HTTPException):
        e = InternalServerError()
    return apology(e.name, e.code)


# Listen for errors
for code in default_exceptions:
    app.errorhandler(code)(errorhandler)
