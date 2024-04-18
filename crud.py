from model import db, User, FestivalInfo, Event, UserEvent, FestivalPost, Follower, FestivalLike, connect_to_db



def create_user(email, password):
    user = User(email=email, password=password)
    return user

def get_users():
    return User.query.all()


def get_user_by_id(user_id):
    return User.query.get(user_id)



def create_festival(title, lineup, date, location):

    festival = festival(
        title=title,
        lineup=lineup,
        date= date,
        location=location,
    )

    return festival



def get_festivals():
    return FestivalInfo.query.all()


def get_fest_by_id(fest_id):
    return FestivalInfo.query.get(fest_id)



def create_event(title, date, time, location):

    event = event(
        title=title,
        date=date,
        time=time,
        location=location,
    )

    return event

def create_festPost(title, content, createdAt):

    festPost = festPost(
        title=title,
        content=content,
        createdAt=createdAt,
    )

    return festPost

