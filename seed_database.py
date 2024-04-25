import json
from random import choice, randint
from datetime import datetime

import crud
import model
import server

model.connect_to_db(server.app)
model.db.create_all()

with open("data/festivals.json") as f:
    festival_data = json.loads(f.read())

festivals_in_db = []
for festival in festival_data:
    fest_name, fest_location, line_up, poster_path = (
        festival["fest_name"],
        festival["fest_location"],
        festival["line_up"],
        festival["poster_path"],
    )
    fest_date = datetime.strptime(festival["fest_date"], "%Y-%m-%d")

    db_festival = crud.create_festival(fest_name, fest_location, fest_date, line_up, poster_path)
    festivals_in_db.append(db_festival)

model.db.session.add_all(festivals_in_db)
model.db.session.commit()