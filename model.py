from datetime import datetime, timezone
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):

    __tablename__ = "users"

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    username = db.Column(db.String(30))
    fname = db.Column(db.String(30))
    lname= db.Column(db.String(30))
    password = db.Column(db.String)
    email = db.Column(db.String, unique=True)
    bio = db.Column(db.Text) 
    avatar = db.Column(db.String) #path to the file
    
    post = db.relationship("Post", back_populates="user")
    festpost = db.relationship("FestPost", back_populates="user")
    events = db.relationship("Event", back_populates="user")
    postlikes = db.relationship("PostLike", back_populates="user")
    festpostlikes = db.relationship("FestPostLike", back_populates="user")


class Event(db.Model):

    __tablename__ = "events"

    event_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    fest_id = db.Column(db.Integer, db.ForeignKey('festivals.fest_id'))

    user = db.relationship("User", back_populates="events")
    festival = db.relationship("FestivalInfo", back_populates="events")


class FestivalInfo(db.Model):

    __tablename__ = "festivals"

    fest_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    fest_name = db.Column(db.String)
    fest_location = db.Column(db.String)
    fest_startdate = db.Column(db.DateTime)
    fest_enddate = db.Column(db.DateTime)
    line_up = db.Column(db.String)

    festposts = db.relationship("FestPost", back_populates="festival")
    events = db.relationship("Event", back_populates="festival")

    def __repr__(self):
        return f"<FestivalInfo fest_id={self.fest_id} fest_name={self.fest_name}>" 

    
class FestPost(db.Model):

    __tablename__ = "festposts"

    festpost_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    content = db.Column(db.String(300))
    fest_id = db.Column(db.Integer, db.ForeignKey('festivals.fest_id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    like_count = db.Column(db.Integer, default=0)

    user = db.relationship("User", back_populates="festpost")
    festival = db.relationship("FestivalInfo", back_populates="festposts")
    likes = db.relationship("FestPostLike", back_populates="festpost")


    def __repr__(self):
        return f"<FestPost(festpost_id={self.festpost_id}, content='{self.content}, likes={self.likes})>" 
    

class FestPostLike(db.Model):
    __tablename__ = "festpostlikes"

    festpostlike_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    festpost_id = db.Column(db.Integer, db.ForeignKey('festposts.festpost_id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))

    festpost = db.relationship("FestPost", back_populates="likes")
    user = db.relationship("User", back_populates="festpostlikes")


class Post(db.Model):

    __tablename__ = "posts"

    post_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    content = db.Column(db.String(300))
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    created_at = db.Column(db.DateTime, default=datetime.now(timezone.utc))
    like_count = db.Column(db.Integer, default=0)

    user = db.relationship("User", back_populates="post")
    likes = db.relationship("PostLike", back_populates="post")

    def __repr__(self):
        return f"<Post(post_id={self.post_id}, content='{self.content}, likes={self.likes})>"


class PostLike(db.Model):
    __tablename__ = "postlikes"

    postlike_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    post_id = db.Column(db.Integer, db.ForeignKey('posts.post_id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))

    post = db.relationship("Post", back_populates="likes")
    user = db.relationship("User", back_populates="postlikes")


def connect_to_db(flask_app, db_uri="postgresql:///ratings", echo=True):
    flask_app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
    flask_app.config["SQLALCHEMY_ECHO"] = echo
    flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.app = flask_app
    db.init_app(flask_app)

    print("Connected to the db!")

if __name__ == "__main__":
    from server import app
    connect_to_db(app)