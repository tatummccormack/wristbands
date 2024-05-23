from flask import Flask, render_template, request, flash, session, redirect, jsonify, url_for
from model import connect_to_db, db, User, FestivalInfo, Post, FestPost, Event, PostLike, FestPostLike
from werkzeug.utils import secure_filename

import crud
import os

from jinja2 import StrictUndefined


app = Flask(__name__)
app.secret_key = "sdjhfbdhjfbfdjh"
app.jinja_env.undefined = StrictUndefined



@app.route('/autocomplete')
def autocomplete():
    query = request.args.get('query', '').strip()
    print("Query:", query) 
    
    if len(query) < 3:
        return jsonify([])  
    
    # Perform a search in the festivals table based on fest_name, fest_location, and line_up
    results = FestivalInfo.query.filter(
        (FestivalInfo.fest_name.ilike(f'%{query}%')) |
        (FestivalInfo.fest_location.ilike(f'%{query}%')) |
        (FestivalInfo.line_up.ilike(f'%{query}%'))
    ).distinct(FestivalInfo.fest_name).limit(10).all()
    
    print("Results:", results)  
    
    # Extract relevant data from the results and return as JSON
    autocomplete_suggestions = [{'id': festival.fest_id, 'name': festival.fest_name} for festival in results]
    return jsonify(autocomplete_suggestions)





@app.route("/handle-avatar", methods=["POST"])
def handle_avatar():
    file = request.files['file']
    if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
    if file:
        user = crud.get_user_by_email(session["user_email"])
        filename = secure_filename(file.filename)
        # user.avatar = filename
        file.save(os.path.join(app.root_path, './static/user_avatars', filename))
        # app.root_path,'/images',img.filename
         # => "image.jpg" => '/static/user_avatars/image.jpg'
        # if this doesn't work, try setting:
        user.avatar = './static/user_avatars/' + filename
        # Here you need to then query for the user in the database, and update the user's avatar to the filename
        db.session.add(user)
        db.session.commit()
        return redirect("/profile")
    
@app.route("/home")
def homepage():
    all_posts = crud.get_all_posts()
    return render_template("homepage.html", all_posts=all_posts)

@app.route("/")
def login():
    return render_template("login.html")

@app.route("/handle-login", methods=["POST"])
def process_login():

    email = request.form.get("email")
    password = request.form.get("password")

    user = crud.get_user_by_email(email)
    if not user or user.password != password:
        flash("The email or password you entered was incorrect.")
        return redirect("/")
    else:
        session["user_email"] = user.email
        # flash(f"Welcome back, {user.username}!")
        return redirect("/home")

@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")

@app.route("/profile")
def profile_page():
    user = crud.get_user_by_email(session["user_email"])
    attending_festivals = crud.get_attending_festivals(user.user_id)
    return render_template("profile.html", user=user, attending_festivals=attending_festivals)

@app.route('/update_bio', methods =["POST"])
def update_bio(user_id):

    new_bio = request.form.get['bio']
    if len(new_bio) > 200: 
        return "Maximum Character limit 200"
    
    user = crud.get_user_by_id(user_id)

    if not user: 
        return "User Not Found"
    
    user['bio'] = new_bio
    return redirect("/profile")

# @app.route("/search")
# def search():
#     return render_template("search.html")

# @app.route("/search-results.json", methods=["POST"])
# def search_results():
#     festival = request.json.get("fest_location")
#     festquery = f'%{festival}%'
#     festival_results = FestivalInfo.query.filter(FestivalInfo.fest_location.like(festquery)).all()
    
#     results = []

#     for fest in festival_results:
#         festlo = {
#             "fest_id": fest.fest_id,
#             "fest_name": fest.fest_name, 
#             "fest_location": fest.fest_location,
#             "fest_startdate": fest.fest_startdate, 
#             "fest_enddate": fest.fest_enddate, 
#             "line_up": fest.line_up,
#         }
#         results.append(festlo)

#     return jsonify(results)



# @app.route("/fest-results.json", methods=["POST"])
# def fest_results():
#     festival = request.json.get("fest_name")
#     festquery = f'%{festival}%'
#     festival_results = FestivalInfo.query.filter(FestivalInfo.fest_name.like(festquery)).all()
    
#     results = []

#     for fest in festival_results:
#         festlo = {
#             "fest_id": fest.fest_id,
#             "fest_name": fest.fest_name, 
#             "fest_location": fest.fest_location,
#             "fest_startdate": fest.fest_startdate, 
#             "fest_enddate": fest.fest_enddate, 
#             "line_up": fest.line_up,
#         }
        
#         results.append(festlo)

#     print(festival_results)
#     print(results)
#     return jsonify(results)



@app.route("/create_account", methods=["POST"])
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


@app.route("/edit_bio", methods=["POST"])
def edit_bio():

    user = crud.get_user_by_email(session["user_email"])
    
    user.bio = request.form["bio"]
    db.session.commit()

    return redirect(url_for("profile_page"))


@app.route("/create_post", methods=["POST"])
def create_post():
   
    content = request.form.get('content')
    user = crud.get_user_by_email(session["user_email"])
   
    print(content)
    print(user.user_id)
    crud.create_feed_post(content, user.user_id)

    return redirect('/home')

@app.route('/post-results.json', methods=['GET'])
def get_posts():

    posts = crud.get_all_posts()
    allposts = []

    for post in posts:
        current_post = {
            "avatar":post.user.avatar,
            "content":post.content, 
            "user_id":post.user_id, 
            "post_id":post.post_id, 
            "username":post.user.username, 
            "like_count": post.like_count,
            "created_at": post.created_at 
        }

        allposts.append(current_post)
    print(allposts)
    return jsonify(allposts)


@app.route('/createFest_post', methods=['POST'])
def createFest_post():

    fest_id = request.form.get('fest_id')
    content = request.form.get('content')
    user = crud.get_user_by_email(session["user_email"])
    print(fest_id)
    print(content)
    print(user.user_id)

    crud.createFest_post(content, user.user_id, fest_id)

    return redirect(url_for('show_fest', fest_id=fest_id))


@app.route('/festpost-results.json/<fest_id>', methods=['GET'])
def get_festposts(fest_id):

    festposts = crud.get_all_posts_by_fest(fest_id)
    allfestposts = []

    if festposts:
        for fp in festposts:
            current_post = {
                "avatar":fp.user.avatar,
                "content":fp.content, 
                "user_id":fp.user_id, 
                "username":fp.user.username, 
                "festpost_id":fp.festpost_id, 
                "fest_id":fp.fest_id,
                "like_count":fp.like_count,
                "created_at": fp.created_at 
                }
            print(current_post)
            allfestposts.append(current_post)
        print(allfestposts)
    return jsonify(allfestposts)


@app.route('/like/<int:post_id>', methods=['POST'])
def like_post(post_id):

    post = crud.get_post_by_id(post_id)
    user = crud.get_user_by_email(session["user_email"])
    user_has_liked = PostLike.query.filter( (PostLike.user_id == user.user_id) & (PostLike.post_id == post.post_id) ).all()

    if not user_has_liked:
        new_like = crud.create_post_like(user.user_id, post.post_id)
        print(post.like_count)
        post.like_count += 1
        db.session.add(post)
        db.session.commit()
        print(user_has_liked)
        return jsonify({'added': 'Success!'})
    else:
        # create crud delete_post_like()
        crud.delete_post_like(user.user_id, post.post_id)
        return jsonify({'added': 'Unliked'})

@app.route('/like/<int:festpost_id>', methods=['POST']) #CHANGES NEEDED TO GET WORKING
def festlike_post(festpost_id):

    festpost = crud.get_festpost_by_id(festpost_id)
    user = crud.get_user_by_email(session["user_email"])
    user_has_liked = festPostLike.query.filter( (festPostLike.user_id == user.user_id) & (festPostLike.post_id == festpost_id.post_id) ).all()

    if not user_has_liked:
        new_like = crud.create_post_like(user.user_id, festpost.festpost_id)
        print(festpost.like_count)
        festpost.like_count += 1
        db.session.add(festpost)
        db.session.commit()
        print(user_has_liked)
        return jsonify({'added': 'Success!'})
    else:
        # create crud delete_post_like()
        crud.delete_post_like(user.user_id, festpost.festpost_id)
        return jsonify({'added': 'Unliked'})

@app.route('/comment/<int:post_id>', methods=['POST'])
def add_comment(post_id):
    data = request.get_json()
    comment = data.get('comment')

    posts_with_comments = []

    for post in posts_with_comments:
        if post['id'] == post_id:
            post['comments'].append(comment)
            return '' 
        

@app.route('/attend-festival/<int:fest_id>', methods=['POST', 'DELETE'])
def attend_festival_route(fest_id):
    if request.method == 'POST':
        user = crud.get_user_by_email(session["user_email"])  
        if crud.attend_festival(user.user_id, fest_id):  
            return jsonify({'message': 'Successfully attending the festival'}), 200
        else:
            return jsonify({'error': 'User is already attending the festival'}), 400
    else:
        user = crud.get_user_by_email(session["user_email"])

        if crud.unattend_festival(user.user_id, fest_id):
            return jsonify({'message': 'Successfully unattended the festival'}), 200
        else:
            return jsonify({'error': 'User is not attending the festival'}), 400

    

@app.route('/attending-festivals.json', methods=['GET'])
def get_attending_festivals():
    user = crud.get_user_by_email(session["user_email"])

    if user:
        attending_events = crud.get_attending_events(user.user_id)
        attending_festivals = []

        for event in attending_events:
            festival = {
                "fest_id": event.festival.fest_id,
                "fest_name": event.festival.fest_name,
                "fest_location": event.festival.fest_location,
                "fest_startdate": event.festival.fest_startdate,
                "fest_enddate": event.festival.fest_enddate,
                "line_up": event.festival.line_up
            }
            attending_festivals.append(festival)

        return jsonify(attending_festivals)
    else:
        return jsonify({'error': 'User not found'}), 404
    


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



@app.route("/festivals")
def all_festivals():
    festivals = crud.get_festivals()
    return render_template("all_festivals.html", festivals=festivals)  


@app.route("/festivals/<fest_id>")
def show_fest(fest_id):
    festival = crud.get_fest_by_id(fest_id)
    user = crud.get_user_by_email(session["user_email"])
    attend = crud.check_if_attending_fest(user.user_id, festival.fest_id)
   
    fest_head_url = url_for('static', filename=festival.fest_head)
    lineup_img_url = url_for('static', filename=festival.lineup_img)

    return render_template("festival_details.html", festival=festival, fest_head_url=fest_head_url, lineup_img_url=lineup_img_url, attend=attend)



if __name__ == "__main__":
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)
