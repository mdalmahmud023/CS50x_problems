import os
import datetime
from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""
    balance = db.execute("SELECT cash FROM users WHERE id = ?", session["user_id"])
    cash = balance[0]["cash"]
    total = cash
    rows = db.execute("SELECT symbol, SUM(shares), price, total FROM shares WHERE user_id = ? GROUP BY symbol", session["user_id"])
    for row in rows:
        row["symbol"] = row["symbol"].upper()
        look = lookup(row["symbol"])
        row["price"] = look["price"]

        row["total"] = row["price"] * row["SUM(shares)"]

        total += row["total"]

    return render_template("index.html", rows=rows, cash=cash, total=total)


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""
    if request.method == "POST":
        symbol = request.form.get("symbol")
        quote_data = lookup(symbol)
        if not request.form.get("shares"):
            return apology("empty share", 400)
        s = request.form.get("shares")
        try:
            shares = int(s)
        except:
            return apology("invalid or empty stock symbol", 400)
        if not quote_data:
            return apology("invalid or empty stock symbol", 400)
        date = datetime.datetime.now()
        price = quote_data["price"]
        total = shares * price
        usr_id = session["user_id"]
        balance = db.execute("SELECT cash FROM users WHERE id = ?", usr_id)
        cash = balance[0]["cash"]

        if shares < 1:
            return apology("invalid or empty number of shares", 400)

        elif cash < total:
            return apology("you don't have enough cash", 403)

        cash -= total
        db.execute("UPDATE users SET cash = ? WHERE id = ?", cash, usr_id)
        db.execute("INSERT INTO shares (user_id, symbol, shares, price, total, date) VALUES (?, ?, ?, ?, ?, ?)",
                   usr_id, symbol, shares, price, total, date)
        flash("Bought!")
        return redirect("/")

    return render_template("buy.html")


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    # fetch data from shares table
    rows = db.execute("SELECT symbol, shares, price, date FROM shares WHERE user_id = ?", session["user_id"])

    for row in rows:
        row["symbol"] = row["symbol"].upper()
    return render_template("history.html", rows=rows)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute(
            "SELECT * FROM users WHERE username = ?", request.form.get("username")
        )

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(
            rows[0]["hash"], request.form.get("password")
        ):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        flash("Logged In!")
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""
    if request.method == "POST":
        quote_data = lookup(request.form.get("symbol"))
        if not quote_data:
            return apology("invalid or empty stock symbol", 400)
        return render_template("quoted.html", quote_data=quote_data)
    return render_template("quote.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    if request.method == "POST":
        usrname = request.form.get("username")
        password = request.form.get("password")
        if not usrname:
            return apology("must provide username", 400)

        elif not password:
            return apology("must provide password", 400)

        elif password != request.form.get("confirmation"):
            return apology("password and confirm password not matched", 400)

        h = generate_password_hash(password)
        try:
            db.execute("INSERT INTO users (username, hash) VALUES (?, ?)", usrname, h)
        except:
            return apology("this username already exists", 400)
        flash("Registerd!")
        return redirect("/")

    return render_template("register.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    if request.method == "POST":
        # data from the form
        symbol = request.form.get("symbol")
        sell_amount = int(request.form.get("shares"))

        # currently owned share of the particular stock
        shares = db.execute("SELECT SUM(shares) FROM shares WHERE user_id = ? AND symbol = ?", session["user_id"], symbol)
        share = shares[0]["SUM(shares)"]

        # if sell amount is negative
        if sell_amount < 1:
            return apology("invalid shares", 400)

        # not having enough share
        elif sell_amount > share:
            return apology("you don't own that many shares of the stock", 400)

        # checking current price of the symbol
        quote_data = lookup(symbol)
        price = quote_data["price"]
        total = sell_amount * price

        # getting current balance cash
        balance = db.execute("SELECT cash FROM users WHERE id = ?", session["user_id"])
        cash = balance[0]["cash"]

        # shares of the shares
        remain_share = share - sell_amount

        # cash after selling shares update cash
        cash += total
        db.execute("UPDATE users SET cash = ? WHERE id = ?", cash, session["user_id"])

        date = datetime.datetime.now()

        # add this transaction on the shares table
        db.execute("INSERT INTO shares (user_id, symbol, shares, price, total, date) VALUES (?, ?, ?, ?, ?, ?)",
                   session["user_id"], symbol, -sell_amount, price, total, date)

        # redirect to homepage
        flash("Sold!")
        return redirect("/")

    symbols = db.execute("SELECT DISTINCT symbol FROM shares WHERE user_id = ?", session["user_id"])
    for symbol in symbols:
        symbol["symbol"] = symbol["symbol"].upper()
    return render_template("sell.html", symbols=symbols)
