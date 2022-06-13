import os, models, server
from datetime import datetime

os.system("dropdb melonreservations")
os.system("createdb melonreservations")

# Connect to db
models.connect_to_db(server.app)

# Create db tables
models.db.create_all()

# Creating 4 fake users
usernames = ["minalee", "emmadow", "inadow", "johndow"]

for username in usernames:
    new_user = models.User.create_user(username)
    models.db.session.add(new_user)

models.db.session.commit()


# Adding data to reservations table (user_id, registration_date, time_slot)
reservation_dates = ['2022/06/13', '2022/06/11', '2022/06/09', '2022/06/03', '2022/06/01']
timeslots = ['8:00-8:30', '8:30-9:00', 
                 '9:00-9:30', '9:30-10:00', 
                 '10:00-10:30', '10:30-11:00', 
                 '11:00-11:30', '11:30-12:00',
                 '12:00-12:30', '12:30-13:00',
                 '11:00-11:30', '11:30-12:00',
                 '1:00-1:30', '1:30-2:00',
                 '2:00-2:30', '2:30-3:00',
                 '3:00-3:30', '3:30-4:00',
                 '4:00-4:30', '4:30-5:00',
]

all_reservations = []
all_users_ids = []

all_users = models.User.get_users()

for user in all_users:
    all_users_ids.append(user.id)

for i, user_id in enumerate(all_users_ids):
    reservation_dates_pool = reservation_dates.copy()
    for j in range(5 * i, 5 * (i + 1)):
        # Converting string to DateTime object
        datetime_object = datetime.strptime(reservation_dates_pool.pop(), "%Y/%m/%d")
        reservation = models.Reservation.new_reservation(user_id, datetime_object, timeslots[j])
        all_reservations.append(reservation)

models.db.session.add_all(all_reservations)
models.db.session.commit()