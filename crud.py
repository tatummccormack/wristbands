from model import db, User, FestivalInfo, connect_to_db, Post, FestPost, Event, PostLike, FestPostLike

#USER
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


   
#FESTIVAL
def create_festival(fest_name, fest_location, fest_startdate, fest_enddate, line_up, fest_head,lineup_img):
    """Make a festival info instance
     example datetime string "2024-04-25 16:46:58,421"
    """
    festival = FestivalInfo(
        fest_name=fest_name,
        fest_location=fest_location,
        fest_startdate= fest_startdate,
        fest_enddate=fest_enddate,
        line_up=line_up,
        fest_head=fest_head,
        lineup_img=lineup_img
    )
    return festival



def get_festivals():
    return FestivalInfo.query.all()

def get_fest_by_id(fest_id):
    return FestivalInfo.query.get(fest_id)

def get_fest_by_name(fest_name):
    return FestivalInfo.query.get(fest_name)

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

def check_if_attending_fest(user_id, fest_id):
    event = Event.query.filter_by(user_id=user_id, fest_id=fest_id).first()
    if event:
        return True
    else:
        return False



#POST 
def create_feed_post(content, user_id):
    new_post = Post(content=content, user_id=user_id)
    db.session.add(new_post)
    db.session.commit()
    return new_post

def get_post_by_id(post_id):
    return Post.query.get(post_id)

def get_all_posts():
    return Post.query.order_by(Post.created_at.desc()).all()

def create_post_like(user_id, post_id):
    new_like = PostLike(user_id=user_id, post_id=post_id)
    db.session.add(new_like)
    db.session.commit()
    return new_like

def delete_post_like(user_id, post_id):
    del_like = PostLike.query.filter( (PostLike.user_id == user_id) & (PostLike.post_id == post_id) ).all()
    for like in del_like:
        db.session.delete(like)
    db.session.commit()
    return del_like



#FESTPOST
def createFest_post(content, user_id, fest_id):
    new_f_post = FestPost(content=content, user_id=user_id, fest_id=fest_id)
    db.session.add(new_f_post)
    db.session.commit()
    return new_f_post

def get_festpost_by_id(festpost_id):
    return FestPost.query.get(festpost_id)

def get_all_fest_posts():
    return FestPost.query.all()

def get_all_posts_by_fest(fest_id):
    fest_id = int(fest_id)
    return FestPost.query.filter(FestPost.fest_id == fest_id).order_by(FestPost.created_at.desc()).all()



    
if __name__ == "__main__":
    from server import app
    connect_to_db(app)


