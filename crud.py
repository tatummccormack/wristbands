from model import db, User, FestivalInfo, connect_to_db
# ^, Event, UserEvent, FestivalPost, Follower, 



def create_user(fname, lname, username, email, password):
    user = User(fname=fname, lname=lname,username=username, email=email, password=password)
    return user

def get_users():
    return User.query.all()


def get_user_by_email(email):
    return User.query.filter(User.email == email).first()


def get_user_by_id(user_id):
    return User.query.get(user_id)

def create_festival(fest_name, fest_location, fest_startdate, fest_enddate, line_up):
    """Make a festival info instance
     example datetime string "2024-04-25 16:46:58,421"
    """
    festival = FestivalInfo(
        fest_name=fest_name,
        fest_location=fest_location,
        fest_startdate= fest_startdate,
        fest_enddate=fest_enddate,
        line_up=line_up
    )

    return festival



# def get_festivals():
#     return FestivalInfo.query.all()


# def get_fest_by_id(fest_id):
#     return FestivalInfo.query.get(fest_id)



# def create_event(title, date, time, location):

#     event = event(
#         title=title,
#         date=date,
#         time=time,
#         location=location,
#     )

#     return event

# def get_event():
#     return Event.query.all()

# # def get_event_by_user():
# #     return UserEvent.query.get(user_attending)


# def create_festPost(title, content, createdAt):

#     festPost = festPost(
#         title=title,
#         content=content,
#         createdAt=createdAt,
#     )

#     return festPost

# def get_festPost():
#     return FestivalPost.query.all()

# def follow_user(follower_id, followee_id):
#     existing_follower = Follower.query.filter_by(follower_id=follower_id, followee_id=followee_id).first()
#     if existing_follower:
#         return False
    
#     new_follower = Follower(follower_id=follower_id, followee_id=followee_id)
#     db.session.add(new_follower)
#     db.session.commit()

#     return True
                                                                                
# def unfollow_user(follower_id, followee_id):
#     follower_to_delete = Follower.query.filter_by(follower_id=follower_id, followee_id=followee_id).first()
#     if not follower_to_delete:
#         return False
    
#     db.session.delete(follower_to_delete)
#     db.session.commit()

#     return True

# # def fest_like():
    

# # def post_like():
    
if __name__ == "__main__":
    from server import app

    connect_to_db(app)