from datetime import datetime
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
    # phone_num = db.Column(db.Integer())
    # dob = db.Column(db.Integer())
    #user_icon = db.Column(db.img?)


class FestivalInfo(db.Model):

    __tablename__ = "festivals"

    fest_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    fest_name = db.Column(db.String)
    fest_location = db.Column(db.String)
    fest_startdate = db.Column(db.DateTime)
    fest_enddate = db.Column(db.DateTime)
    line_up = db.Column(db.String)

    def __repr__(self):
        return f"<FestivalInfo fest_id={self.fest_id} fest_name={self.fest_name}>" 



# class Event(db.Model):

#     __tablename__ = "events"

#     event_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
#     date = db.Column(db.DateTime)
#     time = db.Column(db.DateTime)
#     ev_location = db.Column(db.String)
#     sched_id = db.Column(db.Integer)
#     fest_id = db.Column(db.Integer, db.ForeignKey('festivals.fest_id'))

#     festival = db.relationship("festivalInfo", back_populates="event")

#     #def__repr__(self):
#         # return f"<Event event_id={self.event_id} fest_name={self.fest_name>" 



# class UserEvent(db.Model):

#     __tablename__ = "user events"
    
#     user_event_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
#     user_attending = db.Column(db.Boolean)
#     user_id=db.Column(db.Integer, db.ForeignKey('users.user_id'))
#     event_id=db.Column(db.Integer, db.ForeignKey('events.event_id'))

#     user = db.relationship("user", back_populates="userevent")

#     # sched_id=db.Column(db.Integer, db.ForeignKey('events.sched_id'))

#     #def__repr__(self):
#         # return f"<User_event_id={self.user_event_id} user_attenting={self.user_attenting>" 



# class FestivalPost(db.Model):

#     __tablename__ = "posts"

#     fchat_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
#     content = db.Column(db.String(300))
#     createdAt = db.Column(db.DateTime)

#     fest_id = db.Column(db.Integer, db.ForeignKey('festivals.fest_id'))
#     user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))

#     festivals = db.relationship("festival", back_populates="festivalpost")
#     users = db.relationship("user", back_populates="festivalpost")



# class Follower(db.Model):

#     __tablename__ = "followers"

#     following_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
#     follower_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
#     followee_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))



# class FestivalLike(db.Model):

#     __tablename__ = "festival likes"

#     like_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
#     fest_id = db.Column(db.Integer, db.ForeignKey('festivals.fest_id'))
#     user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))

#     festival= db.relationship("festivalinfo", back_populates="festivallike")
#     users = db.relationship("user", back_populates="festivalpost")



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