from flask import Flask, render_template, request, flash, session, redirect, jsonify
from model import connect_to_db, db, User, FestivalInfo
#, Event, UserEvent, FestivalPost, Follower
import crud

from jinja2 import StrictUndefined


app = Flask(__name__)
app.secret_key = "sdjhfbdhjfbfdjh"
app.jinja_env.undefined = StrictUndefined


@app.route("/")
def homepage():
    return redirect("/login")

@app.route("/search")
def search():
    return render_template("search.html")

@app.route("/search-results.json", methods=["POST"])
def search_results():
    festival = request.json.get("fest_location")
    festquery = f'%{festival}%'
    festival_results = FestivalInfo.query.filter(FestivalInfo.fest_location.like(festquery)).all()
    
    results = []

    for fest in festival_results:
        festlo = {
            "fest_id": fest.fest_id,
            "fest_name": fest.fest_name, 
            "fest_location": fest.fest_location,
            "fest_startdate": fest.fest_startdate, 
            "fest_enddate": fest.fest_enddate, 
            "line_up": fest.line_up,
        }
        results.append(festlo)

    print(festival_results)
    print(results)
    return jsonify(results)


@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/handle-login", methods=["POST"])
def process_login():

    email = request.form.get("email")
    password = request.form.get("password")

    user = crud.get_user_by_email(email)
    if not user or user.password != password:
        flash("The email or password you entered was incorrect.")
    else:
        session["user_email"] = user.email
        flash(f"Welcome back, {user.username}!")
        return redirect("/profile")
    return redirect("/")

@app.route("/profile")
def profile_page():
    user = crud.get_user_by_email(session["user_email"])
    print("We're loggin in this user")
    print(user)
    #get the user by their email
    #pass that into our render template statement
    return render_template("profile.html", user=user)

@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/login")


# @app.route("/register", methods=["POST"])
# def register():
#     new_user = request.json
#     users.append(new_user)
#     return redirect("/login")


# users = {}

@app.route('/create_account', methods=['POST'])
def create_account():
    fname = request.form.get('fname') 
    lname = request.form.get('lname')
    username = request.form.get('username')
    email = request.form.get('email')
    password = request.form.get('password')
    print("This is the username")
    print(username)
    user = crud.get_user_by_email(email)
    print("This is the user")
    print(user)
    if user:
        flash("Cannot create an account with that email. Try again.")
    else:
        user = crud.create_user(fname, lname, username, email, password)
        db.session.add(user)
        db.session.commit()
        flash("Account created! Please log in.")

    return redirect("/login")



# @app.route('/profile/<username>')
# def profile(username):
#     user = users.get(username)
#     if user:
#         return render_template('profile.html', user=user)
#     else:
#         return 'User not found', 404


# @app.route("/users/<user_id>")
# def show_user(user_id):
#     user = crud.get_user_by_id(user_id)
#     return render_template("user_details.html", user=user)



# @app.route("/festivals")
# def all_festivals():
#     festivals = crud.get_festivals()
#     return render_template("all_festivals.html", festivals=festivals) 



# @app.route("/festivalinfo/<fest_id>")
# def show_fest(fest_id):
#     festival = crud.get_fest_by_id(fest_id)
#     return render_template("festival_details.html", festival=festival)



if __name__ == "__main__":
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)
