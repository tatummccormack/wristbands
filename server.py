from flask import Flask, render_template, request, flash, session, redirect, jsonify
from model import connect_to_db, db, User, FestivalInfo, Post
import crud

from jinja2 import StrictUndefined


app = Flask(__name__)
app.secret_key = "sdjhfbdhjfbfdjh"
app.jinja_env.undefined = StrictUndefined


@app.route("/")
def homepage():
    return render_template("homepage.html")

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
    return redirect("/search")

@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/login")

@app.route("/profile")
def profile_page():
    user = crud.get_user_by_email(session["user_email"])
    print("We're loggin in this user")
    print(user)
    #get the user by their email
    #pass that into our render template statement
    return render_template("profile.html", user=user)

# @app.route('/update_bio', methods =["POST"])
# def update_bio(user_id):

#     new_bio = request.form.get['bio']
#     if len(new_bio) > 200: 
#         return "Maximum Character limit 200"
    
#     user = crud.get_user_by_id(user_id)

#     if not user: 
#         return "User Not Found"
    
#     user['bio'] = new_bio
#     return redirect("/profile")

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

@app.route("/fest-results.json", methods=["POST"])
def fest_results():
    festival = request.json.get("fest_name")
    festquery = f'%{festival}%'
    festival_results = FestivalInfo.query.filter(FestivalInfo.fest_name.like(festquery)).all()
    
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





# @app.route("/register", methods=["POST"])
# def register():
#     new_user = request.json
#     users.append(new_user)
#     return redirect("/login")



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


@app.route('/create_post', methods=['POST'])
def create_post():
   
    content = request.form.get('content')
    user = crud.get_user_by_email(session["user_email"])
    # post_time = request.json.get('createdAt') # Assuming you pass user ID in the request

    # if not user_id:
    #     return jsonify({"error": "Missing userid data"}), 400
    
    # if not content:
    #     return jsonify({"error": "Missing required data"}), 400

    crud.create_feed_post(content, user.user_id)

    return redirect('/')


@app.route('/post-results.json', methods=['GET'])
def get_posts():

    posts = crud.get_all_posts()
    allposts = []

    for post in posts:
        current_post = {"content":post.content, "user_id":post.user_id, "post_id":post.post_id}
        allposts.append(current_post)

    return jsonify(allposts)


# @app.route("/handle-posts", methods=["POST"])
# def process_post():

#     user_id = request.json.get('user_id') 
#     content = request.json.get('content')
#     post_time = request.json.get('createdAt')

#     post = crud.get_Post(fchat_id)
#     if not user or user.password != password:
#         flash("The email or password you entered was incorrect.")
#     else:
#         session["user_email"] = user.email
#         flash(f"Welcome back, {user.username}!")
#         return redirect("/profile")
#     return redirect("/search")

# @app.route('/follow', methods=['POST'])
# def follow_user():
#     users = crud.get_user_by_id('user_id')
#     follower = crud.get_follower_by_id(follower_id)
#     followee = crud.get_followee_by_id(followee_id)

#     if not follower or not followee:
#         return jsonify({"error": "Missing follower or followed_user"}), 400

#     if followee not in users:
#         return jsonify({"error": "User not found"}), 404

#     users[followee]["followers"].append(follower)
#     return jsonify({"message": "Successfully followed user"}), 200

# @app.route('/unfollow', methods=['POST'])
# def unfollow_user():
#     Users = crud.request.get('user_id')
#     follower = crud.request.get('follower_id')
#     followee = crud.request.get('followee_id')

#     if not follower or not followee:
#         return jsonify({"error": "Missing follower or followed_user"})

#     if followee not in Users:
#         return jsonify({"error": "User not found"})

#     Users[followee]["followers"].remove(follower)
#     return jsonify({"message": "Successfully unfollowed user"})


# @app.route('/profile/<username>')
# def profile(username):
#     user = users.get(username)
#     if user:
#         return render_template('profile.html', user=user)
#     else:
#         return 'User not found', 404


@app.route("/festivals")
def all_festivals():
    festivals = crud.get_festivals()
    return render_template("all_festivals.html", festivals=festivals)  


@app.route("/festivals/<fest_id>")
def show_fest(fest_id):
    festival = crud.get_fest_by_id(fest_id)
    return render_template("festival_details.html", festival=festival)



if __name__ == "__main__":
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)
