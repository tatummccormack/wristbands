from model import db, User, FestivalInfo, connect_to_db, Post, FestPost, Event
# ^, Event, UserEvent, 



def create_user(fname, lname, username, email, password):
    user = User(fname=fname, lname=lname,username=username, email=email, password=password)
    return user

def get_users():
    return User.query.all()


def get_user_by_email(email):
    return User.query.filter(User.email == email).first()


def get_user_by_id(user_id):
    return User.query.get(user_id)

def get_user_by_username(username):
    return User.query.filter(User.username == username).first()
    

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



def get_festivals():
    return FestivalInfo.query.all()


def get_fest_by_id(fest_id):
    return FestivalInfo.query.get(fest_id)

def get_fest_by_name(fest_name):
    return FestivalInfo.query.get(fest_name)


def create_feed_post(content, user_id):
    new_post = Post(content=content, user_id=user_id)
    db.session.add(new_post)
    db.session.commit()
    return new_post

def get_post_by_id(post_id):
    return Post.query.get(post_id)


def get_all_posts():
    return Post.query.order_by(Post.created_at.desc()).all()


def createFest_post(content, user_id, fest_id):
    new_f_post = FestPost(content=content, user_id=user_id, fest_id=fest_id)
    db.session.add(new_f_post)
    db.session.commit()
    return new_f_post

def get_all_fest_posts():
    return FestPost.query.all()

def get_all_posts_by_fest(fest_id):
    fest_id = int(fest_id)
    return FestPost.query.filter(FestPost.fest_id == fest_id).all()

def get_attending_festivals(user_id):
    user = User.query.get(user_id)
    if user:
        return [event.festival for event in user.events]
    return []

def attend_festival(user_id, fest_id):
    event = Event.query.filter_by(user_id=user_id, fest_id=fest_id).first()
    if event:
        return False
    new_event = Event(user_id=user_id, fest_id=fest_id)
    db.session.add(new_event)
    db.session.commit()
    return True

def unattend_festival(user_id, fest_id):
    
    event = Event.query.filter_by(user_id=user_id, fest_id=fest_id).first()
    if event:
        db.session.delete(event)
        db.session.commit()
        return True
    else:
        return False 

# def get_all_posts_by_fest(fest_id):
#     return FestPost.query.get(fest_id)

# def like_post(post_id):
#     post = get_post(post_id)
#     if post:
#         post.likes += 1
#         db.session.commit()
#         return post
#     return None

# def unlike_post(post_id):
#     post = get_post(post_id)
#     if post and post.likes > 0:
#         post.likes -= 1
#         db.session.commit()
#         return post
#     return None
    

# def get_follower_by_id(follower_id):
#     return Follower.query.get(follower_id)

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

# def post_like(post_id):
#     post = get_post_by_id(post_id)
#     if post:
#         post.likes += 1 
#         db.session.commit()
#         return post
#     return None

# def unlike_post(post_id):
#     post = get_post_by_id(post_id)
#     if post and post.likes > 0:
#         post.likes -= 1
#         db.session.commit()
#         return post
#     return None

# def fest_like(fest_id):
#     fest = get_fest_by_id(fest_id)
#     if fest:
#         fest.likes += 1 
#         db.session.commit()
#         return fest
#     return None

# def unlike_fest(fest_id):
#     fest = get_fest_by_id(fest_id)
#     if fest and fest.likes > 0:
#         fest.likes -= 1
#         db.session.commit()
#         return fest
#     return None

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

    
if __name__ == "__main__":
    from server import app
    connect_to_db(app)