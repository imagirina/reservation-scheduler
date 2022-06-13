from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import UniqueConstraint

db = SQLAlchemy()

class User(db.Model):

    __tablename__ = "users"

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    username = db.Column(db.String(50), nullable=False, unique=True)

    def __repr__(self):
        return f"<User id={self.id} username={self.username}>"

    @classmethod
    def create_user(cls, username):
        """ Create and return a new user """

        username = username.lower()

        user = cls(username=username)

        db.session.add(user)
        db.session.commit()

        return user

    @classmethod
    def get_user_by_username(cls, username):
        """ Return a user by username """

        return cls.query.filter(cls.username == username).first()

    @classmethod 
    def get_users(cls):
        """ Return all users """

        return cls.query.all()


class Reservation(db.Model):

    __tablename__="reservations"
    # Declare the composite UniqueConstraint as part of the __table_args__
    __table_args__=(db.UniqueConstraint('reservation_date', 'time_slot', name='uix_1'),
                    db.UniqueConstraint('user_id', 'reservation_date', name='uix_2'),)

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    reservation_date = db.Column(db.DateTime, nullable=False)
    time_slot = db.Column(db.String(15), nullable=False)

    user = db.relationship("User", backref="reservations")


    @classmethod
    def new_reservation(cls, user_id, datetime_object, timeslot):
        """ Create and add a new reservation """

        reservation = cls(user_id=user_id, reservation_date=datetime_object, time_slot=timeslot)

        db.session.add(reservation)
        db.session.commit()

        return reservation

    @classmethod
    def get_reservations(cls, user_id):
        """ Get all reservations for user """

        return cls.query.filter(cls.user_id==user_id).all()


    @classmethod
    def get_timeslots_for_date(cls, reservation_date):
        """ Get all timeslots for date  """

        reservations = cls.query.filter(cls.reservation_date == reservation_date).all()
        return [r.time_slot for r in reservations]


    @classmethod
    def delete_reservation(cls, reservation_id):
        """ Delete reservation by id from DB """

        cls.query.where(cls.id == reservation_id).delete()
        db.session.commit()


    def __repr_(self):
        return f"<Reservation id={self.id}, user={self.user_id}>"


def connect_to_db(flask_app, echo=True):
    """ Connect the database to our Flask app """

    flask_app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///melonreservations'
    flask_app.config['SQLALCHEMY_ECHO'] = echo # True by default (enable output of the raw SQL executed by SQLAlchemy)
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Connect DB with the Flask app
    db.app = flask_app
    db.init_app(flask_app)

# if __name__ == "__main__":
#     print("<================>")
#     from server import app

#     # To prevent SQLAlchemy from printing every query it executes into STDOUT,
#     # call connect_to_db(flask_app, echo=False)
#     connect_to_db(app)