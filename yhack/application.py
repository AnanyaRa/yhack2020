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

        return render_template("question1.html")

    else:
        return render_template("index.html")


@app.route("/question1", methods=["GET", "POST"])
# @login_required
def question1():
    """first question"""

    if request.method=="POST":
        return apology("TODO")

    else:
        return render_template("question1.html")

@app.route("/reco1")
# @login_required
def reco1():
    """reco1"""

    return render_template("reco1.html")

@app.route("/question2")
# @login_required
def question2():
    """q2"""

    return render_template("question2.html")

@app.route("/reco2")
# @login_required
def reco2():
    """reco2"""

    return render_template("reco2.html")

@app.route("/question3", methods=["GET", "POST"])
# @login_required
def question3():
    """q3"""

    return render_template("question3.html")

@app.route("/reco3")
# @login_required
def reco3():
    """reco3"""

    return render_template("reco3.html")

@app.route("/question4", methods=["GET", "POST"])
def question4():
    """question"""

    return render_template("question4.html")


@app.route("/question5", methods=["GET", "POST"])
# @login_required
def question5():
    """q5"""

    return render_template("question5.html")

@app.route("/question6", methods=["GET", "POST"])
def question6():
    """question6"""

    return render_template("question6.html")

@app.route("/question7", methods=["GET", "POST"])
def question7():
    """question7"""

    return render_template("question7.html")

@app.route("/question8", methods=["GET", "POST"])
def question8():
    """question8"""

    return render_template("question8.html")

@app.route("/question9", methods=["GET", "POST"])
def question9():
    """question9"""

    return render_template("question9.html")

@app.route("/question10", methods=["GET", "POST"])
def question10():
    """question10"""

    return render_template("question10.html")


def errorhandler(e):
    """Handle error"""
    if not isinstance(e, HTTPException):
        e = InternalServerError()
    return apology(e.name, e.code)


# Listen for errors
for code in default_exceptions:
    app.errorhandler(code)(errorhandler)
