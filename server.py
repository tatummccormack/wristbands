from flask import Flask, render_template, request, flash, session, redirect
from model import connect_to_db, db
import crud

from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined


@app.route("/")
def homepage():

    return render_template("homepage.html")

@app.route("/festivals")
def all_festivals():
    
    festivals = crud.get_festivals()

    return render_template("all_festivals.html", festivals=festivals) 

@app.route("/festivalinfo/<fest_id>")
def show_fest(fest_id):

    festival = crud.get_fest_by_id(fest_id)

    return render_template("festival_details.html", festival=festival)

@app.route("/users", methods=["POST"])
def register_user():

    email = request.form.get("email")
    password = request.form.get("password")

    user = crud.get_user_by_email(email)
    if user:
        flash("Cannot create an account with that email. Try again.")
    else:
        user = crud.create_user(email, password)
        db.session.add(user)
        db.session.commit()
        flash("Account created! Please log in.")

    return redirect("/")

@app.route("/users/<user_id>")
def show_user(user_id):

    user = crud.get_user_by_id(user_id)

    return render_template("user_details.html", user=user)