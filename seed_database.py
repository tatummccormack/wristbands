import os
import json
from random import choice, randint
from datetime import datetime

import crud
import model
import server

os.system('dropdb ratings')
os.system('createdb ratings')

model.connect_to_db(server.app)
model.db.create_all()


user = crud.create_user("Ends", "Noodle", "Stinky Fart Boy", "angry@noodle.com", "fart")
model.db.session.add(user)
model.db.session.commit()

user2 = crud.create_user("Archer", "Barcher", "Goofy Goober", "crazyeyez@dog.com", "rah")
model.db.session.add(user2)
model.db.session.commit()

user3 = crud.create_user("Lettuce", "McSalad", "RubberLettuce81", "ceasar@dressing.com", "Toss")
model.db.session.add(user3)
model.db.session.commit()

start = datetime(2024, 4, 20)
end = datetime(2025, 4, 20)
festival=crud.create_festival("Brochella", "Mojo Dojo Casa House", start, end, "Kens")
model.db.session.add(festival)
model.db.session.commit()

start2 = datetime(2024, 6, 10)
end2 = datetime(2025, 6, 12)
festival2 = crud.create_festival("LA LA LAND", "Island", start2, end2, "lalalers")
model.db.session.add(festival2)
model.db.session.commit()

start3 = datetime(2024, 8, 10)
end3 = datetime(2024, 8, 12)
festival3 = crud.create_festival("Manu", "BeachHouse", start3, end3, "Ye")
model.db.session.add(festival3)
model.db.session.commit()

start4 = datetime(2024, 9, 9)
end4 = datetime(2024, 9, 12)
festival4 = crud.create_festival("JAMZ", "Miami", start4, end4, "Sean Kingston")
model.db.session.add(festival4)
model.db.session.commit()

start5 = datetime(2024, 7, 12)
end5 = datetime(2024, 7, 15)
festival5 = crud.create_festival("bopper boppies", "Airplane", start5, end5, "Miley")
model.db.session.add(festival5)
model.db.session.commit()

start6 = datetime(2024, 7, 20)
end6 = datetime(2024, 7, 23)
festival6 = crud.create_festival("slap city", "central park", start6, end6, "Lady Gaba")
model.db.session.add(festival6)
model.db.session.commit()

start7 = datetime(2024, 6, 20)
end7 = datetime(2024, 6, 23)
festival7 = crud.create_festival("Pretty Girl Rock", "in da cloudz", start7, end7, "yonce")
model.db.session.add(festival7)
model.db.session.commit()

start8 = datetime(2024, 9, 22)
end8 = datetime(2024, 9, 25)
festival8 = crud.create_festival("Groupies", "Trap House", start8, end8, "pussycat dolls")
model.db.session.add(festival8)
model.db.session.commit()

start9 = datetime(2024, 12, 9)
end9 = datetime(2024, 12, 12)
festival9 = crud.create_festival("Vibechella", "lazy river", start9, end9, "Frank")
model.db.session.add(festival9)
model.db.session.commit()

start10 = datetime(2024, 12, 24)
end10 = datetime(2024, 12, 26)
festival10 = crud.create_festival("Jingle UR Bells", "North Pole", start10, end10, "Ri Ri")
model.db.session.add(festival10)
model.db.session.commit()

# with open("data/festivals.json") as f:
#     festival_data = json.loads(f.read())

# festivals_in_db = []
# for festival in festival_data:
#     fest_name, fest_location, line_up, poster_path = (
#         festival["fest_name"],
#         festival["fest_location"],
#         festival["line_up"],
#         festival["poster_path"],
#     )
#     fest_date = datetime.strptime(festival["fest_date"], "%Y-%m-%d")

#     db_festival = crud.create_festival(fest_name, fest_location, fest_date, line_up, poster_path)
#     festivals_in_db.append(db_festival)

# model.db.session.add_all(festivals_in_db)
# model.db.session.commit()